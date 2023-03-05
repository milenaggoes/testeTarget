faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

valor_total_mensal = sum(faturamento.values())


percentuais= {}
for estado, faturamento in faturamento.items():
    percentuais[estado] = faturamento / valor_total_mensal * 100


for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
