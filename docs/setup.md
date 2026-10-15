# Configuración del entorno

Todo el repositorio comparte un único entorno virtual en la raíz (`.venv`), que sirve para todas las sesiones y tareas.

## 1. Crear el entorno (solo una vez)

```bash
cd "GCI Word_202609"
python3 -m venv .venv
```

## 2. Activarlo (cada vez que abras una terminal)

```bash
source .venv/bin/activate
```

La terminal muestra `(.venv)` al inicio de la línea. Para comprobarlo:

```bash
which python
```

## 3. Instalar las dependencias (solo una vez, o cuando cambie `requirements.txt`)

```bash
pip install -r requirements.txt
```

Para incluir también las herramientas de calidad (`ruff` y `nbconvert`), que son las mismas que usa el CI:

```bash
pip install -r requirements-dev.txt
```

## 4. Usar el entorno en notebooks

- **VS Code:** abre el `.ipynb`, haz clic en **Select Kernel** → **Python Environments** → `.venv`.
- **JupyterLab:** con el entorno activo, ejecuta `jupyter lab`.

## 5. Salir del entorno

```bash
deactivate
```

## Agregar una librería nueva

```bash
pip install <librería>
```

Después agrégala a `requirements.txt` en la sección que corresponda, con la versión exacta (`pip show <librería>`).

## Problemas comunes

| Síntoma | Causa | Solución |
|---|---|---|
| `ModuleNotFoundError` | El entorno no está activo o el kernel del notebook no es `.venv` | Activar el entorno o cambiar el kernel |
| `bad interpreter` al activar | La carpeta del proyecto se movió después de crear el entorno | Borrar `.venv` y repetir los pasos 1 a 3 |
