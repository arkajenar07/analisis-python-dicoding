import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Dashboard Analisis Peminjaman Sepeda')

df = pd.read_csv('data_peminjaman.csv')

# Pertanyaan 1: Bagaimana pengaruh cuaca terhadap jumlah peminjaman sepeda dalam satu tahun?
st.subheader('☀️ Pengaruh Cuaca terhadap Peminjaman Sepeda')
st.markdown("""
Cuaca memiliki peran penting dalam jumlah peminjaman sepeda. Dari data yang dianalisis:

- **Saat cuaca cerah atau sedikit berawan, jumlah peminjaman meningkat secara signifikan.**
- **Peminjaman paling sedikit terjadi saat hujan deras, kemungkinan karena kondisi jalan yang basah dan kurang nyaman untuk bersepeda.**
""")

weather_mapping = {1: 'Cerah', 2: 'Berawan', 3: 'Hujan', 4: 'Hujan Deras'}
df['weathersit'] = df['weathersit'].map(weather_mapping)
weather_data = df.groupby('weathersit')['cnt'].mean().reset_index()
weather_data.rename(columns={'cnt': 'rata_peminjaman'}, inplace=True)

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x='weathersit', y='rata_peminjaman', data=weather_data, ci=None, ax=ax)
ax.set_xlabel('Cuaca')
ax.set_ylabel('Rata-rata Jumlah Peminjaman')
ax.set_title('Peminjaman Sepeda Berdasarkan Cuaca')
st.pyplot(fig)

# Pertanyaan 2: Bagaimana pola peminjaman sepeda berdasarkan musim dalam satu tahun?
st.subheader('🌤️ Pola Peminjaman Sepeda Berdasarkan Musim')
st.markdown("""
Musim juga memengaruhi jumlah peminjaman sepeda. Berdasarkan pola yang diamati:

- **Peminjaman sepeda paling banyak terjadi di Musim Gugur, kemungkinan karena cuaca yang lebih nyaman dan aktivitas luar ruangan meningkat.**
- **Musim Semi memiliki tingkat peminjaman yang paling rendah, kemungkinan karena cuaca yang masih tidak menentu dan kurangnya liburan panjang.**
- **Musim Panas dan Musim Dingin memiliki tingkat peminjaman yang cukup tinggi tetapi masih lebih rendah dibandingkan Musim Gugur.**
""")

season_mapping = {1: 'Musim Semi', 2: 'Musim Panas', 3: 'Musim Gugur', 4: 'Musim Dingin'}
df['season'] = df['season'].map(season_mapping)
rental_data = df.groupby('season')['cnt'].mean().reset_index()
rental_data.rename(columns={'cnt': 'rata_peminjaman'}, inplace=True)

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x='season', y='rata_peminjaman', data=rental_data, ci=None, ax=ax)
ax.set_xlabel('Musim')
ax.set_ylabel('Rata-rata Jumlah Peminjaman')
ax.set_title('Peminjaman Sepeda Berdasarkan Musim')
st.pyplot(fig)

# Filter Musim dan Tahun
st.subheader('📅 Filter Data Berdasarkan Musim dan Tahun')
season_options = df['season'].unique()
selected_season = st.selectbox('Pilih Musim', season_options)
years = df['yr'].unique()
selected_year = st.selectbox('Pilih Tahun', years)

df_filtered = df[(df['season'] == selected_season) & (df['yr'] == selected_year)]
# Visualisasi Peminjaman Sepeda Berdasarkan Cuaca
st.subheader('☀️ Pola Peminjaman Sepeda Berdasarkan Cuaca')
weather_data = df_filtered.groupby('weathersit')['cnt'].mean().reset_index()
weather_data.rename(columns={'cnt': 'rata_peminjaman'}, inplace=True)

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x='weathersit', y='rata_peminjaman', data=weather_data, ci=None, ax=ax)
ax.set_xlabel('Cuaca')
ax.set_ylabel('Rata-rata Peminjaman')
ax.set_title(f'Peminjaman Sepeda Berdasarkan Cuaca di Musim {selected_season} Tahun {selected_year}')
st.pyplot(fig)