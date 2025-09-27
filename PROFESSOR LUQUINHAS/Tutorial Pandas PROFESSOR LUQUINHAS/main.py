import pandas as pd

df = pd.read_excel('Excel.xlsx')

# ordenado_por_nome = df.sort_values(by="NOME")
# ordenado_por_idade = df.sort_values(by="IDADE")
# ordenado_por_nota_desc = df.sort_values(by="NOTA", ascending=False)

# print("Ordenado por nome:")
# print(ordenado_por_nome)
# print("\nOrdenado por idade:")
# print(ordenado_por_idade)
# print("\nOrdenado por nota (decrescente):")
# print(ordenado_por_nota_desc)

# maiores_de_idade = df[df["IDADE"] >= 18]
# aprovados = df[df["NOTA"] >= 7]
# reprovados = df[df["NOTA"] < 7]

# maiores_de_idade_aprovados= df[(df["IDADE"]) >= 18 & (df["NOTA"] >= 7)]
# menores_de_idade_reprovados= df[(df["IDADE"]) < 18 & (df["NOTA"] < 7)]

# print("Maiores de idade:")
# print(maiores_de_idade)

# media_notas = df["NOTA"].mean()
# mediana = df["NOTA"].median()
# desvio_padrao = df["NOTA"].std()
# print(f"Média das notas: {media_notas}")
# print(f"Mediana das notas: {mediana}")
# print(f"Desvio padrão das notas: {desvio_padrao}")

# print(df)
# print(df.info())
# print(df.dtypes)
# print(df.describe())
# print(df["NOME"])
# print(df[["NOME", "IDADE"]])
# print(df.iloc[0])
# print(df.loc[0:3])

df["Aprovado" ] = df["NOTA"] >= 7
print(df)