
# Udemy Web Scraper

This project is a web scraper for Udemy course categories and subcategories, built using **Python**, **BeautifulSoup**, **Selenium**, and **OpenPyXL**. The scraper collects course information such as course titles, URLs, ratings, number of reviews, and prices, and saves the data to an Excel file.

## **Project Structure**

```
udemy_scraper/
├── config/
│   └── settings.py            # Stores URLs and configuration settings
├── data/                      # Stores Excel files generated by the scraper
├── scraper/
│   ├── __init__.py            # Marks this as a package
│   ├── udemy_scraper.py       # Main scraping logic
│   └── udemy_subcategories.py # Handles scraping of subcategories
├── scripts/
│   ├── __init__.py            # Marks this as a package
│   └── utils.py               # Utility functions for Excel operations
└── main.py                    # Entry point to run the scraper
```

---

## **Features**

- **Scrapes course categories and subcategories** from Udemy.
- **Extracts detailed course data** (title, URL, rating, reviews, price, etc.).
- **Stores the extracted data** in an Excel file inside the `data/` directory.
- **Modular design** for easy maintenance and scaling.

---

## **Prerequisites**

Make sure you have the following installed:

- **Python 3.x**
- **pip** (Python package manager)

---

## **Installation**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/<your-username>/Udemy-Web-Scraping.git
   cd Udemy-Web-Scraping
   ```

2. **Set up a virtual environment (optional but recommended)**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scriptsctivate
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## **Configuration**

Modify the **URLs and settings** in the `config/settings.py` file.

```python
# config/settings.py

BASE_URL = "https://www.udemy.com"
COURSE_CATEGORY_URL = "https://www.udemy.com/courses/development/"
```

---

## **How to Run**

1. Ensure you are in the project root directory.

2. Run the scraper with the following command:

   ```bash
   python main.py
   ```

3. The scraped data will be saved in an Excel file under the `data/` directory.

---

## **Usage Example**

The scraper extracts detailed information such as:

- Course Title
- Course URL
- Rating
- Number of Reviews
- Total Hours
- Price (Original and Discounted)

---

## **Project Dependencies**

- **BeautifulSoup** – For parsing HTML
- **Selenium** – For handling dynamic web pages
- **OpenPyXL** – For working with Excel files
- **webdriver-manager** – For managing Selenium drivers

---

## **Contributing**

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss your ideas.

---

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## **Troubleshooting**

If you encounter any issues, please open an issue on the [GitHub repository](https://github.com/<your-username>/Udemy-Web-Scraping).
