num1 = int(input('Insira um número: '))

num2 = int(input('Insira outro número: '))

maior = num1 > num2

if num1 == num2:
    print('Os números são iguais.')
elif maior:
    print(num1, 'é o maoir número.')
else:
    print(num2, 'é o maoir número.')
