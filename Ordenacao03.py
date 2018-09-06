#--- ALUNO - WALSAN JADSON ---

#------- IMPORTANDO BIBLIOTECAS -------
import sys
import timeit

#------- DEFININDO FUNCOES -------

#-- 1
def countingSort(lista):
    a = lista
    print(a)
    b = [0]
    for i in range(0, len(a)):
		b.append(a[i])

    k = buscaMaior(a)
    print "maior numero da lista: "+str(k)
    
    #cria o vetor auxiliar e zera os elementos
    c = []
    for i in range(0, k+1):
		c.append(0)

    #incrementa
    for j in range(0, len(a)):
		c[a[j]] = c[a[j]] + 1

    #acumula
    for i in range(1, k+1):
		c[i] = c[i] + c[i - 1]

    #ordena
    for j in range(len(a)-1, -1, -1):
		b[c[a[j]]] = a[j]
		c[a[j]] = c[a[j]] - 1

	#retorno
    for i in range (0, len(lista)):
		lista[i] = b[i+1]

def countingSort2(lista, chave):
	a = lista
	print(a)
	b = [0]
	for i in range(0, len(a)):
		b.append(a[i])

	#cria o vetor auxiliar e zera os elementos
	c = [0] * 10

    #incrementa
	for j in range(0, len(a)):
		indice = (a[j]/chave)
		c[ indice%10 ] += 1

	#acumula
	for i in range(1, 10):
		c[i] += c[i-1]

	#ordena
	for j in range(len(a)-1, -1, -1):
		indice = a[j]/chave
		#b[c[a[j]]] = a[j]
		b[c[ indice%10 ]] = a[j]		
		#c[a[j]] = c[a[j]] - 1
		c[ indice%10 ] -= 1

	#retorno
	for i in range (0, len(lista)):
		lista[i] = b[i+1]

#-- 2
def radixSort(lista):
	maiorNumero = buscaMaior(lista)

	chave = 1
	while maiorNumero/chave > 0:
		countingSort2(lista,chave)
		chave *= 10

def buscaMaior(lista):
    maiorNumero = 0
    for i in range(0, len(lista)):
		if(lista[i] > maiorNumero):
			maiorNumero = lista[i]
    return maiorNumero

#------- ENTRADA -------
'''
Exemplo de chamada a ser executada pelo terminal pra ser
proccessada com o metodo 1 (countingSort) :
>python Ordenacao03.py 1 entrada.txt
'''
opcaoOrdenacao = int(sys.argv[1])
arquivoDeEntrada = sys.argv[2]
arquivo = open(arquivoDeEntrada, 'r')
#tamanho = int(raw_input())
tamanho = int(arquivo.readline())
lista = range(0,tamanho)
for i in range(0,tamanho):
    #lista[i] = int(raw_input()) #conversao feita na leitura
    lista[i] = int(arquivo.readline()) #conversao feita na leitura
tempo = []

#------- PROCESSAMENTO -------

# 1 - counting sort
if opcaoOrdenacao == 1:
    t = timeit.Timer("countingSort(lista)","from __main__ import lista, countingSort")
    tempo = t.repeat(1,1)

# 2 - radix sort
if opcaoOrdenacao == 2:
    t = timeit.Timer("radixSort(lista)","from __main__ import lista, radixSort")
    tempo = t.repeat(1,1)

#------- SAIDA -------
arquivoDeSaida = open("saida.txt", 'a')
arquivoDeSaida.write("Entrada: "+str(arquivoDeEntrada)+"\n")

if(opcaoOrdenacao == 1):
   arquivoDeSaida.write("Algoritmo: Counting Sort\n")

if(opcaoOrdenacao == 2):
   arquivoDeSaida.write("Algoritmo: Radix Sort\n")

print ("saida:")
for i in lista:
   print (i)
   arquivoDeSaida.write(""+str(i)+"\n")
print (tempo)
