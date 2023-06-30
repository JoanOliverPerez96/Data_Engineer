import seaborn as sns
import pandas as pd
import streamlit as st
import plotly.express as px

# Load Dataset
df = sns.load_dataset('penguins')

# Page Title
st.title('Ejemplo de uso de st.write()')

# Text + emoji
st.write('Hola :sunglasses: :heart: ')

# Calculations
st.write(1+1)

# Variables
a = 2**2
st.write(a)

# Table
st.write(df.head(5))

# Multiple
st.write('st.write("text", df)', df.head(7))

#Plot
st.plotly_chart(px.scatter(df, x='bill_length_mm', y='bill_depth_mm'))