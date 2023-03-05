texto = "Target"
lista_caracteres = list(texto)

for i in range (len(lista_caracteres) // 2):
    j = len (lista_caracteres) - i - 1
    lista_caracteres[i], lista_caracteres[j] = lista_caracteres[j], lista_caracteres[i]


texto_invertido = ""
for caractere in lista_caracteres:
    texto_invertido += caractere

print(texto_invertido)
