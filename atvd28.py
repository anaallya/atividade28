# Exercício Python 28 : Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
numero = [ ]
for l in range (0, 7):
    ADN = int(input(" digite o ADN"))
    if ADN <=2005:
        print("maioridade")
    else:
        print("ainda nao atingiu")