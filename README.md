# E-Commerce Web Scraping & Data Analysis

A Python-based e-commerce web scraping and data analysis project that collects product information from a public practice website, cleans the data, performs analysis, creates visualizations, and provides a Streamlit search interface.

## Project Features

- Scrape 500 e-commerce products
- Automatic pagination using Playwright
- Extract product name, price, rating, availability, and product URL
- Clean and validate scraped data using Pandas
- Remove duplicate products
- Save data in CSV and Excel formats
- Perform product price and rating analysis
- Create data visualizations using Matplotlib
- Search products through a Streamlit web interface

## Technologies Used

- Python
- Playwright
- Requests
- BeautifulSoup
- Pandas
- OpenPyXL
- Matplotlib
- Jupyter Notebook
- Streamlit

## Project Structure

ecommerce-web-scraping/

├── scraper/

│   └── sandbox_scraper.py

├── data/

│   ├── sandbox_products.csv

│   ├── sandbox_products.xlsx

│   ├── sandbox_products_cleaned.csv

│   └── sandbox_products_cleaned.xlsx

├── output/

├── notebooks/

│   └── sandbox_analysis.ipynb

├── app.py

├── requirements.txt

├── README.md

└── .gitignore

## Scraped Data

The scraper collects the following fields:

- Product Name
- Price
- Rating
- Availability
- Product URL

## Data Analysis

The project analyzes:

- Total number of products
- Average product price
- Minimum product price
- Maximum product price
- Most common rating
- Available products
- Highest-rated products
- Lowest-priced products

## Visualizations

The analysis notebook includes:

- Price distribution
- Rating distribution
- Price vs Rating
- Product analysis charts

## Streamlit Application

The project includes a Streamlit web interface that allows users to:

- Search for products by name
- View product price
- View product rating
- View product availability
- Open the product URL
- Browse all scraped products

## Installation

Clone the repository:

git clone https://github.com/abdullah8090butt-max/ecommerce-web-scraping.git

Move into the project directory:

cd ecommerce-web-scraping

Install the required libraries:

pip install -r requirements.txt

Install Playwright browser:

playwright install chromium

## Run the Scraper

python scraper/sandbox_scraper.py

## Run the Streamlit App

streamlit run app.py

## Author

Abdullah Butt

AI & Python Developer