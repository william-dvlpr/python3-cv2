idade = int(input('Qual a sua idade? '))

print('Sua categoria é', end=' ')

if idade <= 9 :
    print('Mirim.')
elif idade <= 14 :
    print('Infantil.')
elif idade <= 19 :
    print('Junior.')
elif idade <= 20 :
    print('Sênior.')
else:
    print('Master.')