"""Actividad 4. Comprobacion de equivalencias logicas.

Dos formulas son equivalentes cuando sus columnas finales coinciden
linea por linea para todas las combinaciones de valores.
"""
from itertools import product

from tabla import evaluar

LEYES = [
    ("De Morgan (1)",
     "negacion(conjuncion(p, q))",
     "disyuncion(negacion(p), negacion(q))", ["p", "q"]),
    ("De Morgan (2)",
     "negacion(disyuncion(p, q))",
     "conjuncion(negacion(p), negacion(q))", ["p", "q"]),
    ("Implicacion material",
     "condicional(p, q)",
     "disyuncion(negacion(p), q)", ["p", "q"]),
    ("Contrapositiva",
     "condicional(p, q)",
     "condicional(negacion(q), negacion(p))", ["p", "q"]),
    ("Distributiva",
     "conjuncion(p, disyuncion(q, r))",
     "disyuncion(conjuncion(p, q), conjuncion(p, r))", ["p", "q", "r"]),
    ("Doble negacion",
     "negacion(negacion(p))",
     "p", ["p"]),
    # Caso negativo: la reciproca NO es equivalente al condicional
    ("Caso negativo (reciproca)",
     "condicional(p, q)",
     "condicional(q, p)", ["p", "q"]),
]


def evaluar_todas(expresion, variables):
    """Devuelve la lista de resultados sin imprimir la tabla."""
    resultados = []
    for valores in product([True, False], repeat=len(variables)):
        contexto = dict(zip(variables, valores))
        resultados.append(evaluar(expresion, contexto))
    return resultados


def son_equivalentes(expr1, expr2, variables):
    return evaluar_todas(expr1, variables) == evaluar_todas(expr2, variables)


if __name__ == "__main__":
    print(f"{'Ley':<28} | Equivalentes")
    print("-" * 42)
    for nombre, a, b, variables in LEYES:
        print(f"{nombre:<28} | {son_equivalentes(a, b, variables)}")
