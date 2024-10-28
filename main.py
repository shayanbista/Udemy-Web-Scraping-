from scraper.udemy_scraper import scrape_udemy_courses

from config.settings import COURSE_CATEGORY_URL


def main():
    print("Starting Udemy scraper...")

    courses = scrape_udemy_courses(COURSE_CATEGORY_URL)


if __name__ == "__main__":
    main()
