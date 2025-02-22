df = pd.read_csv("https://github.com/Otto0222/ejercicio/blob/main/Credit.csv")
df.drop(columns=["Unnamed: 0"], inplace=True)
# Ver información general del dataset
fig1 = px.histogram(df, x="Balance", title="Distribución de la Variable Balance")
fig1.show()

#Display plot 1
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.imshow(df.corr(numeric_only=True), title="Matriz de Correlación entre Variables Numéricas")

fig2.show()
st.plotly_chart(fig2, use_container_width=True)
