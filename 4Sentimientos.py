palabras_positivas = {"bien":1, "genial":3, "fantástico":3, "excelente":3, "feliz":3}
palabras_negativas = {"mal":2, "terrible":3, "horrible":4, "malo":3, "triste":1}

def analizar_sentimiento(texto):
    texto = texto.lower()
    conteo_positivo = sum(palabras_positivas.get(palabra, 0) for palabra in texto.split())
    conteo_negativo = sum(palabras_negativas.get(palabra, 0) for palabra in texto.split())
    print(conteo_positivo)
    print(conteo_negativo)


    if conteo_positivo > conteo_negativo:
        return "Sentimiento positivo"
    elif conteo_negativo > conteo_positivo:
        return "Sentimiento negativo"
    else:
        return "Sentimiento neutral"

# Ejemplo de uso
texto = input("Escribe una oración para analizar: ")
resultado = analizar_sentimiento(texto)
print(f"El resultado del análisis es: {resultado}")

# CODIGO ORIGINAL
# palabras_positivas = ["bien", "genial", "fantástico", "excelente", "feliz"]
# palabras_negativas = ["mal", "terrible", "horrible", "malo", "triste"]

# def analizar_sentimiento(texto):
#     texto = texto.lower()
#     conteo_positivo = sum(palabra in texto for palabra in palabras_positivas)
#     conteo_negativo = sum(palabra in texto for palabra in palabras_negativas)

#     if conteo_positivo > conteo_negativo:
#         return "Sentimiento positivo"
#     elif conteo_negativo > conteo_positivo:
#         return "Sentimiento negativo"
#     else:
#         return "Sentimiento neutral"

# # Ejemplo de uso
# texto = input("Escribe una oración para analizar: ")
# resultado = analizar_sentimiento(texto)
# print(f"El resultado del análisis es: {resultado}")