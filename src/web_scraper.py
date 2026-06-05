from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time


def scrape_books():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    url = "https://books.toscrape.com/"
    driver.get(url)

    time.sleep(3)

    books = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")

    data = []

    for book in books:
        title = book.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
        price_text = book.find_element(By.CSS_SELECTOR, "p.price_color").text

        price = float(
            price_text
            .replace("£", "")
            .strip()
        )

        data.append({
            "Product": title,
            "Price_USD": price,
            "Demand": 70,
            "Trend": 70,
            "Competition": 50
        })

    driver.quit()

    df = pd.DataFrame(data)

    df.to_csv("data/products.csv", index=False)

    print("Scraping completed successfully")
    print(df)


if __name__ == "__main__":
    scrape_books()