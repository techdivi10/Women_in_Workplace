import streamlit as st
import pandas as pd
import plotly.express as px
import urllib.request
from urllib.error import HTTPError

# Function to download CSV files from URLs with error handling
def download_csv(url):
    try:
        print(f"Downloading data from: {url}")
        response = urllib.request.urlopen(url)
        data = response.read()
        with open('temp.csv', 'wb') as f:
            f.write(data)
        return pd.read_csv('temp.csv')
    except HTTPError as e:
        st.error(f"HTTP Error: {e.code} - {e.reason}")
        return None
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None


gender_parity_higher_edu_url = 'https://data.gov.in/download/622254834dd38be9e781cc59135f9911'
gender_parity_primary_edu_url = 'https://data.gov.in/download/cd0312fb4c95219c34c5baf2b9c6daa1'
employment_exchanges_edu_url = 'https://data.gov.in/catalog/employment-exchanges-data'
average_daily_wage_edu_url = 'https://data.gov.in/catalog/average-daily-wage-rate-rural-india'
employment_public_private_edu_url= 'https://data.gov.in/catalog/employment-public-sector-and-private-sector'
disabled_population_private_edu_url= 'https://data.gov.in/catalog/disabled-population-among-main-workers-marginal-workers-non-workers-type-disability-age-0'
labour_force_participation_edu_url= 'https://data.gov.in/catalog/labour-force-participation-rate-work-force-participation-rate-and-unemployment-rate'
worker_population_ratio_edu_url= 'https://data.gov.in/catalog/worker-population-ratio-1000-persons-age-15-59-years'
employment_unemployment_edu_url= 'https://data.gov.in/catalog/employment-and-unemployment-national-sample-survey'


def main():
    st.title('Women in Workplace Insights - India')

    
    st.sidebar.header('Select Dataset')
    selected_dataset = st.sidebar.selectbox('Choose a dataset', ['Gender Parity Higher Education', 'Gender Parity Primary Education',
                                                                 'Employment Exchanges', 'Average Daily Wage',
                                                                 'Employment in Public and Private Sector',
                                                                 'Disabled Population', 'Labour Force Participation',
                                                                 'Worker Population Ratio', 'Employment and Unemployment'])

    # Display insights based on selected dataset
    st.subheader(f'{selected_dataset} Data')
    df = None

    if selected_dataset == 'Gender Parity Higher Education':
        df = download_csv(gender_parity_higher_edu_url)
    elif selected_dataset == 'Gender Parity Primary Education':
        df = download_csv(gender_parity_primary_edu_url)
    elif selected_dataset == 'Gender Parity Index':
        df = download_csv(gender_parity_index_edu_url)
    elif selected_dataset == 'Employment Exchanges Data':
        df = download_csv(employment_exchanges_edu_url)

    if df is not None:
        st.write("Loaded Data:")
        st.write(df.head())

        # Additional insights or visualizations
        st.subheader('Insights')
        st.write(f"Number of rows: {df.shape[0]}")
        st.write(f"Number of columns: {df.shape[1]}")
        st.write(f"Summary statistics:\n{df.describe()}")

        # Example: Plotting a bar chart using Plotly Express
        st.subheader('Example Visualization')
        fig = px.bar(df, x='Year', y='Value', title='Sample Chart')
        st.plotly_chart(fig)

if __name__ == "__main__":
    main()
