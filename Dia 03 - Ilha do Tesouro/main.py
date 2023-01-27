print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem vindos a Ilha do Tesouro")
print("Sua missão é encontrar o tesouro.") 

#lower() - Deixa as letras minúsculas
while True:
  direção = input('Você está em uma encruzilhada, para onde você quer ir? Direita ou Esquerda? ').lower()
  if direção == 'esquerda':
    decisão = input('Nadar ou Esperar? ').lower()
    if decisão == 'esperar':
      porta = input('Qual porta você escolhe? Vermelho, Azul ou Amarelo? ').lower()
      if porta == 'amarelo':
        print('Você encontrou o tesouro! Você venceu!!!')
      elif porta == 'vermelho':
        print('Você foi queimado pelo fogo. Game Over!')
      elif porta == 'azul':
        print('Você foi comido por feras. Game Over!')
      else:
        print('Game Over!')
    #Caso o usuário escolha nadar ou qualquer outra coisa
    else:
      print('Você foi atacado por uma truta feroz. Game Over!')
  #Caso o usuário escolha a direção direita ou qualquer outra coisa
  else:
    print('Você caiu em um buraco. Game Over!')
  #[0] - Pega só a primeira letra
  resposta = input('Quer jogar de novo? ')[0]
  if resposta in 'Nn':
    break

print('Encerrando jogo...')