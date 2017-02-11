#--- ALUNO - WALSAN JADSON ---

#------- IMPORTANDO BIBLIOTECAS -------
import sys
import timeit

#------- DEFININDO FUNCOES -------

def maiorValor(lista):
    maior = lista[0]
    for i in lista:
        if i > maior:
            maior = i
    return maior

#1--
def countSort(lista):
    numbersN = []
    numbersP = []
    for i in range(0,len(lista)):
        if lista[i] <= 0:
            numbersN.append(lista[i])
        else:
            numbersP.append(lista[i])
    

    #numbersP
    maior = maiorValor(numbersP)

    #frequencia
    c = [0 for i in range(0,maior+1)]
    for i in range(0,len(numbersP)):
        c[numbersP[i]-1] += 1

    #cumulativa
    for i in range(1,len(c)):
        c[i] += c[i-1]

    b = [0 for i in range(0,len(numbersP))]
    for i in range(0,len(b)):
        b[c[numbersP[i]-1]-1] = numbersP[i]
        c[numbersP[i]-1] -=1

    for i in range(0,len(b)):
        numbersP[i] = b[i]

    #numbersN
    #invertendo os valores de numbersN
    numbersN = [i*-1 for i in numbersN ]
    maior = maiorValor(numbersN)

    #frequencia
    c = [0 for i in range(0,maior+1)]
    for i in range(0,len(numbersN)):
        c[numbersN[i]-1] += 1

    #cumulativa
    for i in range(1,len(c)):
        c[i] += c[i-1]

    b = [0 for i in range(0,len(numbersN))]
    for i in range(0,len(b)):
        b[c[numbersN[i]-1]-1] = numbersN[i]
        c[numbersN[i]-1] -=1

    for i in range(0,len(b)):
        numbersN[i] = b[i]
    numbersN = [i*-1 for i in numbersN ]
    numbersN.reverse()

    indexAux = 0
    for number in numbersN:
        lista[indexAux] = number
        indexAux += 1
    for number in numbersP:
        lista[indexAux] = number
        indexAux += 1

#2--
def bucketSort(lista):
    numberOfBuckets = len(lista)/20

    #buckets de valores negativos
    bucketsP = [[] for i in range(0,numberOfBuckets)]
    #buckets de valores positivos
    bucketsN = [[] for i in range(0,numberOfBuckets)]
    
    #colocando valores nos buckets
    for i in range(0,len(lista)):
        if lista[i] > 0:
            j = numberOfBuckets - 1
            while(True):
                if j < 0:
                    break
                if lista[i] >= (j*10):
                    bucketsP[j].append(lista[i])
                    break
                j -= 1
        else:
            j = numberOfBuckets - 1
            while(True):
                if j < 0:
                    break
                if abs(lista[i]) >= (j*10):
                    bucketsN[j].append(lista[i])
                    break
                j -= 1

    #ordenando os valores dos buckets
    for bucket in bucketsP:
        bucket.sort()
    for bucket in bucketsN:
        bucket.sort()

    bucketsN.reverse()

    #colocando os valores ordenados nos vetor original
    indexAux = 0
    for bucket in bucketsN:
        for i in bucket:
            lista[indexAux] = i
            indexAux += 1
    
    for bucket in bucketsP:
        for i in bucket:
            lista[indexAux] = i
            indexAux += 1

def countingSort(lista, exp1):
    tam = len(lista)
    output = [0]*(tam)    #vetor de saida
    count = [0]*(10)    #inicializando os elementos de count com valor 0

    for i in range(0,tam):
        index = (lista[i]/exp1)
        count[ (index)%10 ] += 1

    for i in range(1,10):
        count[i] += count[i-1]

    i = tam-1
    while(i>=0):
        index = (lista[i]/exp1)
        output[ count[ (index)%10 ] - 1 ] = lista[i]
        count[ (index)%10 ] -= 1
        i -= 1

    i = 0
    for i in range(0,len(lista)):
        lista[i] = output[i]

#3--
def radixSort(lista):
    numbersN = []
    numbersP = []
    for i in range(0,len(lista)):
        if lista[i] <= 0:
            numbersN.append(lista[i])
        else:
            numbersP.append(lista[i])

    #numbersN
    #invertendo os valores de numbersN
    numbersN = [i*-1 for i in numbersN ]
    maior = maiorValor(numbersN)
    exp = 1
    while maior/exp > 0:        
        countingSort(numbersN, exp)
        exp *= 10
    numbersN = [i*-1 for i in numbersN ]
    numbersN.reverse()
    
    #numbersP
    maior = maiorValor(numbersP)
    exp = 1
    while maior/exp > 0:        
        countingSort(numbersP, exp)
        exp *= 10
        
    indexAux = 0
    for number in numbersN:
        lista[indexAux] = number
        indexAux += 1
    for number in numbersP:
        lista[indexAux] = number
        indexAux += 1
    
#------- ENTRADA -------
'''
Exemplo de chamada a ser executada pelo terminal pra ser
proccessada com o metodo 5 (heapSort) :

>python Ordenacao01.py 5
7 #tamanho do vetor
10 #tamanho do intervalo
9 #primeiro elemento do array
7 #segundo elemento do array
8 #...
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
tempo = []

#------- PROCESSAMENTO -------

# 1 - count sort
if opcao == 1:
    t = timeit.Timer("countSort(lista)","from __main__ import lista, countSort")
    tempo = t.repeat(1,1)

# 2 - bucket sort
if opcao == 2:
    t = timeit.Timer("bucketSort(lista)","from __main__ import lista, bucketSort")
    tempo = t.repeat(1,1)

# 3 - radix sort
if opcao == 3:
    t = timeit.Timer("radixSort(lista)","from __main__ import lista, radixSort")
    tempo = t.repeat(1,1)

#------- SAIDA -------
for i in lista:
    print i
print tempo

