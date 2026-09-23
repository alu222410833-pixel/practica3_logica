"""Actividad 2. Generador de tablas de verdad.

Recibe una expresion escrita con las funciones de conectivos.py
y la lista de variables que aparecen en ella, e imprime la tabla
completa generando las 2**n combinaciones con itertools.product.
"""
from itertools import product

from conectivos import (negacion, conjuncion, disyuncion, condicional,
                        bicondicional, disyuncion_exclusiva)

CONECTIVOS = {
    "negacion": negacion,
    "conjuncion": conjuncion,
    "disyuncion": disyuncion,
    "condicional": condicional,
    "bicondicional": bicondicional,
    "disyuncion_exclusiva": disyuncion_exclusiva,
}


def evaluar(expresion, contexto):
    """Evalua la expresion con los valores del contexto.

    Las funciones de conectivos se inyectan en el entorno para que
    las formulas puedan escribirse como 'condicional(p, q)'.
    Se desactivan los builtins para reducir la superficie de eval.
    """
    entorno = {**CONECTIVOS, **contexto}
    return eval(expresion, {"__builtins__": {}}, entorno)


def tabla_de_verdad(expresion, variables):
    encabezado = variables + [expresion]
    titulo = " | ".join(encabezado)
    print(titulo)
    print("-" * len(titulo))
    filas = []
    for valores in product([True, False], repeat=len(variables)):
        contexto = dict(zip(variables, valores))
        resultado = evaluar(expresion, contexto)
        filas.append(resultado)
        celdas = ["1" if v else "0" for v in (*valores, resultado)]
        print(" | ".join(celdas))
    return filas


if __name__ == "__main__":
    print("~(p ^ q)")
    tabla_de_verdad("negacion(conjuncion(p, q))", ["p", "q"])

    print("\n(p v q) -> r")
    tabla_de_verdad("condicional(disyuncion(p, q), r)", ["p", "q", "r"])

    print("\n(p <-> q) v ~r")
    tabla_de_verdad("disyuncion(bicondicional(p, q), negacion(r))",
                    ["p", "q", "r"])
