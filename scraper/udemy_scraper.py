import requests

import time
import sys
import os

from bs4 import BeautifulSoup

from openpyxl import Workbook, load_workbook
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from config.settings import BASE_URL

from .udemy_subcategories import scrape_subcategories


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../utils")))

from excel_utils import create_excel_file, write_courses_to_excel


def scrape_udemy_courses(category_url):
    response = requests.get(category_url)

    if response.status_code != 200:
        print(
            f"Failed to retrieve page from {category_url}: Status code {response.status_code}"
        )
        return

    soup = BeautifulSoup(response.content, "html.parser")
    category_name = (
        soup.find("h1").text.strip() if soup.find("h1") else "Unknown Category"
    )

    sub_categories_links = []
    category = soup.find("a", class_="js-side-nav-cat")

    if category:
        subcategory_div = category.find_next_sibling("div")
        if subcategory_div:
            sub_categories = subcategory_div.find_all(
                "a", class_=["js-side-nav-cat", "js-subcat"], href=True
            )
            for sub_category in sub_categories:
                sub_categories_links.append(
                    {
                        "name": sub_category.text.strip(),
                        "url": BASE_URL + sub_category["href"],
                    }
                )

    for sub_cat in sub_categories_links:
        data = scrape_subcategories(sub_cat["url"], BASE_URL, num_pages=1)
        write_courses_to_excel(category_name, sub_cat["name"], sub_cat["url"], data)
        time.sleep(2)


create_excel_file()
