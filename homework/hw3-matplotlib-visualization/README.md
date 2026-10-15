# HW3 · Análisis de Pareto con Matplotlib

| | |
|---|---|
| **Sesión** | 4 · Visualización de datos con Matplotlib |
| **Entrega** | 2026-10-22 |
| **Estado** | ⏳ En progreso |
| **Dataset** | [MyAnimeList Database](https://github.com/Hernan4444/MyAnimeList-Database) |
| **Archivos** | [`hw3_matplotlib.ipynb`](hw3_matplotlib.ipynb) |

## 1. Enunciado

Realizar un **análisis de Pareto (por deciles)** sobre el dataset de MyAnimeList:

1. Ordenar los animes de forma descendente según la métrica `metric_column`.
2. Dividirlos en `n` grupos de igual tamaño sin alterar el orden (con `pd.qcut()` sobre el ranking).
3. Calcular la proporción que cada grupo aporta al total de la métrica.

```python
homework(anime_data: pd.DataFrame, metric_column: str, n: int) -> pd.Series
```

El resultado se visualiza en un **diagrama de Pareto**: barras con la proporción de cada grupo y una línea con la proporción acumulada.

## 2. Enfoque

_Pendiente._

## 3. Solución

_Pendiente._

## 4. Validación

| Caso | Entrada | Esperado | Obtenido | ✔ |
|---|---|---|---|---|
| 1 | Dataset completo, `Completed`, `n=10` | 10 grupos en orden descendente que suman ≈ 1.0 | | |
| 2 | `[40, 30, 20, 10]`, `n=2` | `Group 1 0.7 · Group 2 0.3` | | |
| 3 | `[60, 50, 40, 30, 20, 10]`, `n=3` | `0.523810 · 0.333333 · 0.142857` | | |

## 5. Resultados

_Pendiente: diagrama de Pareto._

## 6. Aprendizajes

_Pendiente._

## 7. Cómo ejecutar

Abre [`hw3_matplotlib.ipynb`](hw3_matplotlib.ipynb) con el kernel `.venv` y ejecuta las celdas en orden. La sección de preparación descarga el dataset (requiere conexión a internet).
