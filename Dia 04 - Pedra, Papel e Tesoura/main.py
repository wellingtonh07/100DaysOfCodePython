import random


pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# colocando eles em uma lista para fácil acesso
escolha = [pedra, papel, tesoura]

#Serão somados com +1 depois de cada partida
#E a soma dos resultados dessas 3 variáveis serão para ser usadas como resultado de partidas_jogadas
vitoria_jogador = empate = vitoria_computador = 0

# validando o input(entrada do usuário)
opções = ['0', '1', '2']

print('-=' * 30)
print('{:>40}'.format('PEDRA, PAPEL E TESOURA'))
print('-=' * 30)

while True:
    while True:
        jogador = input('O que você escolhe? Aperte 0 para Pedra, 1 para Papel or 2 para Tesoura:\n>> ')
        if jogador not in opções:
            print('Opção inválida. Tente novamente...')
        else:
            break

    # Mudando o tipo de dado, de string para inteiro, tendo a certeza que a entrada do usuário(opção) é válida
    escolha_jogador = int(jogador)
    print(escolha[escolha_jogador])

    # Escolha do computador é um número inteiro aleatório(0, 1 ou 2)
    escolha_computador = random.randint(0, 2)
    print('Computador joga: ')
    print(f'>> {escolha[escolha_computador]}')

    # Calculando o resultado
    # Se for o mesmo, é um empate
    if escolha_jogador == escolha_computador:
        print('CARAMBA, EMPATOU')
        empate += 1
    # Casos onde o jogador vence: (Pedra esmaga Tesoura) ou (Papel encobre Pedra) ou (Tesoura corta Papel)
    elif (escolha_jogador == 0 and escolha_computador == 2) or\
            (escolha_jogador == 1 and escolha_computador == 0) or\
            (escolha_jogador == 2 and escolha_computador == 1):
        print('AÊÊÊÊ, VOCÊ VENCEU')
        vitoria_jogador += 1
    # Qualquer outra coisa além disso, vence o computador
    else:
        print('QUE PENA, VOCÊ PERDEU')
        vitoria_computador += 1
    #Para caso o usuário queira continuar jogando. Se a resposta for não, encerra o jogo
    resp = input('Você quer jogar de novo? [S/N] ').strip().upper()[0]
    print('-=' * 30)
    if resp == 'N':
        break
    elif resp not in 'S':
        print('Opção inválida, mas vou considerar como um SIM.')
        

print('Bom, já que não quer jogar mais, aqui vai os resultados de todas as partidas que você jogou.')
#Soma das estatísticas para pegar todas as partidas que o jogador jogou contra o computador
partidas_jogadas = vitoria_jogador + empate + vitoria_computador
print(f'Ao todo, foram {partidas_jogadas} partidas jogadas.')
print(f'Você venceu {vitoria_jogador} vezes, Parabéns!')
print(f'O jogo terminou empatado {empate} vezes. O computador te venceu {vitoria_computador} vezes.')
print('-=' * 30)
print('Encerrando jogo...')