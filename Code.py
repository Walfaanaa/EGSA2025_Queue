import streamlit as st
import pandas as pd

st.title("EGSA Queue Payment Lookup")

# GitHub raw URL of your Excel file
url = "https://github.com/Walfaanaa/EGSA2025_Queue/raw/main/members_data.xlsx"

# Read Excel file directly from GitHub
df = pd.read_excel(url)

# Queue calculation
df['queue'] = range(1, len(df)+1)
N = len(df)

df['Total money for winners'] = df['Amount_per_month'] * N
df['percent_rate'] = (N - df['queue'] + 1) / 100
df['uqub_deduction'] = df['Total money for winners'] * df['percent_rate']
df['service_charge'] = df['Total money for winners'] * 0.005
df['total_payment_after'] = df['Total money for winners'] - df['uqub_deduction'] - df['service_charge']
df['final_money'] = df['service_charge'] + df['total_payment_after']

# Select queue number
queue_number = st.number_input("Select Queue Number", min_value=1, max_value=N, step=1)

# Show final payment for selected queue
selected_row = df[df['queue'] == queue_number]
final_payment = selected_row['final_money'].values[0]

st.write(f"💰 Final Payment for Queue {queue_number}: **{final_payment:,.2f} ETB**")
