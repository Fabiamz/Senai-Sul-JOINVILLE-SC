import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/lukas-senai/pandas-tutorial/refs/heads/main/assets/alunos-30.csv")

media_geral = df["Nota"].mean()
print(f"Média geral das notas: {media_geral}")

menor_que_7 = df[df["Nota"] < 7].__len__()
print("Alunos com nota menor que 7:")
print(menor_que_7)  