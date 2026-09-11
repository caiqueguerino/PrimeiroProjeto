# Aqui o Cliente irá informar o valor pago na compra
print("Insira o valor da compra:")
valor_compra = float(input( ))

# Aqui será calculado os valores do desconto

if valor_compra < 200.00:
    desconto = valor_compra * (5 / 100)
    print("Você teve um desconto de 5%")
    
elif valor_compra >= 200.00 and valor_compra < 300.00:
    desconto = valor_compra * (10 / 100)
    print("Você teve um desconto de 10%")

else:
    desconto = valor_compra * (15 / 100)
    print("Você teve um desconto de 15%")

# Depois calculado o sistema irá informar a porcentagem do desconto
# E por fim irá retornar com o valor sobre o desconto

print(f"Total da compra: R${(valor_compra - desconto):.2f}")