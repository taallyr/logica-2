
velocidade = float(input("Digite a velocidade em km/h: "))
limite = 80

if velocidade > limite:
    excesso = velocidade - limite
    multa= excesso * 50

    print("limite = 80 km/h")
    print(f"exedeu {excesso}km/h")
    print(f"multa = {excesso}km/h * R$50,00")
    print(f" valo da multa: R$ {multa:.2f}")

else:
    print("Você está dentro do limite. Sem multa")