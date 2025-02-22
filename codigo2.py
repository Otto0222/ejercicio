# Example 3
import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv("Credit.csv")
df.drop(columns=["Unnamed: 0"], inplace=True)

#Título
st.title("📊 Ejercicio grupo 1")

# Ver información general del dataset
fig1 = px.histogram(df, x="Balance", title="Distribución de la Variable Balance")
fig1.show()

#Display plot 1
st.plotly_chart(fig1)

fig2 = px.imshow(df.corr(numeric_only=True), title="Matriz de Correlación entre Variables Numéricas")

fig2.show()
st.plotly_chart(fig2)
