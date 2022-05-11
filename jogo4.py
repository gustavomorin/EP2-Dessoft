from funcoes import *
from jogo2 import *

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

while palpite.lower() != 'desisto':

    dados_paises = normaliza(dados)
    sorteado = sorteia_pais(dados_paises)
    print(sorteado)
    lista = []

    for tentativa in range(20,0, -1):
        print('Um país foi escolhido, tente advinhar!')
        print('Você tem {0} tentativa(s)'.format(tentativa))
        palpite = input('\nQual o seu palpite?')
        palpite = palpite.lower()
        
        if palpite == sorteado:
            print('\n*** Parabéns! Você ganhou após {0} tentativa(s)!'.format(21 - tentativa))
            break
        
        elif palpite == 'desisto':
            print('Que deselegante desistir, o pais era: {0}'.format(sorteado))
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
        
        if palpite in dados_paises.keys():
            lista = adiciona_em_ordem(palpite, distancias, lista)
            
        print('\nDistância:')

        for termo in lista:
                print('{0} -> {1} km'.format(termo[0], int(termo[1])))
    
        if palpite not in dados_paises.keys():
            print('\nPaís desconhecido')
    
    jogar_novamente = input('Jogar novamente? [s/n]')
    if jogar_novamente == 's':
        continue
    else:
        print('Até a próxima!')
        break