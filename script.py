
#------- IMPORTANDO BIBLIOTECAS -------
import os
import sys

#------- DEFININDO FUNCOES -------

"""
 * Descricao Geral: Essa funcao leh o conteudo do tipo -[23.351237589318153]- que equivale
 *                  ao tempo (segundos) de execucao de um algoritmo de ordenacao, extrai 
 *                  o numero dessa String e verifica se esse numero eh maior que 300s (5min).
 *                  
 * Entrada: String que representa um endereco de arquivo para leitura
 *
 * Saida: True/False
"""
def ehDemorado(arquivo):
    arquivo = open(arquivo, 'r')
    tempo = arquivo.readline()
    numero =  ""
    for i in range(1, len(tempo)-2):
        numero = numero+tempo[i]
    numero = float(numero)
    if numero > 300:
        return True
    else:
        return False

def calculaMedia(lista):
    n = 0.0
    for i in lista:
        n = n + i
    media = n/len(lista)
    return media

#------- ENTRADA -------

#------- PROCESSAMENTO -------

#10.100000
for i in range(1,6):
    for j in range(1,11):
        os.system("call python Ordenacao01.py "+str(i)+" < 10.100000."+str(j)+".in > 10.100000."+str(j)+"_saida_"+str(i)+".txt")
        if ehDemorado("10.100000."+str(j)+"_saida_"+str(i)+".txt") == True:
            break

#10.500000
for i in range(1,6):
    for j in range(1,11):
        os.system("call python Ordenacao01.py "+str(i)+" < 10.500000."+str(j)+".in > 10.500000."+str(j)+"_saida_"+str(i)+".txt")
        if ehDemorado("10.500000."+str(j)+"_saida_"+str(i)+".txt") == True:
            break

#10.1000000
for i in range(1,6):
    for j in range(1,11):
        os.system("call python Ordenacao01.py "+str(i)+" < 10.1000000."+str(j)+".in > 10.1000000."+str(j)+"_saida_"+str(i)+".txt")
        if ehDemorado("10.1000000."+str(j)+"_saida_"+str(i)+".txt") == True:
            break
    
#50.100000
for i in range(1,6):
    for j in range(1,11):
        os.system("call python Ordenacao01.py "+str(i)+" < 50.100000."+str(j)+".in > 50.100000."+str(j)+"_saida_"+str(i)+".txt")
        if ehDemorado("50.100000."+str(j)+"_saida_"+str(i)+".txt") == True:
            break
        
#50.500000
for i in range(1,6):
    for j in range(1,11):
        os.system("call python Ordenacao01.py "+str(i)+" < 50.500000."+str(j)+".in > 50.500000."+str(j)+"_saida_"+str(i)+".txt")
        if ehDemorado("50.500000."+str(j)+"_saida_"+str(i)+".txt") == True:
            break

#50.1000000
for i in range(1,6):
    for j in range(1,11):
        os.system("call python Ordenacao01.py "+str(i)+" < 50.1000000."+str(j)+".in > 50.1000000."+str(j)+"_saida_"+str(i)+".txt")
        if ehDemorado("50.1000000."+str(j)+"_saida_"+str(i)+".txt") == True:
            break

#90.100000
for i in range(1,6):
    for j in range(1,11):
        os.system("call python Ordenacao01.py "+str(i)+" < 90.100000."+str(j)+".in > 90.100000."+str(j)+"_saida_"+str(i)+".txt")
        if ehDemorado("90.100000."+str(j)+"_saida_"+str(i)+".txt") == True:
            break

#90.500000
for i in range(1,6):
    for j in range(1,11):
        os.system("call python Ordenacao01.py "+str(i)+" < 90.500000."+str(j)+".in > 90.500000."+str(j)+"_saida_"+str(i)+".txt")
        if ehDemorado("90.500000."+str(j)+"_saida_"+str(i)+".txt") == True:
            break

#90.1000000
for i in range(1,6):
    for j in range(1,11):
        os.system("call python Ordenacao01.py "+str(i)+" < 90.1000000."+str(j)+".in > 90.1000000."+str(j)+"_saida_"+str(i)+".txt")
        if ehDemorado("90.1000000."+str(j)+"_saida_"+str(i)+".txt") == True:
            break

#------- SAIDA -------

arquivoDeSaida = open("saida.txt", 'a')

#10.100000
arquivoDeSaida.write("\nSub 10.100000:"+'\n')
for i in range(1,6):
    listaDeTempos = []
    maiorQue5 = False
    for j in range(1,11):   
        arquivoDeLeitura = open("10.100000."+str(j)+"_saida_"+str(i)+".txt", 'r')
        conteudo = arquivoDeLeitura.readline()

        #caso em que o conteudo do arquivo eh nulo
        if conteudo == "":
            maiorQue5 = True
            break

        numero =  ""
        for w in range(1, len(conteudo)-2):
            numero = numero+conteudo[w]
        numero = float(numero)
        
        #caso em que o conteudo do arquivo eh maior que 300s segundos
        if numero > 300.0:
            maiorQue5 = True
            break
        
        listaDeTempos.append(numero)
        arquivoDeLeitura.close()
        
    if maiorQue5 == True:
        arquivoDeSaida.write("  algoritmo "+str(i)+": >5min\n")
    else:
        media = calculaMedia(listaDeTempos)
        arquivoDeSaida.write("  algoritmo "+str(i)+": "+str(media)+"\n")
        
#10.500000
arquivoDeSaida.write("\nSub 10.500000:"+'\n')
for i in range(1,6):
    listaDeTempos = []
    maiorQue5 = False
    for j in range(1,11):   
        arquivoDeLeitura = open("10.500000."+str(j)+"_saida_"+str(i)+".txt", 'r')
        conteudo = arquivoDeLeitura.readline()

        #caso em que o conteudo do arquivo eh nulo
        if conteudo == "":
            maiorQue5 = True
            break

        numero =  ""
        for w in range(1, len(conteudo)-2):
            numero = numero+conteudo[w]
        numero = float(numero)
        
        #caso em que o conteudo do arquivo eh maior que 300s segundos
        if numero > 300.0:
            maiorQue5 = True
            break
        
        listaDeTempos.append(numero)
        arquivoDeLeitura.close()
        
    if maiorQue5 == True:
        arquivoDeSaida.write("  algoritmo "+str(i)+": >5min\n")
    else:
        media = calculaMedia(listaDeTempos)
        arquivoDeSaida.write("  algoritmo "+str(i)+": "+str(media)+"\n")

#10.1000000
arquivoDeSaida.write("\nSub 10.1000000:"+'\n')
for i in range(1,6):
    listaDeTempos = []
    maiorQue5 = False
    for j in range(1,11):   
        arquivoDeLeitura = open("10.1000000."+str(j)+"_saida_"+str(i)+".txt", 'r')
        conteudo = arquivoDeLeitura.readline()

        #caso em que o conteudo do arquivo eh nulo
        if conteudo == "":
            maiorQue5 = True
            break

        numero =  ""
        for w in range(1, len(conteudo)-2):
            numero = numero+conteudo[w]
        numero = float(numero)
        
        #caso em que o conteudo do arquivo eh maior que 300s segundos
        if numero > 300.0:
            maiorQue5 = True
            break
        
        listaDeTempos.append(numero)
        arquivoDeLeitura.close()
        
    if maiorQue5 == True:
        arquivoDeSaida.write("  algoritmo "+str(i)+": >5min\n")
    else:
        media = calculaMedia(listaDeTempos)
        arquivoDeSaida.write("  algoritmo "+str(i)+": "+str(media)+"\n")

#50.100000
arquivoDeSaida.write("\nSub 50.100000:"+'\n')
for i in range(1,6):
    listaDeTempos = []
    maiorQue5 = False
    for j in range(1,11):   
        arquivoDeLeitura = open("50.100000."+str(j)+"_saida_"+str(i)+".txt", 'r')
        conteudo = arquivoDeLeitura.readline()

        #caso em que o conteudo do arquivo eh nulo
        if conteudo == "":
            maiorQue5 = True
            break

        numero =  ""
        for w in range(1, len(conteudo)-2):
            numero = numero+conteudo[w]
        numero = float(numero)
        
        #caso em que o conteudo do arquivo eh maior que 300s segundos
        if numero > 300.0:
            maiorQue5 = True
            break
        
        listaDeTempos.append(numero)
        arquivoDeLeitura.close()
        
    if maiorQue5 == True:
        arquivoDeSaida.write("  algoritmo "+str(i)+": >5min\n")
    else:
        media = calculaMedia(listaDeTempos)
        arquivoDeSaida.write("  algoritmo "+str(i)+": "+str(media)+"\n")

#50.500000
arquivoDeSaida.write("\nSub 50.500000:"+'\n')
for i in range(1,6):
    listaDeTempos = []
    maiorQue5 = False
    for j in range(1,11):   
        arquivoDeLeitura = open("50.500000."+str(j)+"_saida_"+str(i)+".txt", 'r')
        conteudo = arquivoDeLeitura.readline()

        #caso em que o conteudo do arquivo eh nulo
        if conteudo == "":
            maiorQue5 = True
            break

        numero =  ""
        for w in range(1, len(conteudo)-2):
            numero = numero+conteudo[w]
        numero = float(numero)
        
        #caso em que o conteudo do arquivo eh maior que 300s segundos
        if numero > 300.0:
            maiorQue5 = True
            break
        
        listaDeTempos.append(numero)
        arquivoDeLeitura.close()
        
    if maiorQue5 == True:
        arquivoDeSaida.write("  algoritmo "+str(i)+": >5min\n")
    else:
        media = calculaMedia(listaDeTempos)
        arquivoDeSaida.write("  algoritmo "+str(i)+": "+str(media)+"\n")

#50.1000000
arquivoDeSaida.write("\nSub 50.1000000:"+'\n')
for i in range(1,6):
    listaDeTempos = []
    maiorQue5 = False
    for j in range(1,11):   
        arquivoDeLeitura = open("50.1000000."+str(j)+"_saida_"+str(i)+".txt", 'r')
        conteudo = arquivoDeLeitura.readline()

        #caso em que o conteudo do arquivo eh nulo
        if conteudo == "":
            maiorQue5 = True
            break

        numero =  ""
        for w in range(1, len(conteudo)-2):
            numero = numero+conteudo[w]
        numero = float(numero)
        
        #caso em que o conteudo do arquivo eh maior que 300s segundos
        if numero > 300.0:
            maiorQue5 = True
            break
        
        listaDeTempos.append(numero)
        arquivoDeLeitura.close()
        
    if maiorQue5 == True:
        arquivoDeSaida.write("  algoritmo "+str(i)+": >5min\n")
    else:
        media = calculaMedia(listaDeTempos)
        arquivoDeSaida.write("  algoritmo "+str(i)+": "+str(media)+"\n")

#90.100000
arquivoDeSaida.write("\nSub 90.100000:"+'\n')
for i in range(1,6):
    listaDeTempos = []
    maiorQue5 = False
    for j in range(1,11):   
        arquivoDeLeitura = open("90.100000."+str(j)+"_saida_"+str(i)+".txt", 'r')
        conteudo = arquivoDeLeitura.readline()

        #caso em que o conteudo do arquivo eh nulo
        if conteudo == "":
            maiorQue5 = True
            break

        numero =  ""
        for w in range(1, len(conteudo)-2):
            numero = numero+conteudo[w]
        numero = float(numero)
        
        #caso em que o conteudo do arquivo eh maior que 300s segundos
        if numero > 300.0:
            maiorQue5 = True
            break
        
        listaDeTempos.append(numero)
        arquivoDeLeitura.close()
        
    if maiorQue5 == True:
        arquivoDeSaida.write("  algoritmo "+str(i)+": >5min\n")
    else:
        media = calculaMedia(listaDeTempos)
        arquivoDeSaida.write("  algoritmo "+str(i)+": "+str(media)+"\n")

#90.500000
arquivoDeSaida.write("\nSub 90.500000:"+'\n')
for i in range(1,6):
    listaDeTempos = []
    maiorQue5 = False
    for j in range(1,11):   
        arquivoDeLeitura = open("90.500000."+str(j)+"_saida_"+str(i)+".txt", 'r')
        conteudo = arquivoDeLeitura.readline()

        #caso em que o conteudo do arquivo eh nulo
        if conteudo == "":
            maiorQue5 = True
            break

        numero =  ""
        for w in range(1, len(conteudo)-2):
            numero = numero+conteudo[w]
        numero = float(numero)
        
        #caso em que o conteudo do arquivo eh maior que 300s segundos
        if numero > 300.0:
            maiorQue5 = True
            break
        
        listaDeTempos.append(numero)
        arquivoDeLeitura.close()
        
    if maiorQue5 == True:
        arquivoDeSaida.write("  algoritmo "+str(i)+": >5min\n")
    else:
        media = calculaMedia(listaDeTempos)
        arquivoDeSaida.write("  algoritmo "+str(i)+": "+str(media)+"\n")

#90.1000000
arquivoDeSaida.write("\nSub 90.1000000:"+'\n')
for i in range(1,6):
    listaDeTempos = []
    maiorQue5 = False
    for j in range(1,11):   
        arquivoDeLeitura = open("90.1000000."+str(j)+"_saida_"+str(i)+".txt", 'r')
        conteudo = arquivoDeLeitura.readline()

        #caso em que o conteudo do arquivo eh nulo
        if conteudo == "":
            maiorQue5 = True
            break

        numero =  ""
        for w in range(1, len(conteudo)-2):
            numero = numero+conteudo[w]
        numero = float(numero)
        
        #caso em que o conteudo do arquivo eh maior que 300s segundos
        if numero > 300.0:
            maiorQue5 = True
            break
        
        listaDeTempos.append(numero)
        arquivoDeLeitura.close()
        
    if maiorQue5 == True:
        arquivoDeSaida.write("  algoritmo "+str(i)+": >5min\n")
    else:
        media = calculaMedia(listaDeTempos)
        arquivoDeSaida.write("  algoritmo "+str(i)+": "+str(media)+"\n")

arquivoDeSaida.close()
