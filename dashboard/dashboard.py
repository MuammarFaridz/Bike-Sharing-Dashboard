import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('main_data.csv')

# Aplikasi Streamlit
st.title('Analisis Penggunaan Sepeda')

# Tren penggunaan sepeda pada akhir pekan vs. hari kerja
st.header('Tren Penggunaan Sepeda pada Akhir Pekan vs. Hari Kerja')
weekend_mean = df[df['weekday'].isin(['Saturday', 'Sunday'])]['total_count'].mean()
weekday_mean = df[~df['weekday'].isin(['Saturday', 'Sunday'])]['total_count'].mean()
st.write(f"Rata-rata penggunaan sepeda pada akhir pekan: {weekend_mean}")
st.write(f"Rata-rata penggunaan sepeda pada hari kerja: {weekday_mean}")

# Perbedaan penggunaan sepeda antara musim
st.header('Perbedaan Penggunaan Sepeda antara Musim')
season_counts = df.groupby('season')['total_count'].mean()
st.bar_chart(season_counts)

# Pengaruh kondisi cuaca terhadap jumlah pengguna sepeda terdaftar dan casual
st.header('Pengaruh Kondisi Cuaca terhadap Penggunaan Sepeda')
weather_counts = df.groupby('weather')[['registered', 'casual']].mean()
st.bar_chart(weather_counts)

# Tampilkan data
st.subheader('Data Penggunaan Sepeda')
st.write(df)
