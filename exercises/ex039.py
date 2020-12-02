from datetime import date
atual = date.today().year

print('=' * 5, 'ALISTAMENTO MILITAR', '=' * 5 )

nascimento = int(input('Em que ano você nasceu? '))

idade = atual - nascimento

if idade < 18: 
    print(f'Você ainda vai se alistar, faltam {18 - idade} ano(s).')
    print(f'Ano de alistamento: {nascimento + 18}, com 18 anos.')

elif idade == 18:
    print('Você deve se alistar este ano.')
    print(f'Ano de alistamento: {nascimento + 18}, com 18 anos.')

else:
    print(f'Você já deveria ter se alistado, está {idade - 18} ano(s) atrasado.')
    print(f'Ano de alistamento: {nascimento + 18}, com 18 anos.')
    