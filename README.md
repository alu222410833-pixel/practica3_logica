# Práctica No. 3 — Programación y comprobación de lógica proposicional

**Asignatura:** Fundamentos de Inteligencia Artificial
**Programa:** Ingeniería en Tecnologías de la Información e Innovación Digital
**Grupo:** ITIID-I-72
**Docente:** MDTI Marco Antonio Romero Rodríguez

**Integrantes:**
- Jose Carlos De La Cruz Vazquez 
- 

## Estructura del repositorio

| Archivo | Actividad |
|---|---|
| `conectivos.py` | 1. Conectivos lógicos como funciones |
| `tabla.py` | 2. Generador de tablas de verdad |
| `clasificar.py` | 3. Clasificación de fórmulas |
| `equivalencias.py` | 4. Comprobación de equivalencias |
| `argumentos.py` | 5. Validez de argumentos |
| `caso_sistema.py` | 6. Caso aplicado: reglas de un sistema |
| `reto.py` | 7. Reto: fórmulas con símbolos ¬ ∧ ∨ → ↔ |

Las fórmulas se escriben con las funciones de `conectivos.py`
(ej. `condicional(disyuncion(p, q), r)`), que `tabla.py` inyecta
en el entorno de evaluación.

## Ejecución

```powershell
python conectivos.py
python tabla.py
python clasificar.py
python equivalencias.py
python argumentos.py
python caso_sistema.py
python reto.py
```

## Resultados

### Actividad 3 — Clasificación de fórmulas

| Fórmula | Resultado |
|---|---|
| p ∧ ¬p | contradicción |
| p ∨ ¬p | tautología |
| ((p → q) ∧ (q → r)) → (p → r) | tautología |
| (p → q) → (q → p) | contingencia |

### Actividad 4 — Equivalencias comprobadas

| Ley | ¿Equivalentes? |
|---|---|
| De Morgan (1): ¬(p ∧ q) ≡ ¬p ∨ ¬q | True |
| De Morgan (2): ¬(p ∨ q) ≡ ¬p ∧ ¬q | True |
| Implicación material: p → q ≡ ¬p ∨ q | True |
| Contrapositiva: p → q ≡ ¬q → ¬p | True |
| Distributiva: p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r) | True |
| Doble negación: ¬¬p ≡ p | True |
| Caso negativo: p → q vs q → p | **False** (no equivalentes) |

### Actividad 5 — Validez de argumentos

| Argumento | Veredicto | Regla / falacia |
|---|---|---|
| p → q, p ⊢ q | VÁLIDO | Modus ponens |
| p → q, ¬p ⊢ ¬q | INVÁLIDO — contraejemplo {p=0, q=1} | Falacia de negar el antecedente |
| p → q, ¬q ⊢ ¬p | VÁLIDO | Modus tollens |
| p ∨ q, ¬p ⊢ q | VÁLIDO | Silogismo disyuntivo |

### Actividad 6 — Análisis del caso aplicado

Las reglas se tradujeron como R1 = (p ∧ q) → r y R2 = ¬q → ¬r.
**Sí existe el escenario buscado**: en la línea **p=0, q=1, r=1**
ambas reglas se cumplen y, sin embargo, un usuario sin credenciales
puede consultar calificaciones. La política es consistente pero
incompleta: R1 solo dice qué *alcanza* para consultar, no qué se
*exige*. Para cerrar el hueco habría que agregar la regla
r → p ("si consulta calificaciones, entonces tiene credenciales
válidas") o bien r ↔ (p ∧ q).

```
p | q | r | R1 | R2
1 | 1 | 1 | 1  | 1
1 | 1 | 0 | 0  | 1
1 | 0 | 1 | 1  | 0
1 | 0 | 0 | 1  | 1
0 | 1 | 1 | 1  | 1   <-- escenario buscado
0 | 1 | 0 | 1  | 1
0 | 0 | 1 | 1  | 0
0 | 0 | 0 | 1  | 1
```

## Evidencias

Todas las evidencias (tablas de verdad resueltas a mano en el
cuaderno y capturas de la salida de cada programa) se concentran
en un solo documento:

[Ver evidencias (PDF)](evidencias/evidencias.pdf)

## Cuestionario

**1. ¿Por qué el condicional p → q es verdadero cuando p es falso?**
Porque la implicación solo afirma que no ocurre el caso "p verdadero
y q falso". Si p no se cumple, la promesa no se puede romper: es una
*verdad vacua*. En el lenguaje cotidiano "si... entonces" sugiere
causalidad; en lógica solo exige consistencia entre los valores.

**2. ¿Cuántas líneas tiene la tabla con 6 variables? ¿Qué problema
anticipa?**
2⁶ = 64 líneas. Cada variable duplica la tabla: el crecimiento es
exponencial. Con 30 variables serían ~1,073 millones de líneas, así
que la fuerza bruta se vuelve inviable — es la razón de que existan
métodos más inteligentes como los solucionadores SAT.

**3. Diferencia entre fórmula válida y argumento válido.**
Una fórmula válida (tautología) es verdadera en toda interpretación
por sí misma. Un argumento válido es una relación entre premisas y
conclusión: no exige que la conclusión sea siempre verdadera, solo
que no exista ningún caso donde las premisas sean verdaderas y la
conclusión falsa.

**4. ¿Qué relación hay entre De Morgan y simplificar condiciones if?**
Las leyes permiten reescribir condiciones negadas de forma
equivalente y a veces más legible:

```python
if not (usuario_activo and tiene_permiso):
# equivale a:
if (not usuario_activo) or (not tiene_permiso):
```

Son la misma condición; elegir una u otra es cuestión de claridad.

**5. ¿Qué riesgo implica `eval` y cómo mitigarlo?**
`eval` ejecuta cualquier texto que reciba: si la expresión viene del
usuario, puede inyectar código (ej. `__import__("os").system("...")`)
y comprometer el sistema. Mitigaciones: nunca evaluar entrada externa;
usar un parser con gramática limitada que solo acepte la sintaxis de
fórmulas (como el de `reto.py`); usar `ast.literal_eval` para datos;
y restringir el entorno con `{"__builtins__": {}}` como se hace en
`tabla.py` — aunque la medida robusta es no usar `eval` con texto
que no controlas.

## Conclusiones

- 
