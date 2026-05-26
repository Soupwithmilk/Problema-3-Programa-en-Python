# Problema-3-Programa-en-Python
Auditoría de Inventario y Reabastecimiento

Programa desarrollado en Python para resolver una problemática relacionada con el control de inventario y el reabastecimiento de artículos.

El programa permite registrar productos, verificar si el stock actual es suficiente y calcular automáticamente la cantidad exacta que debe solicitarse.

Conceptos utilizados
Matrices
Funciones
Ciclos for
Estructuras condicionales
Variables y constantes
Explicación breve
POS_CODIGO = 0
POS_NOMBRE = 1

Estas constantes permiten identificar la posición de cada dato dentro de la matriz y hacen que el código sea más organizado y fácil de entender.

def calcular_cantidad_pedir(stock_actual, stock_minimo):

Se crea una función encargada de calcular la cantidad exacta de productos que deben solicitarse.

if stock_actual < stock_minimo:

Esta condición verifica si el stock actual es menor al stock mínimo requerido.

cantidad_pedir = stock_minimo - stock_actual

Si el stock es insuficiente, se calcula la diferencia entre ambos valores.

for articulo in inventario:

Este ciclo permite recorrer todos los artículos almacenados en la matriz.

print(f"Cantidad a pedir: {cantidad_pedir}")

Muestra en pantalla la cantidad de productos que deben ser solicitados.
