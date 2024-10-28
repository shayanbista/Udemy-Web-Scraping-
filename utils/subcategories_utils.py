from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def extract_course_title(course_element):
    """
    Extracts and cleans course title from a course element, handling nested elements properly.

    Args:
        course_element: BeautifulSoup element containing the course information

    Returns:
        str: Cleaned course title
    """
    if course_element.find("a"):
        anchor = course_element.find("a")

        direct_texts = [
            text for text in anchor.children if isinstance(text, str) and text.strip()
        ]

        course_title = " ".join(text.strip() for text in direct_texts)
        course_title = " ".join(course_title.split())
        return course_title

    return "N/A"


def setup_driver():
    """
    Sets up the Chrome WebDriver with necessary options.

    Returns:
        WebDriver: Configured Chrome WebDriver instance.
    """
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    )
    return webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chrome_options
    )
