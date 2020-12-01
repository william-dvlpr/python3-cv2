valor = int(input('Qual o valor da casa que você deseja comprar? '))
salario =  int(input('Seu salário mensal é de: R$'))
tempo = int(input('Em quantos anos deseja pagar?'))

parcela = (valor / tempo) / 12

if parcela <= salario * 0.3:
    print(f'Tudo ok, suas parcelas ficaram em: R${parcela:.2f}')
else:
    print(f'Sinto muito, as parcelas ficam de R${parcela:.2f} ultrapassam 30% do seu salário atual')
