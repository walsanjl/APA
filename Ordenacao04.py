#--- ALUNO - WALSAN JADSON ---

#------- IMPORTANDO BIBLIOTECAS -------
import sys
import timeit

#------- DEFININDO FUNCOES -------
#-- 1
def pai(lista, i):
	return lista[(i-1)/2]

def filhoDireita(lista, i):
	return lista[(i*2+1)]

def filhoEsquerda(lista, i):
    return lista[(i*2)]

def menorElemento(lista):
    return lista[1]

def ehHeapMax(lista):
    for i in range(2, len(lista)):
        if(lista[i] < lista[i//2]):
            return false
    return true

def insereHeapMax(lista, indiceFinal):
    i = indiceFinal
    while (True):
        # chegou na raiz
        if i == 1:
            break
        # verifica posicao
        pai = i // 2
        if lista[pai] >= lista[i]:
            break

        # troca com o pai
        aux = lista[pai]
        lista[pai] = lista[i]
        lista[i] = aux

        i = pai

def removeHeapMax(lista, n):
	i = 1
	while True:
		c = 2 * i
		# se o elemento nao possui mais filhos
		if c > n:
			break

		# verifica maior dos filhos.
		if c + 1 <= n:
			if lista[c + 1] > lista[c]:
				c += 1

		# para se o elemento for maior que seu filho
		if lista[i] >= lista[c]:
			break
		# Troca com maior filho.
		#aux = lista[c]
		#lista[c] = lista[i]
		#lista[i] = aux
		lista[c], lista[i] = lista[i], lista[c]
		i = c

#1--
def heapSort(lista, n):
	#construcao do heap.
	for i in range(2, n):
		insereHeapMax(lista, i)

	#construcao do vetor ordenado
	for i in range(n, 1, -1):
		#lista[1], lista[i] = lista[i], lista[1]
		#aux = lista[i]
		#lista[i] = lista[1]
		#lista[1] = aux
		
		removeHeapMax(lista, i - 1)

#------- ENTRADA -------
'''
Exemplo de chamada a ser executada pelo terminal pra ser
proccessada com o metodo 1 (countingSort) :
>python Ordenacao01.py 2
7 #tamanho do arquivo
9
7
8
1
2
0
4
'''
opcaoOrdenacao = int(sys.argv[1])
arquivoDeEntrada = sys.argv[2]
arquivo = open(arquivoDeEntrada, 'r')
tamanho = int(arquivo.readline())
lista = range(0,tamanho)
for i in range(0,tamanho):
    lista[i] = int(arquivo.readline()) #conversao feita na leitura
tempo = []

#------- PROCESSAMENTO -------

# 1 - heap sort
if opcaoOrdenacao == 1:
    t = timeit.Timer("heapSort(lista, len(lista)-1)","from __main__ import lista, heapSort")
    tempo = t.repeat(1,1)

#------- SAIDA -------
arquivoDeSaida = open("saida.txt", 'a')
arquivoDeSaida.write("Entrada: "+str(arquivoDeEntrada)+"\n")

if(opcaoOrdenacao == 1):
   arquivoDeSaida.write("Algoritmo: Heap Maximo\n")
elif(opcaoOrdenacao == 2):
   arquivoDeSaida.write("Algoritmo: Heap Sort\n")

print ("saida:")
for i in lista:
   print (i)
   arquivoDeSaida.write(""+str(i)+"\n")
print (tempo)
