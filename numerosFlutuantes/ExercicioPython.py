print('Exercicio')

idade = int(input('Qual a sua idade? '))
altura = (input('Qual a sua altura? (Digite 3 digitos ex: 180) '))
peso = int(input('Qual a seu peso? '))

ano = 2025 - idade

if len(altura) == 3:
  altura = int(altura)/100
  imc = peso/(altura * altura)
  print(f'Seu IMC é {imc:.2f}')
else:
  print('Na altura, digite apenas 3 números')

if idade % 7 == 0:
  print('Sua idade é divisível por 7')
else:
  print('Sua idade não é divisível por 7')


if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é ano bissexto")
else:
    print(f"{ano} não é ano bissexto")
