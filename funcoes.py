#Normalizando Base de Paises

def normaliza(dic):
    saida = {}
    for continente in dic:
        chave = dic[continente]
        for pais in chave:
            chave2 = chave[pais]
            saida[pais] = chave2
            saida[pais]['continente'] = continente 
    return saida

#Sorteando paises

import random
def sorteia_pais(dic):
    listachave = []
    for pais in dic:
        listachave.append(pais)
    a = random.choice(listachave)
    return a
        
#Dstancia de Haversine

from math import *
def haversine(r, latitudeA, longitudeA, latitudeB, longitudeB):
    a = 2 * r 
    b = sin(radians((latitudeB - latitudeA)/2))**2
    c = cos(radians(latitudeA)) * cos(radians(latitudeB)) * (sin(radians((longitudeB - longitudeA)/2))**2)
    e = (c + b)**(1/2)
    f = asin(e)
    d = a * f
    return d 

#Adicionando em uma Lista Ordenada

def adiciona_em_ordem(pais, distancia, lista):
    saida = [] 
    pais_distancia = [pais, distancia]
    if lista == []:
        saida.append(pais_distancia)

    for lista1 in lista:
        if distancia > lista1[1]:
            saida.append(lista1)
        elif distancia < lista1[1]:
            if pais_distancia not in saida:
                saida.append(pais_distancia)
                saida.append(lista1)
            else:
                saida.append(lista1)
    if pais_distancia not in saida:
        saida.append(pais_distancia)

    return saida

#Esta na lista

def esta_na_lista(pais, listap):

    for lista in listap:
            if pais == lista[0]:
                return True
    return False

#Soretia lista com restricoes

import random
def sorteia_letra(palavra, restrita):
    lista1 = []
    restricao = ['.', ',', '-', ';', ' ']
    letras = palavra.casefold()
    for letra in letras:
        if letra not in restrita and letra not in restricao and letra not in lista1:
            lista1.append(letra)
    if lista1 != []:
        sorteio = random.choice(lista1)
    else:
        sorteio = ''
    return sorteio