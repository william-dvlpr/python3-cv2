from datetime import date
atual = date.today().year

print('=' * 5, 'ALISTAMENTO MILITAR', '=' * 5 )

nascimento = int(input('Em que ano você nasceu? '))

if (atual - nascimento) < 18: # '( )' redundante, p/ facilitar leitura
    print('Você ainda vai se alistar.')
    print(f'Ano de alistamento: {nascimento + 18}, com 18 anos.')

elif (atual - nascimento) == 18:
    print('Você deve se alistar este ano.')
    print(f'Ano de alistamento: {nascimento + 18}, com 18 anos.')

else:
    print('Você já deveria ter se alistado.')
    print(f'Ano de alistamento: {nascimento + 18}, com 18 anos')
