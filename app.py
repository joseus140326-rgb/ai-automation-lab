import streamlit as st
import pandas as pd

st.title("USA Market Intelligence")

df = pd.read_csv("data/products.csv")

st.subheader("Products Dataset")

st.dataframe(df)

average_price = df["Price_USD"].mean()

st.metric("Average Product Price", f"${average_price:.2f}")

st.bar_chart(df.set_index("Product")["Price_USD"])