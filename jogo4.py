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

while palpite != 'desisto':

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
        print('\nDicas:')
        if palpite == 'dica':
            print('----------------------------------------')
            print('1. Cor da Bandeira  - custa 4 tentativas')
            print('2. Letra da capital - custa 3 tentativas')
            print('3. Área             - custa 6 tentativas')
            print('4. População        - custa 5 tentativas')
            print('5. Continente       - custa 7 tentativas')
            print('0. Sem dica                             ')
            print('----------------------------------------')
            dica = ''
            while dica != '0' and dica != '1' and dica != '2' and dica != '3' and dica != '4' and dica != '5' :
                dica = input('Escolha a sua opção [0|1|2|3|4|5]:')
                if dica == '0' and dica == '1' and dica == '2' and dica == '3' and dica == '4' and dica == '5' :
                    break
                print('Opção inválida')
            if dica == '0':
                print('sem dica')
                tentativa += 2
            elif dica == '1':
                print(2)
                tentativa -=4
            elif dica == '2':
                tentativa -= 3
            elif dica == '3':
                tentativa -= 6
            elif dica == '4':
                tentativa -= 5
            elif dica == '5':
                tentativa -= 7
        elif palpite == 'inventario':
            print('\nDistância:')
            tentativa += 1
            for termo in lista:
                print('{0} -> {1} km'.format(termo[0], int(termo[1])))

        elif palpite not in dados_paises.keys():
            print('\nPaís desconhecido')
    
    jogar_novamente = input('Jogar novamente? [s/n]')
    palpite = ""
    if jogar_novamente != 's':
        palpita = ""
        print('Até a próxima!')
        break