"""HW1 Session 2: filtrar múltiplos de 5 que sean impares con máscaras booleanas.

Ejecutar con el entorno activo:
    source ../.venv/bin/activate
    python hw1_explicacion.py
"""
import sys
import time

import numpy as np


def homework(a):
    mask = (a % 5 == 0) & (a % 2 == 1)
    my_result = a[mask]
    return my_result


print("=== Entorno ===")
print("Python:", sys.executable)
print("NumPy:", np.__version__)

print("\n=== Paso a paso con el ejemplo ===")
a = np.array([1, 5, 10, 3, 4, 25, 30])
mask = (a % 5 == 0) & (a % 2 == 1)
print("a                              =", a)
print("a % 5                          =", a % 5)
print("a % 5 == 0                     =", a % 5 == 0)
print("a % 2 == 1                     =", a % 2 == 1)
print("(a % 5 == 0) & (a % 2 == 1)    =", mask)
print("a[mask]                        =", a[mask])

print("\n=== Casos de prueba ===")
casos = [
    ("Caso 1", [1, 5, 10, 3, 4, 25, 30], [5, 25]),
    ("Caso 2", [11, 15, 20, 21, 35, 40, 45], [15, 35, 45]),
    ("Caso 3", [2, 4, 6, 8], []),
    ("Extra negativos", [-5, -15, -10, -25, 0, 7], [-5, -15, -25]),
]
for nombre, entrada, esperado in casos:
    resultado = homework(np.array(entrada))
    ok = np.array_equal(resultado, np.array(esperado))
    print(f"{nombre:16} {str(resultado):14} esperado {esperado} -> {'OK' if ok else 'FALLA'}")

print("\n=== Otros usos de las máscaras ===")
notas = np.array([2.5, 4.0, 3.2, 1.8, 4.7])
print("Aprobados (nota >= 3.0):      ", notas[notas >= 3.0])
t = np.array([22.1, 23.0, -999, 24.5, 85.0, 21.7])
print("Sensor sin valores imposibles:", t[(t > -50) & (t < 60)])
p = np.array([12000, 85000, 45000, 150000])
print("Precios entre 40k y 100k:     ", p[(p >= 40000) & (p <= 100000)])
v = np.array([120, 5000, 80, 150, 7200])
print("Compras sospechosas:          ", v[v > v.mean() + 0.5 * v.std()])
x = np.array([1.0, np.nan, 3.0])
print("Sin datos faltantes (NaN):    ", x[~np.isnan(x)])
s = np.array([3, -1, 7, -4])
s[s < 0] = 0
print("Negativos a cero (ReLU):      ", s)
edades = np.array([15, 22, 34, 41, 67])
print("Etiquetas por edad:           ", np.where(edades >= 18, "Adulto", "Menor"))
img = np.array([[10, 200], [130, 90]])
print("Imagen blanco y negro:\n", np.where(img > 128, 255, 0))

print("\n=== Velocidad: lista de Python vs NumPy (10 millones de números) ===")
grande = np.random.default_rng(0).integers(-1000, 1000, 10_000_000)
lista = grande.tolist()
t0 = time.perf_counter()
r_py = [n for n in lista if n % 5 == 0 and n % 2 == 1]
t_py = time.perf_counter() - t0
t0 = time.perf_counter()
r_np = homework(grande)
t_np = time.perf_counter() - t0
print(f"Python: {t_py:.3f} s | NumPy: {t_np:.3f} s | NumPy es {t_py / t_np:.1f} veces más rápido")
print("Mismo resultado:", len(r_py) == len(r_np))
