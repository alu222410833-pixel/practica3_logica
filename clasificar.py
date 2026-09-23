"""Actividad 3. Clasificacion de formulas.

Segun la ultima columna de su tabla de verdad, una formula es
tautologia (siempre 1), contradiccion (siempre 0) o contingencia
(mezcla de ambos).
"""
from tabla import tabla_de_verdad


def clasificar(resultados):
    if all(resultados):
        return "tautologia"
    if not any(resultados):
        return "contradiccion"
    return "contingencia"


FORMULAS = [
    ("p ^ ~p",
     "conjuncion(p, negacion(p))", ["p"]),
    ("p v ~p",
     "disyuncion(p, negacion(p))", ["p"]),
    ("((p -> q) ^ (q -> r)) -> (p -> r)",
     "condicional(conjuncion(condicional(p, q), condicional(q, r)), "
     "condicional(p, r))",
     ["p", "q", "r"]),
    ("(p -> q) -> (q -> p)",
     "condicional(condicional(p, q), condicional(q, p))", ["p", "q"]),
]

if __name__ == "__main__":
    for nombre, expr, variables in FORMULAS:
        print(f"\n{nombre}")
        resultados = tabla_de_verdad(expr, variables)
        print("->", clasificar(resultados))
