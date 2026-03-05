print('Calcular IMC')

idade = input('Qual a sua idade ')
altura = input('Qual a sua altura ')
peso = input('Qual a seu peso ')


imc = peso/(altura*2)
print(f'seu imc é {imc}')



if idade % 7 == 0:
    print(f'sua idade de {idade} anos é divisivel por 7')
else:
    print(f'sua idade de {idade} anos não é divisivel por 7')

