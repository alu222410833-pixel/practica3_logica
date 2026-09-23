"""Actividad 5. Validez de argumentos.

Un argumento es valido si NO existe ninguna linea donde todas las
premisas sean verdaderas y la conclusion falsa. Si esa linea existe,
la funcion la imprime como contraejemplo.
"""
from itertools import product

from tabla import evaluar


def es_valido(premisas, conclusion, variables):
    for valores in product([True, False], repeat=len(variables)):
        contexto = dict(zip(variables, valores))
        if all(evaluar(p, contexto) for p in premisas):
            if not evaluar(conclusion, contexto):
                print("Contraejemplo:", contexto)
                return False
    return True


ARGUMENTOS = [
    ("1. p -> q, p |- q   (modus ponens)",
     ["condicional(p, q)", "p"], "q", ["p", "q"]),
    ("2. p -> q, ~p |- ~q (negar el antecedente)",
     ["condicional(p, q)", "negacion(p)"], "negacion(q)", ["p", "q"]),
    ("3. p -> q, ~q |- ~p (modus tollens)",
     ["condicional(p, q)", "negacion(q)"], "negacion(p)", ["p", "q"]),
    ("4. p v q, ~p |- q   (silogismo disyuntivo)",
     ["disyuncion(p, q)", "negacion(p)"], "q", ["p", "q"]),
]

if __name__ == "__main__":
    for nombre, premisas, conclusion, variables in ARGUMENTOS:
        valido = es_valido(premisas, conclusion, variables)
        veredicto = "VALIDO" if valido else "INVALIDO"
        print(f"{nombre}: {veredicto}\n")
