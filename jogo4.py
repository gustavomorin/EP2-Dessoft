from funcoes import *
from jogo2 import *
import random

palpite = ''

print(' ============================ ')
print('|                            |')
print('| BEM VINDO AO INSPER PAÍSES |')
print('|                            |')
print(' ==== DESIGN DE SOFTWARE ==== ')

print('\nComandos:')

print('\ndica          - entra no mercado de dicas')
print('desisto       - desiste da rodada')
print('inventario    - exibe sua posição')

while palpite != 'desisto':

    dados_paises = normaliza(dados)
    sorteado = sorteia_pais(dados_paises)
    tentativa = 20
    print(sorteado)
    lista = []
    dic = {}
    string = ''
    lista_cor = []
    lista_paises = []

    while tentativa > 0:
        print('\nUm país foi escolhido, tente advinhar!')
        print('Você tem {0} tentativa(s)'.format(tentativa))
        palpite = input('\nQual o seu palpite?')
        tentativa -= 1
        palpite = palpite.lower()

        
        if palpite == sorteado:
            print('\n*** Parabéns! Você ganhou após {0} tentativa(s)!'.format(20 - tentativa))
            break
        
        elif palpite == 'desisto':
            desistencia = input('Tem certeza de que quer desistir da rodada? [s/n]')
            if desistencia == 's':
                print ('Que deselegante desistir, o pais era: {0}'.format(sorteado))
                break
            else:
                print(palpite)
        
        elif palpite in dados_paises.keys():
            for pais in dados_paises:
                    r = 6371
                    latitudeA = dados_paises[palpite.lower()]['geo']['latitude']
                    longitudeA = dados_paises[palpite.lower()]['geo']['longitude']
                    latitudeB = dados_paises[sorteado]['geo']['latitude']
                    longitudeB = dados_paises[sorteado]['geo']['longitude']
            distancias = haversine(r, latitudeA, longitudeA, latitudeB, longitudeB)
        
        if palpite in dados_paises.keys() and palpite not in lista_paises:
            lista = adiciona_em_ordem(palpite, distancias, lista)
            lista_paises.append(palpite)
        elif palpite in dados_paises.keys() and palpite in lista_paises:
            tentativa+=1
            
        print('\nDistância:')

        for termo in lista:
                print('{0} -> {1} km'.format(termo[0], int(termo[1])))
        print('\nDicas:')
        if dic != {}:
            print(string)
        if palpite == 'dica':
            tentativa +=1
            print('----------------------------------------')
            if tentativa > 4:
                print('1. Cor da Bandeira  - custa 4 tentativas')
            if tentativa > 3:
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
            while dica != '0' and dica != '1' and dica != '2' and dica != '3' and dica != '4' and dica != '5' :
                dica = input('Escolha a sua opção [0|1|2|3|4|5]:')
                if dica != '0' and dica != '1' and dica != '2' and dica != '3' and dica != '4' and dica != '5' :
                    print('Opção inválida')
                else:    
                    break
            if dica == '1' and tentativa > 4:
                for cores in dados_paises[sorteado]['bandeira']:
                    a = dados_paises[sorteado]['bandeira'][cores]
                    if a > 0 and cores != 'outras':
                        lista_cor.append(cores)
                aleatorio = random.choice(lista_cor)
                lista_cor.remove(aleatorio)
                string += '\n-Cores da Bandeira: {0}'.format(aleatorio)
                print('\nDistância:')
                for termo in lista:
                    print('\n{0} -> {1} km'.format(termo[0], int(termo[1])))
                print('\nDicas:')    
                print (string)
                tentativa -=4
            elif dica == '2':
                tentativa -= 3
            elif dica == '3' and tentativa >6:
                dic['Área'] = dados_paises[sorteado]['area']
                string += '\n-{0}: {1}'.format('Área', dic['Área'])
                tentativa -= 6
                print('\nDistância:')
                for termo in lista:
                    	print('\n{0} -> {1} km'.format(termo[0], int(termo[1])))
                print('\nDicas:')
                print(string)
            elif dica == '4' and tentativa >5:
                dic['População'] = dados_paises[sorteado]['populacao']
                string += '\n-População:{0}'.format(dic['População'])
                tentativa -= 5
                print('\nDistância:')
                for termo in lista:
                    print('\n{0} -> {1} km'.format(termo[0], int(termo[1])))
                print('\nDicas:')
                print(string)
            elif dica == '5' and tentativa > 7:
                dic['Continente'] = dados_paises[sorteado]['continente']
                string += '\n-Continente: {0}'.format(dic['Continente'])
                print('\nDistância:')
                for termo in lista:
                    print('\n{0} -> {1} km'.format(termo[0], int(termo[1])))
                print('\nDicas:')
                print(string)
                tentativa -= 7
            elif dica == '0':
                continue
                tentativa += 1
        elif palpite == 'inventario':
            print('\nDistância:')
            tentativa += 1
            for termo in lista:
                print('{0} -> {1} km'.format(termo[0], int(termo[1])))
            print('\nDicas:')
            if dic != {}:
                print(string)
            

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