# O  programa serve para organizar a lista na ordem numerica
lista = [11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8] # sao  os termos 

print("lista original", lista)
N = 20 # numero de termos 

import matplotlib.pyplot as plt
plt.figure ()
plt.plot(range(0, N, 1), lista,'ok') 
plt.title("Original")
plt.xlabel("posicao")
plt.ylabel("valores")
plt.savefig("fig/bubble-inicio.png")

# i e j sao os elementos posicionados
# o range para a letra i e o intervalo entre a primeira posicao (0), e a ultima (N-1),
# em relacao a j, o primeiro termo foi indicado como "for i", por isso comecamos com o comando i+j
# o comando "for" tem a funcao de verificar se lista[i] > lista[j];

for i in range(0, N, 1): # possiveis valores de i
    for j in range(i+1, N, 1): # possiveis valores de j
        if lista[i] > lista[j]: # sendo i > j
            temp = lista[i] # quando j > i, troca 
            lista[i] = lista[j]
            lista[j] = temp

# se lista[i] > lista[j], cria-se a variavel temp para todo i > j

print("lista crescente") # mostrou os valores em ordem crescente

print("lista dos 5 maiores", lista[15:21:1]) # mostrou os 5 maiores valores
print("lista dos 5 menores", lista[0:5:1]) # mostrou os 5 menores valores

# Tarefa 2

import matplotlib.pyplot as plt
plt.figure ()
plt.plot(range(0, N, 1), lista,'ok') 
plt.title("Crescente")
plt.xlabel("posicao")
plt.ylabel("valores")
plt.savefig("fig/bubble-fim.png")
