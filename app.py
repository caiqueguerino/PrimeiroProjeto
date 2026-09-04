# Programa de cálculo de consumo energético
# Autor: caique william de maria guerino

# dados de entrada
aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho em watts (W): "))
tempo = float(input("Digite o tempo médio de uso diário em horas: "))

# Calculo mensal
consumoMensal = (potencia * tempo * 30) / 1000

# Valor fixo
valor_kWh = 0.75

# Calculo do custo estimado
custoEstimado = consumoMensal * valor_kWh

# Resultado
print(f"Aparelho: {aparelho}")
print(f"Consumo mensal: {consumoMensal:.2f} kWh")
print(f"Custo estimado: R$ {custoEstimado:.2f}")