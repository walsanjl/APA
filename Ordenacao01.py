#--- ALUNO - WALSAN JADSON ---

#------- IMPORTANDO BIBLIOTECAS -------
import sys
import timeit

#------- DEFININDO FUNCOES -------

#-- 1
def selectionSort(lista):
    for i in range(0, len(lista)):
        menor = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[menor]:
                menor = j
        aux = lista[i]
        lista[i] = lista[menor]     #troca
        lista[menor] = aux      #troca

#-- 2
def insertionSort(lista):
    for i in range(1, len(lista) ):
        eleito = lista[i]
        j = i - 1
        while j >= 0 and eleito < lista[j]:
            lista[j+1] = lista[j]   #troca
            j = j - 1
        lista[j+1] = eleito     #troca


#------- ENTRADA -------
'''
Exemplo de chamada a ser executada pelo terminal pra ser
proccessada com o metodo 2 (insertionSort) :

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
#tamanho = int(raw_input())
tamanho = int(arquivo.readline())
lista = range(0,tamanho)
for i in range(0,tamanho):
    #lista[i] = int(raw_input()) #conversao feita na leitura
    lista[i] = int(arquivo.readline()) #conversao feita na leitura
tempo = []

#------- PROCESSAMENTO -------

# 1 - selection sort
if opcaoOrdenacao == 1:
    t = timeit.Timer("selectionSort(lista)","from __main__ import lista, selectionSort")
    tempo = t.repeat(1,1)

# 2 - insertion sort
if opcaoOrdenacao == 2:
    t = timeit.Timer("insertionSort(lista)","from __main__ import lista, insertionSort")
    tempo = t.repeat(1,1)

#------- SAIDA -------
arquivoDeSaida = open("saida.txt", 'a')
arquivoDeSaida.write("Entrada: "+str(arquivoDeEntrada)+"\n")

if(opcaoOrdenacao == 1):
   arquivoDeSaida.write("Algoritmo: Selection Sort\n")
elif(opcaoOrdenacao == 2):
   arquivoDeSaida.write("Algoritmo: Insertion Sort\n")

for i in lista:
   print (i)
   arquivoDeSaida.write(""+str(i)+"\n")
print (tempo)

