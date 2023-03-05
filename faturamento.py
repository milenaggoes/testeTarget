import json

with open('faturamento.json', 'r') as arquivo:

    dados = json.load(arquivo)

dados = [valor for valor in dados if valor > 0]

menor_faturamento = min(dados)
maior_faturamento = max(dados)
total_dias = len(dados)
media_mensal = sum(dados) / total_dias

dias_media = len([valor for valor in dados if valor > media_mensal])

print(f"Menor valor de faturamento: R$ {menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R$ {maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_media}")
