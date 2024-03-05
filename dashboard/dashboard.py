import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Mengatur tema seaborn untuk plot
sns.set_theme(style="whitegrid")

# Membaca data
df = pd.read_csv('main_data.csv')

# Aplikasi Streamlit
st.title('Analisis Penggunaan Sepeda')
st.write(
    "Selamat datang di Dashboard Rental Sepeda! 🌟 Nikmati petualangan analisis kami yang mengungkapkan tren menarik seputar penggunaan sepeda dari waktu ke waktu. Dengan grafik yang menarik dan statistik yang informatif, Anda akan mendapatkan wawasan mendalam tentang bagaimana sepeda dipinjamkan. Mari kita mulai petualangan kita! 🚲🔍"
)
st.sidebar.header('Pengaturan Visualisasi')

# Pilihan bulan
bulan_options = ['All'] + list(df['month'].unique())
bulan = st.sidebar.selectbox('Pilih Bulan', bulan_options)

# Filter data berdasarkan bulan yang dipilih
if bulan == 'All':
    df_selected_month = df
else:
    df_selected_month = df[df['month'] == bulan]

# Tren penggunaan sepeda pada akhir pekan vs. hari kerja
st.header('Tren Penggunaan Sepeda pada Akhir Pekan vs. Hari Kerja')
weekend_mean = df_selected_month[df_selected_month['weekday'].isin(['Saturday', 'Sunday'])]['total_count'].mean()
weekday_mean = df_selected_month[~df_selected_month['weekday'].isin(['Saturday', 'Sunday'])]['total_count'].mean()
st.write(f"Rata-rata penggunaan sepeda pada akhir pekan{' di semua bulan' if bulan == 'All' else f' di bulan {bulan}'}: **{weekend_mean:.2f}**")
st.write(f"Rata-rata penggunaan sepeda pada hari kerja{' di semua bulan' if bulan == 'All' else f' di bulan {bulan}'}: **{weekday_mean:.2f}**")

# Plot tren penggunaan sepeda pada akhir pekan vs. hari kerja
fig, ax = plt.subplots()
ax.bar(['Hari kerja', 'Akhir peka'], [weekend_mean, weekday_mean], color=['blue', 'green'])
ax.set_xlabel('Jenis Hari')
ax.set_ylabel('Rata-rata jumlah semua pengguna')
ax.set_title('Rata-rata penggunaan sepeda pada akhir pekan vs Hari Kerja')
st.pyplot(fig)

# Perbedaan penggunaan sepeda antara musim
st.header('Perbedaan Penggunaan Sepeda antara Musim')
season_counts = df_selected_month.groupby('season')['total_count'].mean()
st.bar_chart(season_counts)

# Pengaruh kondisi cuaca terhadap jumlah pengguna sepeda terdaftar dan casual
st.header('Pengaruh Kondisi Cuaca terhadap Penggunaan Sepeda')
weather_counts = df_selected_month.groupby('weather')[['registered', 'casual']].mean()
st.bar_chart(weather_counts)

# Menambahkan footer
st.sidebar.markdown('---')
st.sidebar.markdown('Dibuat oleh Muammar Faridz Dimyati')
