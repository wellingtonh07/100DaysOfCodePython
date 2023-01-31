#Para facilitar a gerar uma senha aleatória
import random
from time import sleep
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('-=' * 20)
print('Bem vindo ao PyPassword!')
print('O seu Gerador de Senhas em Python!')
print('-=' * 20)

nr_letters = int(input('Quantas letras você gostaria de ter em sua senha?\n>>> ')) 
nr_symbols = int(input(f'Quantos símbolos você gostaria de ter em sua senha?\n>>> '))
nr_numbers = int(input(f"Quantos números você gostaria de ter em sua senha?\n>>> "))

#Lista para armazenar uma senha aleatória
password_list = []

#Adicionando letras, símbolos e números aleatórios nessa lista
for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

#Para mostrar a senha fora da lista
password = ""
for char in password_list:
  password += char

print('Gerando uma senha em 3, 2, 1...')
print('-=' * 20)
#Espera 1 segundo antes de mostrar a senha
sleep(1)
print(f'Sua senha é:')
print(password)
print('-=' * 20)
print('Encerrando programa...')