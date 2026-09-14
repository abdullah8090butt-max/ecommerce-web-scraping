import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="E-Commerce Product Search",
    page_icon="🛍️",
    layout="wide"
)

# Load Product Data
df = pd.read_csv("data/sandbox_products_cleaned.csv")

# Main Page
st.title("🛍️ E-Commerce Product Search")

st.write(
    "Search and explore product information collected "
    "from an e-commerce website."
)

# Instructions
st.info(
    """
🔎 How to use this application

1. Enter a product name in the search box.
2. Click Search to find matching products.
3. Or click Browse All Products to explore the dataset.
4. View the product price, rating, availability, and URL.
"""
)

# Dataset Information
st.metric(
    "📊 Total Products",
    len(df)
)

# Search Box
search_query = st.text_input(
    "🔎 Search for a product",
    placeholder="Example: lamp, tea, camera..."
)

# Buttons
col1, col2 = st.columns(2)

with col1:
    search_button = st.button(
        "🔍 Search",
        type="primary",
        use_container_width=True
    )

with col2:
    browse_button = st.button(
        "📋 Browse All Products",
        use_container_width=True
    )

# Search Products
if search_button:

    if search_query.strip():

        query = search_query.strip().lower()

        results = df[
            df["Product Name"]
            .str.lower()
            .str.contains(query, na=False)
        ]

        if not results.empty:

            st.success(
                f"Found {len(results)} product(s) "
                f"matching '{search_query}'."
            )

            for _, product in results.iterrows():

                st.subheader(
                    f"📦 {product['Product Name']}"
                )

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.write("💰 Price")
                    st.write(
                        f"${product['Price']:.2f}"
                    )

                with col2:
                    st.write("⭐ Rating")
                    st.write(
                        product["Rating"]
                    )

                with col3:
                    st.write("📦 Availability")
                    st.write(
                        product["Availability"]
                    )

                st.markdown(
                    f"[🔗 View Product]({product['Product URL']})"
                )

                st.divider()

        else:

            st.warning(
                f"No products found for '{search_query}'."
            )

    else:

        st.warning(
            "Please enter a product name before searching."
        )

# Browse All Products
if browse_button:

    st.subheader("📋 All Products")

    st.success(
        f"Showing all {len(df)} products."
    )

    display_df = df[
        [
            "Product Name",
            "Price",
            "Rating",
            "Availability",
            "Product URL"
        ]
    ].copy()

    display_df["Price"] = display_df["Price"].apply(
        lambda x: f"${x:.2f}"
    )

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )

# About Project
st.divider()

st.subheader("ℹ️ About This Project")

st.write(
    "This application provides a simple interface for "
    "searching and exploring products collected through "
    "a Python web-scraping project using Playwright and Pandas."
)

st.caption(
    "Developed by Abdullah Butt | AI & Python Developer"
)