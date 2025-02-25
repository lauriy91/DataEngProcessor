import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"

st.title("Sales Dashboard")

# Obtain sales by product
st.header("Sales by Product")
product = st.text_input("Filter by product (optional)")
category = st.text_input("Filter by category (optional)")

params = {}
if product:
    params["product"] = product
if category:
    params["category"] = category

response = requests.get(f"{API_URL}/sales/product", params=params)
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    st.dataframe(df)
else:
    st.error("Error")

# Obtain sales per day
st.header("Sales per day")
start_date = st.date_input("Start Date", value=pd.to_datetime("2024-01-01"))
end_date = st.date_input("End Date", value=pd.to_datetime("2024-12-31"))

response = requests.get(
    f"{API_URL}/sales/day", params={"start_date": start_date, "end_date": end_date}
)
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    st.line_chart(df.set_index("date"))
else:
    st.error("Error")

# Obtain sales by category
st.header("Sales by Category")

response = requests.get(f"{API_URL}/sales/category")
if response.status_code == 200:
    df_category = pd.DataFrame(response.json())
    st.bar_chart(df_category.set_index("day_with_highest_sales"))
else:
    st.error("Error")

# Obtain sales by outliers
st.header("Outliers in Sales")

response = requests.get(f"{API_URL}/sales/outliers")
if response.status_code == 200:
    df_outliers = pd.DataFrame(response.json())
    st.line_chart(df_outliers.set_index("quantity"))
    st.dataframe(df_outliers)
else:
    st.error("Error")
