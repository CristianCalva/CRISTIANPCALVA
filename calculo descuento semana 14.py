def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicando el porcentaje al monto total de la compra.

    Parámetros:
        monto_total (float): Monto total de la compra.
        porcentaje_descuento (float): Porcentaje de descuento a aplicar (por defecto 10%).

    Retorna:
        float: Monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Llamadas a la función calcular_descuento
monto_compra_1 = 200
porcentaje_descuento_1= 10
descuento_1 = calcular_descuento(monto_compra_1)
monto_final_1 = monto_compra_1 - descuento_1

monto_compra_2 = 400
porcentaje_descuento_2 = 20
descuento_2 = calcular_descuento(monto_compra_2, porcentaje_descuento_2)
monto_final_2 = monto_compra_2 - descuento_2

# Resultados
print("Resultado 1:")
print(f"Monto de la compra: ${monto_compra_1}")
print(f"porcentaje de descuento: {porcentaje_descuento_1}%")
print(f"Descuento aplicado: ${descuento_1}")
print(f"Monto final a pagar: ${monto_final_1}\n")

print("Resultado 2:")
print(f"Monto de la compra: ${monto_compra_2}")
print(f"Porcentaje de descuento: {porcentaje_descuento_2}%")
print(f"Descuento aplicado: ${descuento_2}")
print(f"Monto final a pagar: ${monto_final_2}")