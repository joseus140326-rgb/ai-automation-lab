import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="USA Market Intelligence",
    page_icon="📊",
    layout="wide"
)

st.title("USA Market Intelligence")
st.write("Dashboard for product price analysis in the USA market.")

df = pd.read_csv("data/products.csv")

min_price = float(df["Price_USD"].min())
max_price = float(df["Price_USD"].max())

selected_range = st.slider(
    "Filter by price range",
    min_value=min_price,
    max_value=max_price,
    value=(min_price, max_price)
)

filtered_df = df[
    (df["Price_USD"] >= selected_range[0]) &
    (df["Price_USD"] <= selected_range[1])
]

col1, col2, col3 = st.columns(3)

col1.metric("Total Products", len(filtered_df))
col2.metric("Average Price", f"${filtered_df['Price_USD'].mean():.2f}")
col3.metric("Max Price", f"${filtered_df['Price_USD'].max():.2f}")

st.subheader("Filtered Products")
st.dataframe(filtered_df, use_container_width=True)

st.subheader("Price Chart")
st.bar_chart(filtered_df.set_index("Product")["Price_USD"])

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download filtered CSV",
    data=csv,
    file_name="filtered_products.csv",
    mime="text/csv"
)