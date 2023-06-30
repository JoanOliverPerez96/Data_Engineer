import seaborn as sns
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

# Set Page Layout
st.set_page_config(layout='wide')
# Set Page Layout

uploaded_file = st.file_uploader('Sube tus deseos', type=['csv'])

if uploaded_file is not None:
    # Procesar el archivo CSV aquí
    st.balloons()

df = pd.read_csv('Streamlit/Practica/Data/red_recarga_2021.csv')

# Colocamos nuestro titulo
st.title('Localiza tu puerto :electric_plug:')

# Cover de nuestra página
st.image("Streamlit/Practica/img/cover.jpg",width=1000) 