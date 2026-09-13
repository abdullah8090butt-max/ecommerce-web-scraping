# E-Commerce Product Web Scraper


A Python-based web scraping project that collects e-commerce product data from Scraping Sandbox, cleans and analyzes the data, and generates useful visualizations.

## Project Overview

This project is a Python-based e-commerce web scraper built to collect, clean, analyze, and visualize product data from a public practice website.

The scraper uses Playwright to navigate multiple pages automatically and collects product names, prices, ratings, availability, and product URLs.

The collected data is cleaned using Pandas and exported to CSV and Excel files. A Jupyter Notebook is then used to perform data analysis and create visualizations with Matplotlib.
A Python-based web scraping project that collects e-commerce product data from Scraping Sandbox, cleans and analyzes the data, and generates useful visualizations.
## Features

- Scrapes product data from multiple pages
- Automatic pagination
- Collects product name, price, rating, availability, and product URL
- Cleans and validates scraped data
- Removes duplicate products
- Saves data in CSV and Excel formats
- Performs basic data analysis using Pandas
- Generates data visualizations using Matplotlib
- Handles 120 products for analysis
- ## Technologies Used

- Python
- Requests
- BeautifulSoup
- Playwright
- Pandas
- OpenPyXL
- Matplotlib
- Jupyter Notebook
- ## Project Structure

```text
ecommerce-web-scraping/
├── scraper/
│   ├── books_scraper.py
│   └── sandbox_scraper.py
├── data/
│   ├── sandbox_products.csv
│   ├── sandbox_products.xlsx
│   ├── sandbox_products_cleaned.csv
│   └── sandbox_products_cleaned.xlsx
├── output/
├── notebooks/
│   └── sandbox_analysis.ipynb
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
## Data Analysis

The scraped dataset contains 120 unique products.

The analysis includes:

- Total number of products
- Average, minimum, and maximum price
- Most common product rating
- Product availability analysis
- Highest-rated products
- Lowest-priced products
- Price distribution
- Rating distribution
- Price vs. rating relationship
- Product availability visualization
## Results

After scraping and cleaning the data:

- **Total Products:** 120
- **Average Price:** $104.80
- **Minimum Price:** $6.22
- **Maximum Price:** $204.29
- **Most Common Rating:** 3.6
- **In Stock:** 102 products (85%)
- **Out of Stock:** 18 products (15%)

The cleaned dataset is available in both CSV and Excel formats.
## How to Run

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd ecommerce-web-scraping
## Author

**Abdullah Butt**

AI & Python Developer

- GitHub: https://github.com/abdullah8090butt-max
- LinkedIn: https://linkedin.com/in/abdullah-butt-878a31429