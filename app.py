import streamlit as st
from data_processing import load_data
from eda import perform_eda
from hypothesis_testing import perform_hypothesis_testing

# Load the dataset
df = load_data()

# Set the page layout to wide
st.set_page_config(layout="wide")

# Title of the app
st.title("Customer Behavior and Segmentation Analysis")

# Sidebar for navigation
st.sidebar.title("Navigation")
option = st.sidebar.radio("Choose a page", ["Dashboard", "Hypothesis Testing"])

if option == "Dashboard":
    perform_eda(df)
elif option == "Hypothesis Testing":
    st.header("Hypothesis Testing Results")
    st.write("View the results of hypothesis testing for various metrics.")
    perform_hypothesis_testing(df)
