import pandas as pd
import matplotlib.pyplot as plt  # Importando matplotlib.pyplot

uri = 'https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula4.1/ratings.csv'
notas = pd.read_csv(uri)
notas.columns = ["usuarioId", "filmesId", "nota", "momento"]
primeirasNotas = notas["nota"].head()
print(primeirasNotas)
print(primeirasNotas.unique())
print(primeirasNotas.mean()) # pega a media dos valores
print(primeirasNotas.min()) # pega o menor valor
print(notas.describe()) # descreve o dataframe
print(notas.nota.plot(kind="hist"))

plt.show()  # Mostrando o histograma
