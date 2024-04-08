nome = "Phillipe"
print(nome)

idade = 19
print(idade)

def mais_um_ano(idade): 
    return idade + 1 

idade = mais_um_ano(idade)  # Atualizando o valor de idade com o resultado da função
print(idade)

filme1 = "MATRIX 1"
filme2 = "A xuxa de baixo astral"
filme3 = "Toy Store 10"

filmes = [filme1, filme2, filme3]
# print(filmes)

def listaDeFilmes(mostrar_filmes):
    print("Os filmes disniveis são:")
    print(mostrar_filmes)


listaDeFilmes(filmes)

print(filmes[0],filmes[1],filmes[2])

print(filmes[-1]) # -1 pega o ultimo elemento da lista.
print(filmes[-2]) # -2 pega o penultima e assim vai.
print(filmes[1:]) # ignora o elemento "0" e pega somente do "1" até a ultima posição
print(filmes[-2:]) # pega a partida do penultimo até o ultimo

for filme in filmes:
    print(filmes)
    print("...")
print("fora do escopo")

dados =  {"nome": "Phillipe", "idade": 19, "situação" : "procurando job"}

print(dados["nome"])
