meses = {
    1: 'January', 
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

valor = int(input("Digite um valor entre 1 e 12: "))
if valor > 0 and valor < 12:
    print(meses[valor])
else:
    print("Número inválido")








tweet = input('Digite seu tweet: ')
if len(tweet) <= 280:
    print('Tweet postado')
else:
    print('Número de caracteres maior que o permitido')








idade = 18
peso = 60
horas_sono = 7

if idade < 16 and idade > 69:
    print("Sua idade não atende os requisitos")
elif peso < 50:
    print("Seu peso não atende os requisitos")
elif horas_sono < 6:
    print("Seu sono não atende os requisitos")
else:
    print("Seu perfil se encaixa nos requisitos")


if idade < 16 and idade > 69:
    if peso  > 50:
        if horas_sono > 6:
            print("Seu perfil não atende os requisitos")
else:
    print("Seu perfil se encaixa nos requisitos")
