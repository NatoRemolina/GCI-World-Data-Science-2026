# Convenciones del repositorio

## Nombres

| Elemento | Formato | Ejemplo |
|---|---|---|
| Carpeta de tarea | `hwN-tema-en-kebab-case` | `hw2-pandas-data-cleaning` |
| Notebook de tarea | `hwN_tema.ipynb` | `hw2_pandas.ipynb` |
| Script de apoyo | `hwN_explicacion.py` | `hw1_explicacion.py` |
| Apuntes | `session-NN-tema.md` | `session-03-pandas.md` |
| Material oficial | `course-materials/lectures/session-NN-tema/` | `session-05-supervised-learning/` |

## Idioma

- **Enunciados y material del curso:** en su idioma original (inglés).
- **Documentación, explicaciones y apuntes propios:** en español.
- **Código:** nombres de variables y funciones en inglés si los exige la plantilla del curso; comentarios en español.
- Para la versión en inglés se agregará `README.en.md` junto a cada `README.md`, con enlaces cruzados entre ambos.

## Flujo de trabajo por sesión

1. Guardar las diapositivas y notebooks oficiales en `course-materials/lectures/session-NN-tema/` (no se versionan).
2. Copiar la plantilla de la tarea a `homework/hwN-tema/` y renombrarla según la tabla anterior.
3. Copiar `homework/_plantilla/README.md` a la carpeta de la tarea y llenar el encabezado y el enunciado.
4. Resolver, validar con los casos de prueba y documentar el enfoque, los resultados y los aprendizajes.
5. Ejecutar todas las celdas en orden para que GitHub muestre las salidas.
6. Verificar localmente con `ruff check homework/`.
7. Actualizar las tablas de progreso de [README.md](../README.md) y [homework/README.md](../homework/README.md).
8. Si la tarea tiene un script de apoyo, agregarlo a `.github/workflows/ci.yml`.

## Cuándo publicar

Las soluciones se publican **después de la fecha de entrega**, para no exponerlas a otros participantes de la cohorte mientras la tarea sigue abierta.

## Mensajes de commit

Se usa [Conventional Commits](https://www.conventionalcommits.org/es/v1.0.0/) en español:

```text
<tipo>(<alcance opcional>): <descripción en imperativo y minúscula>
```

| Tipo | Uso | Ejemplo |
|---|---|---|
| `feat` | Solución nueva de una tarea | `feat(hw2): resuelve promedio de Score por Type` |
| `docs` | Documentación y apuntes | `docs(notes): agrega apuntes de la sesión 3` |
| `fix` | Corrección de una solución | `fix(hw3): corrige el orden de los grupos de Pareto` |
| `chore` | Configuración, dependencias, CI | `chore: actualiza pandas a 3.0.7` |
| `style` | Formato sin cambios de lógica | `style(hw1): ordena imports` |

## Calidad

- Python con un máximo de 100 caracteres por línea; la configuración de `ruff` está en `pyproject.toml`.
- Las celdas de preparación de los notebooks del curso no se modifican.
- Cada función entregada se valida con al menos los casos del enunciado y un caso borde propio.
