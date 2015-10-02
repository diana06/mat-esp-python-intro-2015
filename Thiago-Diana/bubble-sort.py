# O  programa serve para organizar a lista na ordem numerica
lista = [11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8] # essa e a lista com os termos fora de ordem

print("lista original", lista) #imprimir a lista fora de ordem
N = 20 # variavel com o numero de termos na lista
T = 0 # variavel que sera utilizada para realizar a troca dos termos
count_troca = 0 # contador para as figuras de acordo com a ocorrencia das trocas
count_it 0 # contador para as figuras de acordo com a ocorrencia das interacoes

import matplotlib.pyplot as plt #importar o módulo matplotlib

plt.figure() #criar figura em branco
plt.plot(range(0, N, 1), lista,'ok') #preencher com os dados primarios
plt.title("Original") #dar nome ao titulo
plt.xlabel("Posição") #nomear o eixo x
plt.ylabel("Valor") #nomear o eixo y
plt.savefig("fig/bubble-inicio.png") #salvar figura na pasta fig
plt.close #fechar figura

# i e j sao os elementos posicionados
# o range para a letra i e o intervalo entre a primeira posicao (0), e a ultima (N-1),
# em relacao a j, o primeiro termo foi indicado como "for i", por isso comecamos com o comando i+j

for i in range(0, N, 1): #o programa vai rodar todos os valores
    for j in range(i+1, N, 1): #o programa vai rodar todos os valores menos o ultimo

        plt.figure() #criar figura em branco
        plt.plot(range(0, N, 1), lista,'ok') #preencher com os dados primarios
        plt.plot(i, lista[i],'or') #preencher com os dados primarios
        plt.plot(j, lista[j],'ob') #preencher com os dados primarios
        count_it = count_it+1 #aumentar o contador da interacao
        plt.title("Interação {}".format(count_it)) #dar nome ao titulo
        plt.xlabel("Posição") #nomear o eixo x
        plt.ylabel("Valor") #nomear o eixo y
        plt.savefig("fig/bubble-it-{}.png".format(count_it)) #salvar figura na pasta fig
        plt.close #fechar figura

        if lista[i] > lista[j]: # cada termo e comparado com o termo a seguir e, caso seja maior, o comando é executado
            T = lista[i] # a troca comecou
            lista[i] = lista[j] # durante a troca
            lista[j] = T # a troca finalizou
            
            plt.figure() #criar figura em branco
            plt.plot(range(0, N, 1), lista,'ok') #preencher com os dados primarios
            count_troca = count_troca+1 #aumentar o contador da troca
            plt.title("Troca {}".format(count_troca)) #dar nome ao titulo
            plt.xlabel("Posição") #nomear o eixo x
            plt.ylabel("Valor") #nomear o eixo y
            plt.savefig("fig/bubble-troca-{}.png".format(count_troca)) #salvar figura na pasta fig
            plt.close #fechar figura


print("lista crescente") # mostrou os valores em ordem crescente

plt.figure() #criar figura em branco
plt.plot(range(0, N, 1), lista,'ok') #preencher com os dados primarios
plt.title("Crescente") #dar nome ao titulo
plt.xlabel("Posição") #nomear o eixo x
plt.ylabel("Valor") #nomear o eixo y
plt.savefig("fig/bubble-inicio.png") #salvar figura na pasta fig
plt.close #fechar figura

print("Lista dos 5 maiores valores", lista[15:21:1]) # mostrou os 5 maiores valores
print("Lista dos 5 menores valores", lista[0:5:1]) # mostrou os 5 menores valores
