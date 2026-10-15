# GCI World 2026 · Ciencia de Datos con Python

Portafolio de tareas, apuntes y scripts desarrollados durante el programa **GCI World** del Matsuo-Iwasawa Lab, The University of Tokyo (cohorte septiembre 2026).

[![CI](https://github.com/NatoRemolina/GCI-World-Data-Science-2026/actions/workflows/ci.yml/badge.svg)](https://github.com/NatoRemolina/GCI-World-Data-Science-2026/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.14-3776AB?logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-2.5-013243?logo=numpy&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-3.0-150458?logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.9-F7931E?logo=scikitlearn&logoColor=white)
[![Licencia: MIT](https://img.shields.io/badge/Licencia-MIT-green.svg)](LICENSE)

🇪🇸 Español · 🇬🇧 English (próximamente)

---

## Contenido

- [Descripción](#descripción)
- [Objetivos de aprendizaje](#objetivos-de-aprendizaje)
- [Progreso](#progreso)
- [Estructura del repositorio](#estructura-del-repositorio)
- [Reproducibilidad](#reproducibilidad)
- [Control de calidad](#control-de-calidad)
- [Documentación](#documentación)
- [Material del curso y licencia](#material-del-curso-y-licencia)
- [Autora](#autora)

## Descripción

GCI World es un programa intensivo de ciencia de datos que recorre el flujo completo de un proyecto analítico: manipulación de datos, limpieza, visualización, estadística y aprendizaje automático, con Python como lenguaje de trabajo.

Este repositorio documenta mi proceso: para cada tarea registro el enfoque, la solución, cómo la validé y qué aprendí. Los enunciados se conservan en su idioma original (inglés) y mis explicaciones están en español.

## Objetivos de aprendizaje

1. Manipular arreglos y tablas de forma vectorizada con **NumPy** y **pandas**.
2. Limpiar, transformar y agregar datos reales con valores faltantes e inconsistencias.
3. Comunicar hallazgos con visualizaciones claras en **Matplotlib** y **Seaborn**.
4. Entrenar y evaluar modelos supervisados con **scikit-learn**.
5. Trabajar con un flujo reproducible: entorno aislado, versiones fijadas y verificación automática.

## Progreso

| # | Sesión | Tema | Tarea | Conceptos clave | Entrega | Estado |
|---|---|---|---|---|---|---|
| 0 | Pre-lecture | Fundamentos de Python | — | Tipos, control de flujo, funciones | — | ✅ |
| 1 | Session 1 | Introducción a la ciencia de datos | — | Ciclo de un proyecto de datos | — | ✅ |
| 2 | Session 2 | NumPy | [HW1](homework/hw1-numpy-boolean-masks/) | Vectorización, máscaras booleanas | 2026-10-08 | ✅ |
| 3 | Session 3 | pandas | [HW2](homework/hw2-pandas-data-cleaning/) | `groupby`, agregación, ordenamiento | 2026-10-15 | ⏳ |
| 4 | Session 4 | Matplotlib y Seaborn | [HW3](homework/hw3-matplotlib-visualization/) | Análisis de Pareto, `qcut` | 2026-10-22 | ⏳ |
| 5 | Session 5 | Aprendizaje supervisado | [HW4](homework/hw4-supervised-learning/) | Regresión lineal, R² | 2026-10-30 | ⏳ |

✅ completado · ⏳ en progreso

## Estructura del repositorio

```text
.
├── .github/workflows/   Integración continua (lint + ejecución de tareas)
├── docs/                Configuración del entorno, convenciones y recursos
├── homework/            Una carpeta por tarea, con notebook, script y README
│   └── _plantilla/      Plantilla de documentación para tareas nuevas
├── notes/               Apuntes por sesión y glosario bilingüe
├── course-materials/    Material oficial del curso (solo local, excluido de git)
├── requirements.txt     Dependencias con versiones fijadas
├── requirements-dev.txt Herramientas de calidad (ruff, nbconvert)
└── pyproject.toml       Configuración del linter
```

## Reproducibilidad

```bash
git clone https://github.com/NatoRemolina/GCI-World-Data-Science-2026.git
cd GCI-World-Data-Science-2026
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
```

Las versiones están fijadas en `requirements.txt` y verificadas con Python 3.14. La guía completa, con el uso en VS Code y la solución de problemas, está en [docs/setup.md](docs/setup.md).

## Control de calidad

En cada `push` a `main`, GitHub Actions ejecuta:

| Verificación | Herramienta | Alcance |
|---|---|---|
| Estilo y errores estáticos | `ruff check` | Scripts y notebooks de `homework/` |
| Ejecución de scripts | `python` | Scripts de las tareas completadas |
| Ejecución de notebooks | `jupyter nbconvert --execute` | Notebooks de las tareas completadas |

Para correrlo localmente:

```bash
ruff check homework/
```

## Documentación

| Documento | Contenido |
|---|---|
| [docs/setup.md](docs/setup.md) | Instalación y uso del entorno virtual |
| [docs/convenciones.md](docs/convenciones.md) | Nombres de carpetas, commits y flujo de trabajo por sesión |
| [docs/recursos.md](docs/recursos.md) | Videos del curso, documentación oficial y datasets |
| [homework/README.md](homework/README.md) | Índice de tareas |
| [notes/glosario.md](notes/glosario.md) | Glosario de términos inglés → español |

## Material del curso y licencia

Las diapositivas, notebooks de clase, soluciones oficiales y datasets son propiedad del **Matsuo-Iwasawa Lab, The University of Tokyo**, y su distribución a terceros sin permiso está prohibida. Por eso `course-materials/` está excluida del control de versiones y este repositorio solo contiene trabajo propio.

El código y la documentación originales se publican bajo [licencia MIT](LICENSE). Los enunciados incluidos en los notebooks de tareas pertenecen al curso y no están cubiertos por esa licencia.

## Autora

**Natalia Patricia Remolina Rodríguez**
Ingeniería Física · Universidad Nacional de Colombia

[![GitHub](https://img.shields.io/badge/GitHub-NatoRemolina-181717?logo=github)](https://github.com/NatoRemolina)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Natalia%20Remolina-0A66C2?logo=linkedin)](https://www.linkedin.com/in/natalia-patricia-remolina-rodriguez-1327a8220/)
