
# ===== PRUEBA AUDITORÍA DE INVENTARIO Y REABASTECIMIENTO =====


# ===== CONSTANTES =====

POS_CODIGO = 0
POS_NOMBRE = 1
POS_STOCK_ACTUAL = 2
POS_STOCK_MINIMO = 3


# ===== MATRIZ DE INVENTARIO =====
# [Código, Nombre, Stock Actual, Stock Mínimo]

inventario = [
    ["A101", "Teclado", 5, 10],
    ["A102", "Mouse", 12, 10],
    ["A103", "Monitor", 3, 8],
    ["A104", "Memoria USB", 20, 15],
    ["A105", "Audifonos", 2, 6]
]


# ===== FUNCIÓN PARA CALCULAR LA CANTIDAD A PEDIR =====

def calcular_cantidad_pedir(stock_actual, stock_minimo):

    if stock_actual < stock_minimo:
        cantidad_pedir = stock_minimo - stock_actual
    else:
        cantidad_pedir = 0

    return cantidad_pedir


# ===== REPORTE DE REABASTECIMIENTO =====

print("=" * 50)
print("      REPORTE DE REABASTECIMIENTO")
print("=" * 50)

for articulo in inventario:

    codigo_articulo = articulo[POS_CODIGO]
    nombre_articulo = articulo[POS_NOMBRE]
    stock_actual = articulo[POS_STOCK_ACTUAL]
    stock_minimo = articulo[POS_STOCK_MINIMO]

    cantidad_pedir = calcular_cantidad_pedir(
        stock_actual,
        stock_minimo
    )

    print("\n" + "-" * 50)
    print(f"Código: {codigo_articulo}")
    print(f"Artículo: {nombre_articulo}")
    print(f"Stock actual: {stock_actual}")
    print(f"Stock mínimo: {stock_minimo}")
    print(f"Cantidad a pedir: {cantidad_pedir}")
    print("-" * 50)