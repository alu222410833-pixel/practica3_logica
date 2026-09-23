"""Actividad 1. Conectivos logicos como funciones.

Cada funcion recibe valores booleanos y devuelve un booleano.
El bloque __main__ imprime las cuatro combinaciones posibles
de cada conectivo binario.
"""


def negacion(p):
    return not p


def conjuncion(p, q):
    return p and q


def disyuncion(p, q):
    return p or q


def condicional(p, q):
    return (not p) or q


def bicondicional(p, q):
    return p == q


def disyuncion_exclusiva(p, q):
    # XOR: solo es verdadera cuando p y q tienen valores DIFERENTES.
    # La disyuncion normal (or) acepta el caso en que ambas son
    # verdaderas; la exclusiva lo rechaza.
    return p != q


if __name__ == "__main__":
    print("negacion")
    print("p | not p")
    for p in (True, False):
        print(f"{int(p)} | {int(negacion(p))}")

    for f in (conjuncion, disyuncion, condicional, bicondicional,
              disyuncion_exclusiva):
        print(f"\n{f.__name__}")
        print("p | q | resultado")
        for p in (True, False):
            for q in (True, False):
                print(f"{int(p)} | {int(q)} | {int(f(p, q))}")
