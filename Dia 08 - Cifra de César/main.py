alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Função para decodificar o texto
def caesar(começo_texto, deslocamento, direção_cifra):
  novo_texto = ''
  if direção_cifra == 'decodificar':
    deslocamento *= -1
  #Para cada caractere no texto
  for c in começo_texto:
    #Se a letra tiver no alfabeto, descobre a posição
    # e soma o número da posição da letra, com o número do deslocamento.
    if c in alfabeto:
      posição = alfabeto.index(c)
      nova_posição = posição + deslocamento
      novo_texto += alfabeto[nova_posição]
    #Para mostrar o texto, seja ele decodificado ou codificado
    else:
      novo_texto += c
  print(f'\nAqui está o resultado de {direção_cifra}: {novo_texto}')

#Programa principal
print('-=' * 20)
print('{:>25}'.format('CIFRA DE CÉSAR'))
print('-=' * 20)
acabou = False
while not acabou:
  direção = input("\nDigite 'codificar' para criptografar, ou digite 'decodificar' para descriptografar:\n").lower()
  texto = input('\nEscreva sua mensagem:\n').lower()
  mudança_deslocamento = int(input('\nDigite o número para deslocarmos sua mensagem:\n'))

  #Evitando erro caso a escolha do usuário nessa variável passe de 26.
  mudança_deslocamento = mudança_deslocamento % 26

  #Chamando a função
  caesar(começo_texto=texto, deslocamento=mudança_deslocamento, direção_cifra=direção)

  reiniciar = input("\nDigite 's' se você quer ir de novo. Caso contrário, digite 'n'.\n").lower()[0]
  if reiniciar == 'n':
    acabou = True
    print('\nEncerrando programa...')
