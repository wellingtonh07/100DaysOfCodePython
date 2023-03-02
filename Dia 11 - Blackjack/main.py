import random
#Feito no replit
from replit import clear

def deal_card():
  """Retorna uma carta aleatória do baralho."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """Pega numa lista de cartas e devolver a pontuação calculada a partir dos cartas"""

  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "Passou por cima. Perdeu 😤"


  if user_score == computer_score:
    return "Empatou 🙃"
  elif computer_score == 0:
    return "Perde, o adversário tem Blackjack 😱"
  elif user_score == 0:
    return "Ganhou com um Blackjack 😎"
  elif user_score > 21:
    return "Passou por cima. Perdeu 😭"
  elif computer_score > 21:
    return "O oponente passou por cima. Você ganhou 😁"
  elif user_score > computer_score:
    return "Você venceu 😃"
  else:
    return "Você perdeu 😤"

def play_game():

  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   As suas cartas: {user_cards}, pontuação atual: {user_score}")
    print(f"   A primeira carta do computador: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Digite 's' para obter outra carta, digite 'n' para passar: ")
      if user_should_deal == "s":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"   A sua mão final: {user_cards}, pontuação final: {user_score}")
  print(f"   Mão final do computador: {computer_cards}, pontuação final: {computer_score}")
  print(compare(user_score, computer_score))

while input("Quer jogar um jogo de Blackjack? Escreva 's' ou 'n'.: ") == "s":
  clear()
  play_game()