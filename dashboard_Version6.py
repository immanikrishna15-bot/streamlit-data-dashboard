import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Function to load data from uploaded file (CSV or Excel)
def load_data(uploaded_file):
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    return df

# Function to clean data by dropping rows with missing values
def clean_data(df):
    df = df.dropna()
    return df

# Function to display basic KPIs and summary statistics
def show_kpis(df):
    st.subheader("Basic KPIs")
    st.write(f"Rows: {df.shape[0]}")
    st.write(f"Columns: {df.shape[1]}")
    if df.select_dtypes(include=[np.number]).shape[1] > 0:
        st.write("Numerical Column Summary:")
        st.write(df.describe())

# Function to detect anomalies using the IQR method for numerical columns
def detect_anomalies(df):
    st.subheader("Anomaly Detection (basic outlier check)")
    num_cols = df.select_dtypes(include=[np.number]).columns
    for col in num_cols:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        outliers = df[(df[col] < (q1 - 1.5 * iqr)) | (df[col] > (q3 + 1.5 * iqr))]
        st.write(f"{col}: {len(outliers)} outliers")

# Function for line plot visualization on a selected numerical column
def plot_data(df):
    num_cols = df.select_dtypes(include=[np.number]).columns
    if len(num_cols) >= 1:
        st.subheader("Trend Visualization")
        col = st.selectbox("Select column for trend plot", num_cols)
        fig = px.line(df, y=col)
        st.plotly_chart(fig)
    else:
        st.write("No numerical columns available for plotting.")

# Sidebar filtering tool: filter rows by selected columns and values
def filter_data(df):
    st.sidebar.header("Filter Data")
    filter_cols = st.sidebar.multiselect("Select columns to filter", df.columns.tolist())
    filtered_df = df.copy()
    for col in filter_cols:
        unique_vals = df[col].unique()
        selected_vals = st.sidebar.multiselect(f"Filter {col}", unique_vals, default=list(unique_vals))
        filtered_df = filtered_df[filtered_df[col].isin(selected_vals)]
    return filtered_df

# Prepare CSV download from dataframe
def download_csv(df):
    return df.to_csv(index=False).encode('utf-8')

# Main app interface
st.title("Modular Data Dashboard")
st.write("Upload a CSV or Excel file to analyze your data:")

uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])
if uploaded_file:
    # Load and preview raw data
    df = load_data(uploaded_file)
    st.write("Raw Data Preview:")
    st.dataframe(df.head())
    # Clean data (remove missing values)
    df_clean = clean_data(df)
    # Filter data using sidebar controls
    df_filtered = filter_data(df_clean)
    st.write("Filtered Data Preview:")
    st.dataframe(df_filtered.head())
    # Display KPIs
    show_kpis(df_filtered)
    # Detect anomalies
    detect_anomalies(df_filtered)
    # Plot numerical data
    plot_data(df_filtered)
    # Download button for filtered data
    st.subheader("Download Filtered Data")
    st.download_button(
        label="Download CSV",
        data=download_csv(df_filtered),
        file_name="filtered_data.csv",
        mime="text/csv"
    )