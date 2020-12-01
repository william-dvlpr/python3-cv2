
numero = int(input('Insira o número: '))

base = int(input('Para qual base você deseja converter:\n[1] Binário\n[2] Octal\n[3] Hexadecimal\n\nOpção:'))

if base == 1:
    print(f'{numero} em binário: {bin(numero)[2:]}')
elif base == 2:
    print(f'{numero} em octal: {oct(numero)[2:]}')
elif base == 3:
    print(f'{numero} em hexadecimal: {hex(numero)[2:]}')
else:
    print('Parece que você digitou um número que não corresponde a nenhuma das opções')
