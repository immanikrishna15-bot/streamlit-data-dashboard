# streamlit-data-dashboard

A modular Streamlit web app for data analysis. Upload CSV/Excel, clean data, view KPIs, detect anomalies, filter interactively, visualize trends, and download processed data. Perfect for business, education, and general data exploration.

## Features

- Upload CSV or Excel datasets (e.g. sales, students, weather)
- Automated data cleaning (removes missing values)
- KPI summary and basic statistics
- Outlier/anomaly detection using IQR method
- Interactive data filtering via sidebar
- Trend visualization with Plotly
- Download cleaned and filtered data as CSV
- User-friendly Streamlit interface

## How to Run

1. **Clone the repo**  
   `git clone https://github.com/your-username/streamlit-data-dashboard.git`
2. **Install dependencies**  
   `pip install -r requirements.txt`
3. **Run the app**  
   `streamlit run dashboard.py`
4. **Upload a sample data file** from the `sample_data` folder or your own.

## Example Data

Place your CSV or Excel files in the `sample_data/` folder.  
Sample files like `sales.csv` and `students.csv` provided.

## License

MIT License