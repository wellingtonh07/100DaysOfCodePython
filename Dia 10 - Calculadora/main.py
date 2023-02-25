#Feito no replit
from replit import clear

#Funções das operações
def somar(n1, n2):
  return n1 + n2

def subtrair(n1, n2):
  return n1 - n2

def multiplicar(n1, n2):
  return n1 * n2

def dividir(n1, n2):
  return n1 / n2

#Dicionário com os sinais e o nome das operações
operações = {
  "+": somar,
  "-": subtrair,
  "*": multiplicar,
  "/": dividir
}

#Função calculadora
def calculadora():

  num1 = float(input('Digite o primeiro número:\n>>> '))
  for símbolo in operações:
    print(símbolo)
  deve_continuar = True
 
  while deve_continuar:
    símbolo_operação = input('Que operação você quer fazer?\n>>> ')
    num2 = float(input('Digite o próximo número:\n>>> '))
    função_calculadora = operações[símbolo_operação]
    resposta = função_calculadora(num1, num2)
    print(f"{num1} {símbolo_operação} {num2} = {resposta}")

    if input(f"Digite 's' para continuar calculando com a {resposta}, ou aperte 'n' para começar uma nova conta ") == 's'.lower():
      num1 = resposta
    else:
      deve_continuar = False
      clear()
      calculadora()

calculadora()
