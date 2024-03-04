import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

def create_bycity_df(df):
    bycity_top10_df = df.groupby(by="customer_city").customer_id.nunique().reset_index()
    bycity_top10_df.rename(columns={
        "customer_id": "customer_count"
    }, inplace=True)
    
    return bycity_top10_df

def create_payment_df(df):
    payment_df = df.groupby(by="payment_type").customer_id.nunique().reset_index()
    payment_df.rename(columns={
        "customer_id": "payment_count"
    }, inplace=True)
    
    return payment_df

all_df = pd.read_csv("dashboard/all_data.csv")

bycity_top10_df = create_bycity_df(all_df)
payment_df = create_payment_df(all_df)

st.header('Dashboard My project  E-commerce:star: :star: :star:')

st.subheader("Most customers by city")

bycity_top10_sorted = bycity_top10_df.sort_values(by='customer_count', ascending=False)

# Mengambil 10 baris pertama DataFrame yang sudah diurutkan
bycity_top10_sorted = bycity_top10_sorted.head(10)
# Menampilkan visualisasi di Streamlit
st.bar_chart(bycity_top10_sorted.set_index('customer_city'))


st.subheader("most payment methods used by customers")
payment_top = payment_df.sort_values(by='payment_count',ascending=False)

payment_top = payment_top
st.bar_chart(payment_top.set_index('payment_type'))








