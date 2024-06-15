import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://books.toscrape.com/catalogue/page-{}.html"
titles = []
prices = []
availability = []


def scrape_page (page_num):
    url = base_url.format(page_num)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    books_data = soup.find_all("article", class_="product_pod")

    for book in books_data:
        titles.append(book.h3.a["title"])
        price_text = book.find("p", class_="price_color").text.strip()
        price = price_text.replace('Â', '')
        prices.append(price)
        availability.append(book.find("p", class_="instock").text.strip())


for page in range(1, 6):
    scrape_page(page)

books = pd.DataFrame({
    "title": titles,
    "price": prices,
    'availability': availability
    })

books.to_csv('books.csv', index=False)

print("may the force be with you")