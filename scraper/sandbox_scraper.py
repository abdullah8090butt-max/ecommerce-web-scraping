from playwright.sync_api import sync_playwright
import pandas as pd
from pathlib import Path

BASE_URL = "https://scrapingsandbox.com"
TARGET_PRODUCTS = 120

products = []

# Project root folder
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Data folder
DATA_FOLDER = PROJECT_ROOT / "data"
DATA_FOLDER.mkdir(exist_ok=True)


with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto(BASE_URL, wait_until="networkidle")

    page_number = 1

    while len(products) < TARGET_PRODUCTS:

        print(f"\n========== Page {page_number} ==========")

        # Wait for products
        page.locator("a.product-card").first.wait_for()

        product_cards = page.locator("a.product-card")
        count = product_cards.count()

        print("Products on current page:", count)

        # Extract products
        for i in range(count):

            product = product_cards.nth(i)

            name = product.locator(
                "h3.product-name"
            ).inner_text().strip()

            price = product.locator(
                "span.price"
            ).inner_text().strip()

            rating = product.locator(
                "span.rating"
            ).inner_text().strip()

            availability = product.locator(
                "span.availability"
            ).inner_text().strip()

            product_url = BASE_URL + product.get_attribute("href")

            products.append({
                "Product Name": name,
                "Price": price,
                "Rating": rating,
                "Availability": availability,
                "Product URL": product_url
            })

            if len(products) >= TARGET_PRODUCTS:
                break

        print("Total collected:", len(products))

        # Stop when target is reached
        if len(products) >= TARGET_PRODUCTS:
            break

        # Move to next page
        next_page_number = page_number + 1

        print("Moving to page:", next_page_number)

        # Find the numbered pagination button
        next_button = page.get_by_role(
            "button",
            name=str(next_page_number),
            exact=True
        )

        if next_button.count() == 0:
            print("Next page button not found.")
            break

        # Click next page
        next_button.click()

        # Wait for the product list to update
        page.wait_for_timeout(1000)

        page_number += 1

    browser.close()


# Convert to DataFrame
df = pd.DataFrame(products)


# Remove duplicate products
df = df.drop_duplicates(subset=["Product URL"])


print("\n================================")
print("FINAL RESULTS")
print("================================")

print("Total unique products:", len(df))

print("\nFirst 5 products:")
print(df.head())


# Save CSV
csv_path = DATA_FOLDER / "sandbox_products.csv"
df.to_csv(csv_path, index=False)


# Save Excel
excel_path = DATA_FOLDER / "sandbox_products.xlsx"
df.to_excel(excel_path, index=False)


print("\nFiles saved successfully!")

print("CSV:", csv_path)
print("Excel:", excel_path)