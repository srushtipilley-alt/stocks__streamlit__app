import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Set Streamlit page config
st.set_page_config(page_title="Nifty Stock Viewer", layout="wide")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('Nifty_Stocks.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    return df

df = load_data()

# Sidebar for inputs
st.sidebar.title("Stock Filter")

category_options = df['Category'].unique()
selected_category = st.sidebar.selectbox("Select Category", category_options)

filtered_df = df[df['Category'] == selected_category]
symbol_options = filtered_df['Symbol'].unique()
selected_symbol = st.sidebar.selectbox("Select Symbol", symbol_options)

# Filter based on selection
stock_data = filtered_df[filtered_df['Symbol'] == selected_symbol]

# Title
st.title(f"{selected_symbol} Stock Price Trend")
st.markdown(f"Category: **{selected_category}**")

# Plotting
fig, ax = plt.subplots(figsize=(15, 8))
sb.lineplot(data=stock_data, x='Date', y='Close', ax=ax)
ax.set_title(f"{selected_symbol} Closing Price Over Time", fontsize=16)
ax.set_xlabel("Date")
ax.set_ylabel("Close Price")

st.pyplot(fig)
