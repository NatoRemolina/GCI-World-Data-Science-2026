# HW1 · Filtrado con máscaras booleanas en NumPy

| | |
|---|---|
| **Sesión** | 2 · Manipulación eficiente de datos con NumPy |
| **Entrega** | 2026-10-08 |
| **Estado** | ✅ Completada |
| **Entorno** | Python 3.14 · NumPy 2.5 |
| **Archivos** | [`hw1_numpy.ipynb`](hw1_numpy.ipynb) · [`hw1_explicacion.py`](hw1_explicacion.py) · [`numpy_paso_a_paso.pdf`](numpy_paso_a_paso.pdf) |

## 1. Enunciado

Dado un arreglo unidimensional de enteros, devolver solo los elementos que cumplen **dos condiciones a la vez**:

1. Ser **múltiplos de 5**.
2. Ser **impares**.

```python
homework(a: np.ndarray) -> np.ndarray
```

## 2. Enfoque

Resuelto primero a mano con `[1, 5, 10, 3, 4, 25, 30]`:

| Número | ¿Múltiplo de 5? | ¿Impar? | ¿Se queda? |
|---|---|---|---|
| 1 | No | Sí | No |
| **5** | Sí | Sí | **Sí** |
| 10 | Sí | No | No |
| 3 | No | Sí | No |
| 4 | No | No | No |
| **25** | Sí | Sí | **Sí** |
| 30 | Sí | No | No |

Ambas condiciones se expresan con el residuo de la división (operador `%`):

| Pregunta | Operación | Con 25 | Con 10 |
|---|---|---|---|
| ¿Es múltiplo de 5? | `x % 5 == 0` | sobra 0 → Sí | sobra 0 → Sí |
| ¿Es impar? | `x % 2 == 1` | sobra 1 → Sí | sobra 0 → No |

En lugar de recorrer el arreglo con un `for`, NumPy evalúa cada condición sobre todos los elementos a la vez y devuelve una **máscara booleana**. Las dos máscaras se combinan con `&` y se usan para indexar el arreglo.

## 3. Solución

```python
def homework(a):
    mask = (a % 5 == 0) & (a % 2 == 1)
    my_result = a[mask]
    return my_result
```

- `a % 5 == 0` y `a % 2 == 1` producen arreglos de `True`/`False` del mismo tamaño que `a`.
- `&` combina las máscaras elemento a elemento. Cada condición va entre paréntesis porque `&` tiene mayor precedencia que `==`.
- `a[mask]` conserva solo las posiciones marcadas como `True`.
- También funciona con negativos: en Python, `-5 % 2` da `1`.

## 4. Validación

| Caso | Entrada | Esperado | Obtenido | ✔ |
|---|---|---|---|---|
| 1 | `[1, 5, 10, 3, 4, 25, 30]` | `[5, 25]` | `[5, 25]` | ✅ |
| 2 | `[11, 15, 20, 21, 35, 40, 45]` | `[15, 35, 45]` | `[15, 35, 45]` | ✅ |
| 3 | `[2, 4, 6, 8]` | `[]` | `[]` | ✅ |
| Extra · negativos | `[-5, -15, -10, -25, 0, 7]` | `[-5, -15, -25]` | `[-5, -15, -25]` | ✅ |

[`hw1_explicacion.py`](hw1_explicacion.py) verifica los casos automáticamente con `np.array_equal`, y el CI del repositorio ejecuta tanto el script como el notebook en cada `push`.

## 5. Resultados

Salida del script:

```text
=== Paso a paso con el ejemplo ===
a                              = [ 1  5 10  3  4 25 30]
a % 5                          = [1 0 0 3 4 0 0]
a % 5 == 0                     = [False  True  True False False  True  True]
a % 2 == 1                     = [ True  True False  True False  True False]
(a % 5 == 0) & (a % 2 == 1)    = [False  True False False False  True False]
a[mask]                        = [ 5 25]

=== Casos de prueba ===
Caso 1           [ 5 25]        esperado [5, 25] -> OK
Caso 2           [15 35 45]     esperado [15, 35, 45] -> OK
Caso 3           []             esperado [] -> OK
Extra negativos  [ -5 -15 -25]  esperado [-5, -15, -25] -> OK
```

**Rendimiento.** Resultado de filtrar 10 millones de enteros con la misma regla en mi equipo:

| Implementación | Tiempo |
|---|---|
| Python puro | 0.219 s |
| NumPy (máscara booleana) | 0.044 s |

NumPy fue **5 veces más rápido** y dio el mismo resultado, porque sus operaciones corren en código C compilado sobre memoria contigua de un solo tipo.

## 6. Aprendizajes

**La misma idea aplicada a otros problemas** (incluidos en el script):

| Caso | Código |
|---|---|
| Estudiantes aprobados | `notas[notas >= 3.0]` |
| Limpiar lecturas imposibles de un sensor | `t[(t > -50) & (t < 60)]` |
| Rango de precios | `p[(p >= 40000) & (p <= 100000)]` |
| Detección simple de anomalías | `v[v > v.mean() + 0.5 * v.std()]` |
| Quitar datos faltantes | `x[~np.isnan(x)]` |
| Activación ReLU | `s[s < 0] = 0` |
| Crear etiquetas | `np.where(edades >= 18, "Adulto", "Menor")` |

Operadores para combinar condiciones: `&` (y), `|` (o) y `~` (no).

**Errores comunes identificados:**

| Error | Síntoma | Corrección |
|---|---|---|
| Usar `and` en lugar de `&` | `ValueError: truth value of an array is ambiguous` | Usar `&` |
| Omitir los paréntesis | Resultado incorrecto o error de tipos | `(a % 5 == 0) & (a % 2 == 1)` |
| Devolver la máscara | Sale `[False True ...]` | Devolver `a[mask]` |
| Poner `import` dentro de la función | El evaluador la rechaza | Las librerías ya vienen cargadas |

## 7. Cómo ejecutar

Con el entorno del repositorio activo (ver [docs/setup.md](../../docs/setup.md)):

```bash
cd homework/hw1-numpy-boolean-masks
python hw1_explicacion.py
```

Para el notebook, abre [`hw1_numpy.ipynb`](hw1_numpy.ipynb) y selecciona el kernel `.venv`.

La guía [`numpy_paso_a_paso.pdf`](numpy_paso_a_paso.pdf) resume el método completo para leer, resolver y probar este tipo de problemas.
