# HW1 Session 2: filtrado con máscaras booleanas en NumPy

Ejecutado el 2026-10-07 con Python 3.14.4 y NumPy 2.5.3 en el entorno virtual del repositorio.
Entrega: jueves 8 de octubre de 2026, 11:00 UTC (6:00 a.m. hora de Colombia).

---

## 0. Cómo ejecutarlo

Con el entorno virtual del repositorio activo (ver [docs/setup.md](../../docs/setup.md)):

```bash
cd homework/hw1-numpy-boolean-masks
python hw1_explicacion.py
```

**En VS Code con el notebook:** abre `hw1_numpy.ipynb`, haz clic en **Select Kernel**, elige **Python Environments** y luego `.venv`. Ejecuta las celdas en orden con Shift + Enter.

**Archivos de esta carpeta:**

| Archivo | Contenido |
|---|---|
| `hw1_numpy.ipynb` | Notebook de la tarea resuelto |
| `hw1_explicacion.py` | Script con el paso a paso, casos de prueba y otros usos de las máscaras |
| `numpy_paso_a_paso.pdf` | Guía en PDF del método de resolución |

---

## 1. El problema en palabras simples

De una lista de números enteros hay que quedarse solo con los que cumplen **dos reglas a la vez**:

1. Ser **múltiplo de 5**, es decir, estar en la tabla del 5.
2. Ser **impar**.

Resuelto a mano con `[1, 5, 10, 3, 4, 25, 30]`:

| Número | ¿Múltiplo de 5? | ¿Impar? | ¿Se queda? |
|---|---|---|---|
| 1 | No | Sí | No |
| **5** | Sí | Sí | **Sí** |
| 10 | Sí | No | No |
| 3 | No | Sí | No |
| 4 | No | No | No |
| **25** | Sí | Sí | **Sí** |
| 30 | Sí | No | No |

Resultado: **5 y 25**.

## 2. El residuo: operador `%`

| Pregunta | Operación | Con 25 | Con 10 |
|---|---|---|---|
| ¿Es múltiplo de 5? | `x % 5 == 0` | sobra 0 → Sí | sobra 0 → Sí |
| ¿Es impar? | `x % 2 == 1` | sobra 1 → Sí | sobra 0 → No |

Con negativos también funciona: en Python `-5 % 2` da `1`.

## 3. Cómo lo resuelve NumPy

NumPy hace la pregunta a todos los números a la vez y devuelve una **máscara** de `True` y `False`. Luego `a[mask]` se queda solo con los elementos marcados como `True`.

```python
def homework(a):
    mask = (a % 5 == 0) & (a % 2 == 1)
    my_result = a[mask]
    return my_result
```

Esta función va en la celda debajo de **"2. Your Answer"** del notebook y es lo que se pega en Omnicampus, sin `import`.

Salida real del script:

```text
=== Entorno ===
Python: .venv/bin/python
NumPy: 2.5.3

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

## 4. Para qué sirve NumPy

NumPy es la librería de Python para operar **arreglos de números completos sin escribir ciclos `for`**. A esto se le llama vectorización, y es la base de pandas, scikit-learn, TensorFlow y PyTorch.

- **Código corto:** una línea expresa la regla completa.
- **Velocidad:** las operaciones corren en código C compilado.
- **Menos memoria:** los elementos tienen un solo tipo y se guardan juntos.
- **Herramientas listas:** estadística, álgebra lineal y números aleatorios.

Medición en este equipo, filtrando 10 millones de números con la regla de la tarea:

```text
Python: 0.219 s | NumPy: 0.044 s | NumPy es 5.0 veces más rápido
Mismo resultado: True
```

## 5. Otros casos donde se usa la misma idea

Salida real del script:

```text
Aprobados (nota >= 3.0):       [4.  3.2 4.7]
Sensor sin valores imposibles: [22.1 23.  24.5 21.7]
Precios entre 40k y 100k:      [85000 45000]
Compras sospechosas:           [5000 7200]
Sin datos faltantes (NaN):     [1. 3.]
Negativos a cero (ReLU):       [3 0 7 0]
Etiquetas por edad:            ['Menor' 'Adulto' 'Adulto' 'Adulto' 'Adulto']
Imagen blanco y negro:
 [[  0 255]
 [255   0]]
```

| Caso | Código |
|---|---|
| Estudiantes aprobados | `notas[notas >= 3.0]` |
| Limpiar un sensor | `t[(t > -50) & (t < 60)]` |
| Rango de precios | `p[(p >= 40000) & (p <= 100000)]` |
| Compras sospechosas | `v[v > v.mean() + 0.5 * v.std()]` |
| Quitar datos faltantes | `x[~np.isnan(x)]` |
| Negativos a cero (ReLU) | `s[s < 0] = 0` |
| Crear etiquetas | `np.where(edades >= 18, 'Adulto', 'Menor')` |
| Imagen blanco y negro | `np.where(img > 128, 255, 0)` |

Operadores para combinar condiciones: `&` (y), `|` (o) y `~` (no). Cada condición va siempre entre paréntesis.

## 6. Errores comunes y entrega

| Error | Qué pasa | Solución |
|---|---|---|
| Dejar la línea `some` del notebook original | `NameError` | Borrar el contenido de la celda y pegar la función |
| Usar `and` en vez de `&` | `ValueError` | Usar `&` |
| Olvidar los paréntesis | Resultado incorrecto o error | `(a % 5 == 0) & (a % 2 == 1)` |
| Poner `import` dentro de la función | Omnicampus puede rechazarla | El evaluador ya incluye NumPy |
| Devolver la máscara | Sale `[False True ...]` | Devolver `a[mask]` |

Pasos para entregar:

1. Abrir Homework 1 en Omnicampus.
2. Pegar la función completa, desde `def homework(a):` hasta `return my_result`.
3. Hacer clic en **[Python code submission]**.
4. Verificar que la nota sea 3.0. Cuenta la **última** entrega, así que no se reenvía después de un 3.0.
