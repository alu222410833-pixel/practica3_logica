"""Actividad 7. Reto: formulas escritas con simbolos logicos.

El usuario escribe la formula con ¬, ∧, ∨, → y ↔; el programa la
traduce a la sintaxis de conectivos.py antes de evaluarla y detecta
automaticamente las variables con re.findall.

La traduccion usa un parser descendente recursivo que respeta la
precedencia del manual:  ¬ > ∧ > ∨ > → > ↔
(→ es asociativo a la derecha: p → q → r = p → (q → r))
"""
import re

from tabla import tabla_de_verdad

TOKEN_RE = re.compile(r"\s*([a-zA-Z_]+|[()¬∧∨→↔])")


def detectar_variables(formula):
    """Devuelve las variables que aparecen en la formula, ordenadas."""
    return sorted(set(re.findall(r"[a-zA-Z_]+", formula)))


def tokenizar(formula):
    tokens, pos = [], 0
    while pos < len(formula):
        m = TOKEN_RE.match(formula, pos)
        if not m:
            raise ValueError(f"Simbolo no reconocido: {formula[pos]!r}")
        tokens.append(m.group(1))
        pos = m.end()
    return tokens


class Parser:
    """Convierte los tokens en una expresion con funciones de conectivos."""

    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def _ver(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def _comer(self, esperado=None):
        tok = self._ver()
        if esperado and tok != esperado:
            raise ValueError(f"Se esperaba {esperado!r} y aparecio {tok!r}")
        self.pos += 1
        return tok

    def parse(self):
        expr = self.bicondicional()
        if self._ver() is not None:
            raise ValueError(f"Token inesperado: {self._ver()!r}")
        return expr

    def bicondicional(self):
        izq = self.condicional()
        while self._ver() == "↔":
            self._comer()
            izq = f"bicondicional({izq}, {self.condicional()})"
        return izq

    def condicional(self):
        izq = self.disyuncion()
        if self._ver() == "→":
            self._comer()
            # asociativo a la derecha
            return f"condicional({izq}, {self.condicional()})"
        return izq

    def disyuncion(self):
        izq = self.conjuncion()
        while self._ver() == "∨":
            self._comer()
            izq = f"disyuncion({izq}, {self.conjuncion()})"
        return izq

    def conjuncion(self):
        izq = self.negacion()
        while self._ver() == "∧":
            self._comer()
            izq = f"conjuncion({izq}, {self.negacion()})"
        return izq

    def negacion(self):
        if self._ver() == "¬":
            self._comer()
            return f"negacion({self.negacion()})"
        return self.atom()

    def atom(self):
        tok = self._ver()
        if tok == "(":
            self._comer("(")
            expr = self.bicondicional()
            self._comer(")")
            return expr
        if tok and re.fullmatch(r"[a-zA-Z_]+", tok):
            self._comer()
            return tok
        raise ValueError(f"Se esperaba variable o '(' y aparecio {tok!r}")


def traducir(formula):
    return Parser(tokenizar(formula)).parse()


if __name__ == "__main__":
    formula = input("Escribe la formula (¬ ∧ ∨ → ↔): ").strip()
    if not formula:
        formula = "¬(p ∧ q) → r"
        print("Ejemplo:", formula)
    variables = detectar_variables(formula)
    expr = traducir(formula)
    print("Variables detectadas:", variables)
    print("Traduccion:", expr)
    tabla_de_verdad(expr, variables)
