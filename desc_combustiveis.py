litros = float(input("Digite a quantidade de litros: "))
tipo = input("Digite o tipo de combustível (A ou G): ")

if tipo == "A" or tipo == "a":
    preco = 2.89
    if litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05

elif tipo == "G" or tipo == "g":
    preco = 4.95
    if litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06

else:
    print("Tipo inválido!")
    preco = 0
    desconto = 0

valor = litros * preco
valor_final = valor - (valor * desconto)

print(f"Valor a pagar: R$ {valor_final:.2f}")