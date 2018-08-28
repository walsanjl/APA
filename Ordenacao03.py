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

    #b.append(0)
    print ("entrou no countingSort")
    k = buscaMaior(a)
    print "maior numero da lista: "+str(k)
    
    #cria o vetor auxiliar e zera os elementos
    c = []
    for i in range(0, k+1):
	c.append(0)
    print (c)

    #incrementa
    for j in range(0, len(a)):
	c[a[j]] = c[a[j]] + 1
    print("incrementa")
    print(c)

    #acumula
    for i in range(1, k+1):
	c[i] = c[i] + c[i - 1]
    print("acumula")
    print(c)

    print(b)
    #ordena
    print ("ordena")
    print (len(a))
    for j in range(len(a)-1, -1, -1):
	print j
	b[c[a[j]]] = a[j]
	c[a[j]] = c[a[j]] - 1
    print(b)

    for i in range (0, len(lista)):
	lista[i] = b[i+1]

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

# 1 - counting sort
if opcaoOrdenacao == 1:
    t = timeit.Timer("countingSort(lista)","from __main__ import lista, countingSort")
    tempo = t.repeat(1,1)

'''
# 2 - quick sort
if opcaoOrdenacao == 2:
    t = timeit.Timer("quickSort(lista, 0, len(lista)-1)","from __main__ import lista, quickSort")
    tempo = t.repeat(1,1)
'''
#------- SAIDA -------
arquivoDeSaida = open("saida.txt", 'a')
arquivoDeSaida.write("Entrada: "+str(arquivoDeEntrada)+"\n")

if(opcaoOrdenacao == 1):
   arquivoDeSaida.write("Algoritmo: Merge Sort\n")
elif(opcaoOrdenacao == 2):
   arquivoDeSaida.write("Algoritmo: Quick Sort\n")

print ("saida:")
for i in lista:
   print (i)
   arquivoDeSaida.write(""+str(i)+"\n")
print (tempo)
