#importar bibliotecas

from funcoes import *
from jogo2 import *
import random

#criar variavel do palpite
palpite = ''

#codigos das cores
class bcolors:
    LIGHT_CYAN = '\033[1;36m'
    RED = '\033[0;31m'
    DARK_GRAY = '\033[1;30m'
    normal = '\033[0m'
    YELLOW = '\033[1;33m'

#desenho de entrada e quadro de opcoes
print(' ============================ ')
print('|                            |')
print('| BEM VINDO AO INSPER PAÍSES |')
print('|                            |')
print(' ==== DESIGN DE SOFTWARE ==== ')

print('\nComandos:')

print('\ndica          - entra no mercado de dicas')
print('desisto       - desiste da rodada')
print('inventario    - exibe sua posição')

#looping principal
while palpite != 'desisto':

    dados_paises = normaliza(dados)
    sorteado = sorteia_pais(dados_paises)
    tentativa = 20
    lista = []
    dic = {}
    string = ''
    lista_cor = []
    lista_paises = []
    lista_cor2 = []
    string2 = ''
    lista_letra = []
    i = 0
    j = 0
    opcoes = ''
    #looping para cada tentativa com todas as condicoes
    while tentativa > 0:
        print('\nUm país foi escolhido, tente advinhar!')
        print('Você tem {0} tentativa(s)'.format(tentativa))
        palpite = input('\nQual o seu palpite?')
        tentativa -= 1
        palpite = palpite.lower()

        #caso escolha o pais sorteado
        if palpite == sorteado:
            print('\n*** Parabéns! Você ganhou após {0} tentativa(s)!'.format(20 - tentativa))
            break
        #caso o jogador queira desistir
        elif palpite == 'desisto':
            desistencia = input('Tem certeza de que quer desistir da rodada? [s/n]')
            if desistencia == 's':
                print ('Que deselegante desistir, o pais era: {0}'.format(sorteado))
                break
            else:
                print(palpite)
        
        #caso o palpite estiver nas chaves dos dicionarios calcular distancia
        elif palpite in dados_paises.keys():
            for pais in dados_paises:
                    r = 6371
                    latitudeA = dados_paises[palpite.lower()]['geo']['latitude']
                    longitudeA = dados_paises[palpite.lower()]['geo']['longitude']
                    latitudeB = dados_paises[sorteado]['geo']['latitude']
                    longitudeB = dados_paises[sorteado]['geo']['longitude']
            distancias = haversine(r, latitudeA, longitudeA, latitudeB, longitudeB)
        
        #caso o palpite estiver nas chaves dos dicionarios e palpite nao estiver na lista de paises , adicionar em ordem
        if palpite in dados_paises.keys() and palpite not in lista_paises:
            lista = adiciona_em_ordem(palpite, distancias, lista)
            lista_paises.append(palpite)
        elif palpite in dados_paises.keys() and palpite in lista_paises:
            tentativa+=1
            
        print('\nDistância:')
        #colocar as cores em cada pais e distancia
        for termo in lista:
                if int(termo[1]) <= 1000:
                    print(bcolors.LIGHT_CYAN+'{0} -> {1} km'.format(termo[0], int(termo[1]))+bcolors.normal)
                elif int(termo[1]) > 1000 and int(termo[1]) <= 2500:
                    print(bcolors.YELLOW+'{0} -> {1} km'.format(termo[0], int(termo[1]))+bcolors.normal)
                elif int(termo[1]) > 2500 and int(termo[1]) <= 5000:
                    print(bcolors.RED+'{0} -> {1} km'.format(termo[0], int(termo[1]))+bcolors.normal)
                elif int(termo[1]) > 5000:
                    print(bcolors.DARK_GRAY+'{0} -> {1} km'.format(termo[0], int(termo[1]))+bcolors.normal)
                
        #dicas
        print('\nDicas:')
        if dic != {}:
            print(string)
        if palpite == 'dica':
            tentativa +=1
            print('----------------------------------------')
            if tentativa > 4 and j <= len(lista_cor):
                print('1. Cor da Bandeira  - custa 4 tentativas')
            if tentativa > 3 and i <= len(dados_paises[sorteado]['capital']):
                print('2. Letra da capital - custa 3 tentativas')
            if tentativa > 6 and 'Área' not in string:
                print('3. Área             - custa 6 tentativas')
            if tentativa > 5 and 'População' not in string:
                print('4. População        - custa 5 tentativas')
            if tentativa > 7 and 'Continente' not in string:
                print('5. Continente       - custa 7 tentativas')
            print('0. Sem dica                             ')
            print('----------------------------------------')
            dica = ''
            while dica != '0' and dica != '1' and dica != '2' and dica != '3' and dica != '4' and dica != '5':
                if opcoes == '':
                    dica = input('Escolha a sua opção [0|1|2|3|4|5]:')
                if dica != '0' and dica != '1' and dica != '2' and dica != '3' and dica != '4' and dica != '5' :
                    print('Opção inválida')
                else:    
                    break
            if dica == '1' and tentativa > 4:
                j += 1
                bandeira = dados_paises[sorteado]['bandeira']
                for cores in bandeira:
                    a = dados_paises[sorteado]['bandeira'][cores]
                    if a > 0 and cores != 'outras' and cores not in lista_cor:
                        lista_cor.append(cores)
                aleatorio = random.choice(lista_cor)
                lista_cor.remove(aleatorio)
                if aleatorio not in lista_cor2:
                    lista_cor2.append(aleatorio)
                print(lista_cor2)
                if len(lista_cor) == 0:
                    tentativa+=1
                if 'Cores da Bandeira' in string:
                    string += '-Cores da Bandeira: {0}'.format(','.join(lista_cor2))
                string = '\n-Cores da Bandeira: {0}'.format(','.join(lista_cor2))
                
                print('\nDistância:')
                #colocar as cores em cada pais e distancia
                for termo in lista:
                    if int(termo[1]) <= 1000:
                        print(bcolors.LIGHT_CYAN+'{0} -> {1} km'.format(termo[0], int(termo[1]))+bcolors.normal)
                    elif int(termo[1]) > 1000 and int(termo[1]) <= 2500:
                        print(bcolors.YELLOW+'{0} -> {1} km'.format(termo[0], int(termo[1]))+bcolors.normal)
                    elif int(termo[1]) > 2500 and int(termo[1]) <= 5000:
                        print(bcolors.RED+'{0} -> {1} km'.format(termo[0], int(termo[1]))+bcolors.normal)
                    elif int(termo[1]) > 5000:
                        print(bcolors.DARK_GRAY+'{0} -> {1} km'.format(termo[0], int(termo[1]))+bcolors.normal)
                print('\nDicas:')    
                print(string)
                tentativa -=4
            elif dica == '2' and tentativa > 3:
                palavra = dados_paises[sorteado]['capital']
                i += 1
                for letra in palavra:
                    sorteio = sorteia_letra(palavra, lista_letra)
                lista_letra.append(sorteio)
                if 'Letras' in string:
                    string += '\nLetras da capital: {0}'.format(sorteio)
                string += '\nLetras da capital: {0}'.format(sorteio)
                tentativa -= 3
                for termo in lista:
                    if int(termo[1]) <= 1000:
                        print(bcolors.LIGHT_CYAN+'{0} -> {1} km'.format(termo[0], int(termo[1]))+bcolors.normal)
                    elif int(termo[1]) > 1000 and int(termo[1]) <= 2500:
                        print(bcolors.YELLOW+'{0} -> {1} km'.format(termo[0], int(termo[1]))+bcolors.normal)
                    elif int(termo[1]) > 2500 and int(termo[1]) <= 5000:
                        print(bcolors.RED+'{0} -> {1} km'.format(termo[0], int(termo[1]))+bcolors.normal)
                    elif int(termo[1]) > 5000:
                        print(bcolors.DARK_GRAY+'{0} -> {1} km'.format(termo[0], int(termo[1]))+bcolors.normal)
                print('\nDicas:')
                print(string)
            elif dica == '3' and tentativa >6 and 'Área' not in string:
                dic['Área'] = dados_paises[sorteado]['area']
                string += '\n-{0}: {1}'.format('Área', dic['Área'])
                tentativa -= 6
                for termo in lista:
                    if int(termo[1]) <= 1000:
                        print(bcolors.LIGHT_CYAN+'{0} -> {1} km'.format(termo[0], int(termo[1]))+bcolors.normal)
                    elif int(termo[1]) > 1000 and int(termo[1]) <= 2500:
                        print(bcolors.YELLOW+'{0} -> {1} km'.format(termo[0], int(termo[1]))+bcolors.normal)
                    elif int(termo[1]) > 2500 and int(termo[1]) <= 5000:
                        print(bcolors.RED+'{0} -> {1} km'.format(termo[0], int(termo[1]))+bcolors.normal)
                    elif int(termo[1]) > 5000:
                        print(bcolors.DARK_GRAY+'{0} -> {1} km'.format(termo[0], int(termo[1]))+bcolors.normal)
                print('\nDicas:')
                print(string)
            elif dica == '4' and tentativa >5 and 'População' not in string:
                dic['População'] = dados_paises[sorteado]['populacao']
                string += '\n-População:{0}'.format(dic['População'])
                tentativa -= 5
                for termo in lista:
                    if int(termo[1]) <= 1000:
                        print(bcolors.LIGHT_CYAN+'{0} -> {1} km'.format(termo[0], int(termo[1]))+bcolors.normal)
                    elif int(termo[1]) > 1000 and int(termo[1]) <= 2500:
                        print(bcolors.YELLOW+'{0} -> {1} km'.format(termo[0], int(termo[1]))+bcolors.normal)
                    elif int(termo[1]) > 2500 and int(termo[1]) <= 5000:
                        print(bcolors.RED+'{0} -> {1} km'.format(termo[0], int(termo[1]))+bcolors.normal)
                    elif int(termo[1]) > 5000:
                        print(bcolors.DARK_GRAY+'{0} -> {1} km'.format(termo[0], int(termo[1]))+bcolors.normal)
                print('\nDicas:')
                print(string)
            elif dica == '5' and tentativa > 7 and 'Continente' not in string:
                dic['Continente'] = dados_paises[sorteado]['continente']
                string += '\n-Continente: {0}'.format(dic['Continente'])
                for termo in lista:
                    if int(termo[1]) <= 1000:
                        print(bcolors.LIGHT_CYAN+'{0} -> {1} km'.format(termo[0], int(termo[1]))+bcolors.normal)
                    elif int(termo[1]) > 1000 and int(termo[1]) <= 2500:
                        print(bcolors.YELLOW+'{0} -> {1} km'.format(termo[0], int(termo[1]))+bcolors.normal)
                    elif int(termo[1]) > 2500 and int(termo[1]) <= 5000:
                        print(bcolors.RED+'{0} -> {1} km'.format(termo[0], int(termo[1]))+bcolors.normal)
                    elif int(termo[1]) > 5000:
                        print(bcolors.DARK_GRAY+'{0} -> {1} km'.format(termo[0], int(termo[1]))+bcolors.normal)
                print('\nDicas:')
                print(string)
                tentativa -= 7
            elif dica == '0':
                tentativa += 1
                for termo in lista:
                    if int(termo[1]) <= 1000:
                        print(bcolors.LIGHT_CYAN+'{0} -> {1} km'.format(termo[0], int(termo[1]))+bcolors.normal)
                    elif int(termo[1]) > 1000 and int(termo[1]) <= 2500:
                        print(bcolors.YELLOW+'{0} -> {1} km'.format(termo[0], int(termo[1]))+bcolors.normal)
                    elif int(termo[1]) > 2500 and int(termo[1]) <= 5000:
                        print(bcolors.RED+'{0} -> {1} km'.format(termo[0], int(termo[1]))+bcolors.normal)
                    elif int(termo[1]) > 5000:
                        print(bcolors.DARK_GRAY+'{0} -> {1} km'.format(termo[0], int(termo[1]))+bcolors.normal)
                print('\nDicas:')
                if dic != {}:
                    print(string)
                    continue
                    tentativa += 1
            else:
                for termo in lista:
                    if int(termo[1]) <= 1000:
                        print(bcolors.LIGHT_CYAN+'{0} -> {1} km'.format(termo[0], int(termo[1]))+bcolors.normal)
                    elif int(termo[1]) > 1000 and int(termo[1]) <= 2500:
                        print(bcolors.YELLOW+'{0} -> {1} km'.format(termo[0], int(termo[1]))+bcolors.normal)
                    elif int(termo[1]) > 2500 and int(termo[1]) <= 5000:
                        print(bcolors.RED+'{0} -> {1} km'.format(termo[0], int(termo[1]))+bcolors.normal)
                    elif int(termo[1]) > 5000:
                        print(bcolors.DARK_GRAY+'{0} -> {1} km'.format(termo[0], int(termo[1]))+bcolors.normal)
                print('\nDicas:')
                print(string) 
        elif palpite == 'inventario':
            tentativa +=1
            

        elif palpite not in dados_paises.keys():
            tentativa += 1
            print('\nPaís desconhecido')
        
    if tentativa == 0:
        print('\n>>> Você perdeu, o país era: {0}'.format(sorteado))
    jogar_novamente = input('Jogar novamente? [s/n]')
    palpite = ""
    if jogar_novamente != 's':
        palpita = ""
        print('Até a próxima!')
        break