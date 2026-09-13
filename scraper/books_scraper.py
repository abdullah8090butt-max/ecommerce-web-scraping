import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

products = []

for page in range(1, 6):
    url = base_url.format(page)

    response = requests.get(url)
    print("Page", page, "Status:", response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.find("h3").find("a")["title"]

        price = book.find("p", class_="price_color").text

        rating = book.find("p", class_="star-rating")["class"][1]

        availability = book.find(
            "p", class_="instock availability"
        ).get_text(strip=True)

        product_url = "https://books.toscrape.com/" + book.find(
            "h3"
        ).find("a")["href"]

        product = {
            "Product Name": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability,
            "Product URL": product_url
        }

        products.append(product)

    time.sleep(1)

print("Total products collected:", len(products))

df = pd.DataFrame(products)

# Clean Price
df["Price"] = (
    df["Price"]
    .str.replace("Â£", "", regex=False)
    .str.replace("£", "", regex=False)
    .str.strip()
    .astype(float)
)

# Convert Rating to numbers
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating"] = df["Rating"].map(rating_map)

# Clean Product Names
df["Product Name"] = df["Product Name"].str.strip()

print(df.head())
print("Total products:", len(df))

# Save CSV
df.to_csv("../data/books_products.csv", index=False)

print("CSV file saved successfully!")
df.to_excel("../data/books_products.xlsx", index=False)

print("Excel file saved successfully!")