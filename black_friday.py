preco = float(input("Digite o preço total da venda: "))

print("Forma de pagamento:")
print("1 - À vista (10% de desconto)")
print("2 - Débito (5% de desconto)")
print("3 - Crédito (3% de desconto)")
print("4 - PIX (7.5% de desconto)")

opcao = int(input("Escolha a forma de pagamento: "))

if opcao == 1:
    desconto = 10
elif opcao == 2:
    desconto = 5
elif opcao == 3:
    desconto = 3
elif opcao == 4:
    desconto = 7.5
else:
    desconto = 0
    print("Opção inválida!")

valor_final = preco - (preco * desconto / 100)

print(f"Valor final a pagar: R$ {valor_final:.2f}")