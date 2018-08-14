#--- ALUNO - WALSAN JADSON ---

#------- IMPORTANDO BIBLIOTECAS -------
import sys
import timeit

#------- DEFININDO FUNCOES -------

#-- 1
def mergeSort(lista):
    print ("entrou no mergeSort")
    if len(lista) > 1:
        pontoMedio = len(lista)/2
        listaDaEsquerda = lista[:pontoMedio]
        listaDaDireita = lista[pontoMedio:]
        mergeSort(listaDaEsquerda)
        mergeSort(listaDaDireita)

        i = 0
        j = 0
        k = 0

        #ordena as listas da direita e da esquerda
        while i < len(listaDaEsquerda) and j < len(listaDaDireita):
            if listaDaEsquerda[i] < listaDaDireita[j]:
                lista[k]=listaDaEsquerda[i]
                i += 1
            else:
                lista[k]=listaDaDireita[j]
                j += 1
            k += 1

        #concatena as listas da direita e esquerda jah ordenadas
        while i < len(listaDaEsquerda):
            lista[k]=listaDaEsquerda[i]
            i += 1
            k += 1

        while j < len(listaDaDireita):
            lista[k]=listaDaDireita[j]
            j += 1
            k += 1

#-- 2
def quickSort(lista, inicio, fim):
    print ("entrou no quickSort")
    if(inicio < fim):
        pivo = particiona(lista, inicio, fim)
        quickSort(lista, inicio, pivo-1)
        quickSort(lista, pivo+1, fim)

def particiona(lista, inicio, fim):
    pivo = lista[fim]
    i = inicio
    
    for j in range(inicio,fim):
        if lista[j] <= pivo:
            aux = lista[i]
            lista[i] = lista[j]     #troca
            lista[j] = aux      #troca
            i += 1
    aux = lista[i]
    lista[i] = lista[fim]     #troca
    lista[fim] = aux      #troca

    return i


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

# 1 - merge sort
if opcaoOrdenacao == 1:
    t = timeit.Timer("mergeSort(lista)","from __main__ import lista, mergeSort")
    tempo = t.repeat(1,1)

# 2 - quick sort
if opcaoOrdenacao == 2:
    t = timeit.Timer("quickSort(lista, 0, len(lista)-1)","from __main__ import lista, quickSort")
    tempo = t.repeat(1,1)

#------- SAIDA -------
arquivoDeSaida = open("saida.txt", 'a')
arquivoDeSaida.write("Entrada: "+str(arquivoDeEntrada)+"\n")

if(opcaoOrdenacao == 1):
   arquivoDeSaida.write("Algoritmo: Merge Sort\n")
elif(opcaoOrdenacao == 2):
   arquivoDeSaida.write("Algoritmo: Quick Sort\n")

for i in lista:
   print (i)
   arquivoDeSaida.write(""+str(i)+"\n")
print (tempo)
