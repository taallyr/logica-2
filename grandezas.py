print("******************************")
print("CÁLCULO DE GRANDEZAS ELÉTRICAS")
print("******************************")
print("1. Tensão (em Volt)")
print("2. Resistência (em Ohm)")
print("3. Corrente (em Ampére)")
print("4. Sair do programa")
print("******************************")

opcao = int(input("Qual grandeza deseja calcular? "))

if opcao == 1:
    R = float(input("Digite a Resistência (Ohm): "))
    I = float(input("Digite a Corrente (Ampére): "))
    U = R * I
    print(f"Tensão (U) = {U}")

elif opcao == 2:
    U = float(input("Digite a Tensão (Volt): "))
    I = float(input("Digite a Corrente (Ampére): "))
    R = U / I
    print(f"Resistência (R) = {R}")

elif opcao == 3:
    U = float(input("Digite a Tensão (Volt): "))
    R = float(input("Digite a Resistência (Ohm): "))
    I = U / R
    print(f"Corrente (I) = {I}")

elif opcao == 4:
    print("Programa encerrado")

else:
    print("Opção inválida!")