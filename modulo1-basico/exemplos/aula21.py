"""
imprecisão dos numeros de ponto flutuante + round e decimal.Decimal
"""

numero_1 = 0.1
numero_2 = 0.7

numero_3 = numero_1 + numero_2

print(f'{numero_3:.2f}')
print(round(numero_3, 3))