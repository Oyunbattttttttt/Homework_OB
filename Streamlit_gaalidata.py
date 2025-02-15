import streamlit as st # pip install streamlit, streamlit run 1_Loan.py
import plotly.express as px
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')
import datetime as dt

st.set_page_config(page_title="Gaalidata!!!", page_icon="📊",layout="wide")

st.title("📊 Gaali analysis")
st.markdown('<style>div.block-container{padding-top:2rem;}</style>',unsafe_allow_html=True)

file_path = 'output_file.xlsx'
if not os.path.exists(file_path):
    st.error(f"Error: '{file_path}' not found. Please upload the file.")
else:
    # Read the Excel file
    df = pd.read_excel(file_path)

df["date_column"] = pd.to_datetime(df["date_column"])

df = df.rename(columns={"Тээврийн төрөл_01": "transport_type"})
df_out = df.groupby(["date_column", "transport_type"])['Len_1'].count().reset_index()


# outstanding loan monthly
fig = px.line(df_out, x="date_column", y="Len_1",color="transport_type",
                 title="Outstanding amount")

st.plotly_chart(fig, use_container_width=True)

start_date = '2024-01-01'
end_date = '2024-03-01'

df_out_filtered = df_out[(df_out['date_column'] >= start_date) & (df_out['date_column'] <= end_date)]

## Convert 'month' to a datetime format for better compatibility with Plotly
df_out['month'] = df_out['date_column'].dt.to_period('M').dt.to_timestamp()

# Now, group by the new 'month' column (which is in datetime format)
df_out_month = df_out.groupby(['month',"transport_type"])['Len_1'].sum().reset_index()

# Create the bar plot
fig = px.bar(df_out_month, x="month", y="Len_1",color="transport_type", title="Monthly Transport Type Counts")

# Display the plot
st.plotly_chart(fig, use_container_width=True)
st.dataframe(df_out)
