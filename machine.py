from sklearn.svm import LinearSVC

# # pelos longos, perna curta, faz auau
# porco1 = [0, 1, 0]
# porco2 = [0, 1, 1]
# porco3 = [1, 1, 0]

# cachorro1 = [0, 1, 1]
# cachorro2 = [1, 0, 1]
# cachorro3 = [1, 1, 1]

# treino_x = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]
# treino_y = [1, 1, 1, 0, 0, 0]  # 0 para cachorro, 1 para porco

# modelo = LinearSVC()
# modelo.fit(treino_x, treino_y)
# print(modelo)

# animal_misterioso = [1,1,1]
# modelo.predict([animal_misterioso])

# misterio1 = [1,1,1]
# misterio2 = [1,1,0]
# misterio3 = [0,1,1]

# teste_x = [misterio1, misterio2, misterio3]
# teste_y = [0,1,1]

# previsoes = modelo.predict(teste_x)
# print(previsoes)

# from sklearn.metrics import accuracy_score

# print(accuracy_score(teste_y, previsoes))

import pandas as pd

uri = 'https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula4.1/ratings.csv'
dados = pd.read_csv(uri)
# print(dados.head())
print(dados.sample(5))
x = dados[["userId", "movieId", "rating"]]
print(x.head())
y = dados["timestamp"]
print(y.head())

modelo = LinearSVC() 
modelo.fit(x, y)
print(modelo)