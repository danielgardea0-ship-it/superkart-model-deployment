
import streamlit as st
import pandas as pd
import requests 
import os

# Flsak API address inside Docker network
API_URL = os.getenv(
    "API_URL",
    "http://backend:7860/v1/predict"
)

# Application title
st.title("SuperKart Sales Prediction")

st.write("Enter product and store information to predict sales.")

# Collect product information
product_weight = st.number_input(
    "Product Weight",
    min_value=0.0,
    value=12.65
)

product_sugar_content = st.selectbox(
    "Product Sugar Content",
    options=["Low Sugar", "Medium Sugar", "High Sugar"]

allocated_area = st.number_input(
    "Product Allocated Area",
    min_value=0.0,
    value=0.027
)

store_size = st.selectbox(
    "Store Size",
    options=["Small", "Medium", "Large"]
)

city_type = st.selectbox(
    "Store Location City Type",
    options=["Tier 1", "Tier 2", "Tier 3"]
)

store_type = st.selectbox(
    "Store Type",
    options=["Supermarket Type1", "Supermarket Type2", "Departmental Store, "Food Mart"]
)

product_id = st.text_input("Product ID Characters", "FD")

store_age = st.number_input()
    "Store Age (Years)", mi_value=0, value=16
)

product_category = st.text_input(
    "Product Type Category", "Non Perishables"
)

#Generate sales prediction
if st.button("Predict Sales"):
  payload = {
      "Product_Weight": product_weight,
      "Product_Sugar_Content": product_sugar_content,
      "Product_Allocated_Area": allocated_area,
      "Product_MRP": product_mrp,
      "Store_Size": store_size,
      "Store_Location_City_Type": city_type,
      "Store_Type": store_type,
      "Product_Id_Category": product_category
      "Store_Age_Years": store_age
      "Product_Type_Category": product_category
  }

  try:
    response = requests.post(
        API_URL, json=payload, timeout=30
    )
    response.raise_for_status()

    result =. response.json()
  
    st.success(
        f"Predicted Sales: ${prediction:.2f}"
        )
    except Exception as e:
      st.error(f"Prediction failed:{e}")
