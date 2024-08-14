def calcular_propina(total_cuenta, porcentaje_propina):
    propina = total_cuenta * (porcentaje_propina / 100)
    total_pagar = total_cuenta + propina
    return propina, total_pagar

# Ejemplo de uso
total_cuenta = float(input("Ingresa el total de la cuenta: "))
porcentaje_propina = float(input("Ingresa el porcentaje de propina que deseas dejar: "))
personas=int(input("Ingrese la cantidad de personas: "))
porPersona=total_cuenta/personas

propina, total_pagar = calcular_propina(total_cuenta, porcentaje_propina)
print(f"Debes dejar una propina de: ${propina:.2f}")
print(f"El total a pagar es: ${total_pagar:.2f}")
print(f"El total a pagar por persona es: ${porPersona:.2f}")

# CODIGO ORIGINAL
# def calcular_propina(total_cuenta, porcentaje_propina):
#     propina = total_cuenta * (porcentaje_propina / 100)
#     total_pagar = total_cuenta + propina
#     return propina, total_pagar

# # Ejemplo de uso
# total_cuenta = float(input("Ingresa el total de la cuenta: "))
# porcentaje_propina = float(input("Ingresa el porcentaje de propina que deseas dejar: "))

# propina, total_pagar = calcular_propina(total_cuenta, porcentaje_propina)
# print(f"Debes dejar una propina de: ${propina:.2f}")
# print(f"El total a pagar es: ${total_pagar:.2f}")