df = pd.read_csv("https://github.com/Otto0222/ejercicio/blob/main/Credit.csv")
df.drop(columns=["Unnamed: 0"], inplace=True)
# Ver información general del dataset
df.info()
plt.figure(figsize=(8, 5))
fig1 = sns.histplot(df["Balance"], bins=30, kde=True, color='blue')
plt.title("Distribución de la Variable Balance")
plt.xlabel("Balance")
plt.ylabel("Frecuencia")
plt.show()

#Display plot 1
st.plotly_chart(fig1, use_container_width=True)

plt.figure(figsize=(10, 6))
fig2 = sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Matriz de Correlación entre Variables Numéricas")
plt.show()
 
st.plotly_chart(fig2, use_container_width=True)
