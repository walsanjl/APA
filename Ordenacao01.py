#--- ALUNO - WALSAN JADSON ---

#------- IMPORTANDO BIBLIOTECAS -------
import sys

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

#-- 3
def mergeSort(lista):
    if len(lista) > 1:
        pontoMedio = len(lista)/2
        listaDaEsquerda = lista[:pontoMedio]
        listaDaDireita = lista[pontoMedio:]
        mergeSort(listaDaEsquerda)
        mergeSort(listaDaDireita)

        i = 0
        j = 0
        k = 0
        while i < len(listaDaEsquerda) and j < len(listaDaDireita):
            if listaDaEsquerda[i] < listaDaDireita[j]:
                lista[k]=listaDaEsquerda[i]
                i += 1
            else:
                lista[k]=listaDaDireita[j]
                j += 1
            k += 1

        while i < len(listaDaEsquerda):
            lista[k]=listaDaEsquerda[i]
            i += 1
            k += 1

        while j < len(listaDaDireita):
            lista[k]=listaDaDireita[j]
            j += 1
            k += 1

#-- 4
def quickSort(lista, inicio, fim):
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

#-- 5
def heapSort(lista):
    n = len(lista)-1

    #i = n/2
    for i in range(n/2,-1,-1):
        lista = maxHeap(lista, i, n)

    for i in range(n, 0, -1):
        aux = lista[0]
        lista[0] = lista[i]     #troca
        lista[i] = aux     #troca
        n = n-1
        maxHeap(lista, 0, n)

def maxHeap(lista, i, n):
    l = 2*i
    r = 2*i+1
    if l <= n and lista[l] > lista[i]:
        maior = l
    else:
        maior = i
    if r <= n and lista[r] > lista[maior]:
        maior = r
    if maior != i:
        aux = lista[i]
        lista[i] = lista[maior]     #troca
        lista[maior] = aux     #troca
        maxHeap(lista, maior, n)
    return lista

#------- ENTRADA -------
'''
Exemplo de chamada a ser executada pelo terminal pra ser
proccessada com o metodo 5 (heapSort) :

>python Ordenacao01.py 5
7 #tamanho do arquivo
9
7
8
1
2
0
4
'''
opcao = int(sys.argv[1])
tamanho = int(raw_input())
lista = range(0,tamanho)
for i in range(0,tamanho):
    lista[i] = int(raw_input()) #conversao feita na leitura

#------- PROCESSAMENTO -------

#selection sort
if opcao == 1:
    selectionSort(lista)

#insertion sort
if opcao == 2:
    insertionSort(lista)

#merge sort
if opcao == 3:
    mergeSort(lista)

#quick sort
if opcao == 4:
    quickSort(lista, 0, len(lista)-1)

#heap sort
if opcao == 5:
    heapSort(lista)

#------- SAIDA -------
for i in lista:
    print i

