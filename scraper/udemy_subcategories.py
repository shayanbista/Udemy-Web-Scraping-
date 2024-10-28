import sys
import os
import time


from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../utils")))

from subcategories_utils import extract_course_title, setup_driver


def scrape_subcategories(url, base_url, num_pages):
    all_course_data = []

    for current_page in range(1, num_pages + 1):
        time.sleep(10)

        driver = setup_driver()
        dynamic_url = f"{url}?p={current_page}"

        print(f"Fetching page {current_page} with URL: {dynamic_url}")

        try:
            driver.get(dynamic_url)

            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "[data-purpose='course-title-url']")
                )
            )

            page_content = driver.page_source
            soup = BeautifulSoup(page_content, "html.parser")

            course_title_elements = soup.find_all(
                attrs={"data-purpose": "course-title-url"}
            )

            for course_element in course_title_elements[4:]:
                course_info_div = course_element.find_next(
                    "div", {"aria-hidden": "true"}
                )
                if course_info_div:
                    course_title = extract_course_title(course_element)
                    course_href = (
                        base_url + course_element.find("a")["href"]
                        if course_element.find("a")
                        else None
                    )
                    course_description = (
                        course_info_div.find(
                            "span", {"data-testid": "seo-headline"}
                        ).text.strip()
                        if course_info_div.find("span", {"data-testid": "seo-headline"})
                        else "N/A"
                    )
                    rating = (
                        course_info_div.find(
                            "span", {"data-testid": "seo-rating"}
                        ).text.strip()
                        if course_info_div.find("span", {"data-testid": "seo-rating"})
                        else "N/A"
                    )
                    num_reviews = (
                        course_info_div.find(
                            "span", {"data-testid": "seo-num-reviews"}
                        ).text.strip()
                        if course_info_div.find(
                            "span", {"data-testid": "seo-num-reviews"}
                        )
                        else "N/A"
                    )
                    total_hours = (
                        course_info_div.find(
                            "span", {"data-testid": "seo-content-info"}
                        ).text.strip()
                        if course_info_div.find(
                            "span", {"data-testid": "seo-content-info"}
                        )
                        else "N/A"
                    )
                    num_lectures = (
                        course_info_div.find(
                            "span", {"data-testid": "seo-num-lectures"}
                        ).text.strip()
                        if course_info_div.find(
                            "span", {"data-testid": "seo-num-lectures"}
                        )
                        else "N/A"
                    )
                    level = (
                        course_info_div.find(
                            "span", {"data-testid": "seo-instructional-level"}
                        ).text.strip()
                        if course_info_div.find(
                            "span", {"data-testid": "seo-instructional-level"}
                        )
                        else "N/A"
                    )
                    prices = scrape_subsections(course_href)
                    time.sleep(5)
                    all_course_data.append(
                        {
                            "title": course_title,
                            "url": course_href,
                            "description": course_description,
                            "rating": rating,
                            "num_reviews": num_reviews,
                            "total_hours": total_hours,
                            "num_lectures": num_lectures,
                            "level": level,
                            **(
                                prices
                                if prices
                                else {
                                    "current_price": "N/A",
                                    "original_price": "N/A",
                                    "discount": "N/A",
                                }
                            ),
                        }
                    )
        except Exception as e:
            print(f"Error occurred while fetching page {current_page}: {e}")
        finally:
            driver.quit()

    print("Scraping complete.")
    return all_course_data


def scrape_subsections(url, file_name="pased.html"):

    try:
        driver = setup_driver()
        driver.get(url)
        time.sleep(5)
        page_content = driver.page_source

        soup = BeautifulSoup(page_content, "html.parser")

        original_price_label = soup.find(
            "span", class_="ud-sr-only", string="Original Price"
        )
        original_price = (
            original_price_label.find_next("span").find("s").find("span").text.strip()
            if original_price_label
            else "N/A"
        )

        current_price_label = soup.find(
            "span", class_="ud-sr-only", string="Current price"
        )
        current_price = (
            current_price_label.find_next("span").find("span").text.strip()
            if current_price_label
            else "N/A"
        )

        discount_label = soup.find("span", class_="ud-sr-only", string="Discount")
        discount = (
            discount_label.find_next("span").text.strip() if discount_label else "N/A"
        )

        scraped_prices = {
            "current_price": current_price,
            "original_price": original_price,
            "discount": discount,
        }

        print("scraped prices", scraped_prices)

        return scraped_prices

    except Exception as e:
        print(f"Error occurred while fetching page {current_page}: {e}")
    finally:
        driver.quit()
