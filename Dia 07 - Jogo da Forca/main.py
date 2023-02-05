import random
from palavras_times_futebol import times

#Sorteando um time aleatório e pegando a quantidade de letras desse time
time_escolhido = random.choice(times)
tamanho_palavra = len(time_escolhido)

#Para colocar no loop depois, em caso de vitória se torna True
#Em caso de derrota também, mas com as vidas chegando em 0
fim_do_jogo = False
vidas = 6

print('-=' * 20)
print('{:>25}'.format('JOGO DA FORCA'))
print('-=' * 20 )

print('Versão - Brasileirão 2023!')
print('Você tem que adivinhar o nome de um time da Série A do Brasileirão 2023.')
print('Será que você consegue? Você tem 6 vidas.\n')

#Criando os espaços em branco
lista = []
#Para cada letra do tamanho de letras do time escolhido, faz um _
for _ in range(tamanho_palavra):
    lista += "_"

#Enquanto não for o fim do jogo
while not fim_do_jogo:
    adivinha = input('Adivinhe uma letra: ').lower()

    #Se o usuário já tiver dito a letra, deixar isso claro e mostrar a letra
    if adivinha in lista:
        print(f'Você já digitou essa letra {adivinha}')

    #Checando a letra escolhida
    for posição in range(tamanho_palavra):
        letra = time_escolhido[posição]
        #Se a letra escolhida estiver na palavra, coloca ela na posição certa, substituindo o _
        if letra == adivinha:
            lista[posição] = letra

    #Checando se o usuário está errado.
    if adivinha not in time_escolhido:
        #Se a letra não está na palavra, deixar isso claro e mostrar a letra que foi digitada
        print(f'Você digitou a letra {adivinha}, que não está na palavra. Você perdeu uma vida.\n')
        #Se ele errou, tira uma vida. Com 0 vidas, é fim de jogo
        vidas -= 1
        if vidas == 0:
            fim_do_jogo = True
            print('Você perdeu!')
            print(f'O time escolhido foi o {time_escolhido}.')

    #Juntando todos os elementos da lista e formando a palavra
    print(f"{' '.join(lista)}\n")

    #Verificando se o usuário já tem todas as letras.
    #Se não tiver mais o _ em branco, o jogo acabou e o usuário venceu.
    if "_" not in lista:
        fim_do_jogo = True
        print('Você ganhou!')
        print(f'O time escolhido foi o {time_escolhido}.')

    #Importando o desenho da forca 
    from desenho_forca import forca
    print(forca[vidas])