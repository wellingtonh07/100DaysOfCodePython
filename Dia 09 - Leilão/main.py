#Foi feito no replit
from replit import clear

print('-=' * 20)
print('{:>25}'.format('LEILÃO'))
print('-=' * 20)

lances = {}
lances_acabados = False

def lance_mais_alto(registro_lances):
  maior_lance = 0
  vencedor = ""
  for concorrente in registro_lances:
    montante_oferta = registro_lances[concorrente]
    if montante_oferta > maior_lance: 
      maior_lance = montante_oferta
      vencedor = concorrente
  print(f'O vencedor é {vencedor} com um lance de R${maior_lance}. Parabéns')

while not lances_acabados:
  nome = input('Digite seu nome: ')
  preço = int(input('De quanto é o seu lance? R$ '))
  lances[nome] = preço
  deve_continuar = input('Existem outros concorrentes? [S/N]\n').upper()[0]
  if deve_continuar == 'N':
    lances_acabados = True
    lance_mais_alto(lances)
  elif deve_continuar == 'S':
    clear()
  