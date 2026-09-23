"""Actividad 6. Caso aplicado: reglas de un sistema escolar.

Variables:
  p: el usuario tiene credenciales validas
  q: el usuario esta inscrito en el cuatrimestre actual
  r: el usuario puede consultar sus calificaciones

Reglas traducidas a logica proposicional:
  R1: "si tiene credenciales validas y esta inscrito,
       entonces puede consultar calificaciones"
       -> condicional(conjuncion(p, q), r)
  R2: "si no esta inscrito, entonces no puede consultar
       calificaciones"
       -> condicional(negacion(q), negacion(r))

Pregunta: existe algun escenario en el que ambas reglas se cumplan
y aun asi un usuario SIN credenciales consulte calificaciones?
"""
from itertools import product

from tabla import evaluar

R1 = "condicional(conjuncion(p, q), r)"
R2 = "condicional(negacion(q), negacion(r))"
VARIABLES = ["p", "q", "r"]

if __name__ == "__main__":
    print("p | q | r | R1 | R2")
    print("-" * 20)
    for valores in product([True, False], repeat=len(VARIABLES)):
        contexto = dict(zip(VARIABLES, valores))
        r1 = evaluar(R1, contexto)
        r2 = evaluar(R2, contexto)
        fila = [int(v) for v in (*valores, r1, r2)]
        marca = ""
        if r1 and r2 and not contexto["p"] and contexto["r"]:
            marca = "  <-- escenario buscado"
        print(" | ".join(map(str, fila)) + marca)
