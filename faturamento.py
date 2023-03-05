import json

with open('dados.json', 'r') as file:
    faturamento = json.load(file)

faturamento = [dia['valor'] for dia in faturamento if dia['valor'] != 0]

menor_valor = min(faturamento)
maior_valor = max(faturamento)

media_mensal = sum(faturamento) / len(faturamento)
dias_acima_da_media = sum(1 for valor in faturamento if valor > media_mensal)


print("Menor valor de faturamento diário:", menor_valor)
print("Maior valor de faturamento diário:", maior_valor)
print("Número de dias no mês com faturamento acima da média:", dias_acima_da_media)

