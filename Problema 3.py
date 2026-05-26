
# Nombre del estudiante: Yordy Montesino Castro 
# Grupo: 213022_160 
# Programa: Ingeniería de telecomunicaciones 
# Código Fuente: Autoría propia 

# =========================================================
# AUDITORÍA DE INVENTARIO Y REABASTECIMIENTO
# =========================================================


# =========================================================
# CONSTANTES
# =========================================================

POS_CODIGO = 0
POS_NOMBRE = 1
POS_STOCK_ACTUAL = 2
POS_STOCK_MINIMO = 3

CANTIDAD_ARTICULOS = 5


# =========================================================
# FUNCIÓN PARA CALCULAR LA CANTIDAD A PEDIR
# =========================================================

def calcular_cantidad_pedir(stock_actual, stock_minimo):

    if stock_actual < stock_minimo:
        cantidad_pedir = stock_minimo - stock_actual
    else:
        cantidad_pedir = 0

    return cantidad_pedir


# =========================================================
# MATRIZ DE INVENTARIO
# =========================================================

inventario = []

print("=" * 40)
print(" REGISTRO DE ARTÍCULOS ")
print("=" * 40)


# Registro de artículos

for i in range(CANTIDAD_ARTICULOS):

    print(f"\nArtículo #{i + 1}")

    codigo = input("Ingrese el código del artículo: ")
    nombre = input("Ingrese el nombre del artículo: ")
    stock_actual = int(input("Ingrese el stock actual: "))
    stock_minimo = int(input("Ingrese el stock mínimo requerido: "))

    articulo = [
        codigo,
        nombre,
        stock_actual,
        stock_minimo
    ]

    inventario.append(articulo)


# =========================================================
# REPORTE FINAL
# =========================================================

print("\n" + "=" * 40)
print(" REPORTE DE REABASTECIMIENTO ")
print("=" * 40)

for articulo in inventario:

    codigo_articulo = articulo[POS_CODIGO]
    nombre_articulo = articulo[POS_NOMBRE]
    stock_actual = articulo[POS_STOCK_ACTUAL]
    stock_minimo = articulo[POS_STOCK_MINIMO]

    cantidad_pedir = calcular_cantidad_pedir(
        stock_actual,
        stock_minimo
    )

    print(f"\nArtículo: {nombre_articulo}")
    print(f"Cantidad a pedir: {cantidad_pedir}")
    print("-" * 40)