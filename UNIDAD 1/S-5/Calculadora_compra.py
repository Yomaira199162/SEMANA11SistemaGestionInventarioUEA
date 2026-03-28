"""
Programa: Calculadora de Precio Final
Descripción: Este programa calcula el costo total de un producto aplicando
un porcentaje de impuesto y un descuento fijo.
"""


def calcular_precio_final(precio_base, tasa_impuesto, descuento):
    # Cálculo del impuesto (float)
    monto_impuesto = precio_base * tasa_impuesto

    # Cálculo del precio antes de descuento
    precio_con_impuesto = precio_base + monto_impuesto

    # Aplicar descuento fijo (integer o float)
    precio_final = precio_con_impuesto - descuento

    return precio_final


# --- Variables con diferentes tipos de datos ---
nombre_producto = "Monitor Gamer 24\""  # string
precio_inicial = 250.00  # float
cantidad_unidades = 2  # integer
tiene_envio_gratis = True  # boolean
impuesto_iva = 0.15  # float (15%)
descuento_promocional = 10  # integer

# Lógica del programa
costo_total_base = precio_inicial * cantidad_unidades
resultado = calcular_precio_final(costo_total_base, impuesto_iva, descuento_promocional)

# Salida de datos
print(f"--- Recibo de: {nombre_producto} ---")
print(f"Precio base total: ${costo_total_base}")
print(f"¿Incluye envío gratis?: {tiene_envio_gratis}")
print(f"El precio final a pagar es: ${resultado}")
