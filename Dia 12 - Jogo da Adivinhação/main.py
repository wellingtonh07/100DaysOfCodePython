from random import randint

#Definindo os turnos do nivel fácil e difícil
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Função para checar a resposta do usuário
def check_answer(guess, answer, turns):
  """Se o usuário errar, diminui o número de tentativas."""
  if guess > answer:
    print("Menos...")
    return turns - 1
  elif guess < answer:
    print("Mais...")
    return turns - 1
  else:
    print(f"Você conseguiu! A resposta é {answer}.")

#Função para definir a dificuldade do jogo.
def set_difficulty():
  level = input("Escolha uma dificuldade, fácil ou difícil [f/f] ")
  if level == "f".lower():
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  #escolhendo um número entre 0 e 100.
  print("Bem vindo ao jogo da adivinhação")
  print("Estou pensando em um número entre 0 e 100, tente adivinhar...")
  answer = randint(1, 100)
  print(f"Opsss, a resposta correta é: {answer}") 

  turns = set_difficulty()
  #Repete a funcionalidade de adivinhação se errar.
  guess = 0
  while guess != answer:
    print(f"Você tem {turns} tentativas restantes para adivinhar o número.")

    #Faz o usuário adivinhar o número.
    guess = int(input("Manda um palpite ai: "))

    #Acompanha os turnos e reduz em -1 se errar.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("Seus palpites acabaram, você perdeu.")
      return
    elif guess != answer:
      print("Tente de novo.")


game()
