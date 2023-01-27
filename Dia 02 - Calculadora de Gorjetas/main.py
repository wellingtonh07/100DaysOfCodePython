print('Bem vindo a sua Calculadora de Gorjetas')
conta = float(input('Qual foi a conta total: R$ '))
porcentagem = int(input('Quanto seria a porcentagem de gorjeta que você quer dar? 10, 12, ou 15? '))
pessoas = int(input('Quantas pessoas para dividir a conta? '))
total = porcentagem / 100 * conta + conta
#Resultado com 2 casas decimais usando o :.2f
print(f'O total a pagar é: R${total:.2f}')