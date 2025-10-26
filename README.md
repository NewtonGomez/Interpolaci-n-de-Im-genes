# Proyecto: Interpolación de Imágenes (Métodos de Lagrange y Aleatorio)

Este repositorio contiene un proyecto de métodos numéricos aplicados a interpolación de imágenes. Implementa y compara varios métodos de interpolación (Lagrange global, Lagrange local bilineal y un método aleatorio) sobre imágenes en color y en gris. Además incluye herramientas para reducir resolución, calcular errores y registrar tiempos de ejecución.

## Contenido principal

- `main.py` - Script principal; recorre imágenes en `img/sets/` (color y gris), reduce su tamaño, ejecuta los métodos de interpolación y escribe logs en `logs/`.
- `global_lagrange.py` - Implementación del modelo de Lagrange global.
- `local_lagrange.py` - Implementación del modelo local (bilineal Lagrange).
- `randomize.py` - Implementación del método aleatorio de interpolación.
- `tools.py` - Utilidades: reducción de imagen, cálculo de tiempo, comparación de error, visualización.
- `generate_reduce_img.py` - (herramienta auxiliar) — generación/reducción de imágenes (si aplica).

## Estructura de carpetas

- `img/`
  - `sets/` - Conjuntos de imágenes de entrada
    - `color_images/` - imágenes en color usadas por el script
    - `gray_images/` - imágenes en escala de grises usadas por el script
  - `interpolated/` - Salida de las imágenes interpoladas (por método)
  - `originals/` - (opcional) imágenes originales
  - `reduced/` - (opcional) versiones reducidas

- `logs/` - Archivos de log generados por cada método, p. ej. `log_global_lagrange_model_color.txt`.
- `md/` - Documentación del proyecto y notas: contiene varios documentos explicativos sobre los métodos y resultados (por ejemplo `1_0_origen.md`, `2_1_Mbilineal.md`, `2_2_MBicubico.md`, `2_3_MAleatorio.md`, `2_5_CComputacional.md`, `3_1MBilinealLagrange.md`).

## Requisitos

- Python 3.7+ (recomendado 3.8+)
- Paquetes principales:
  - numpy
  - opencv-python


## Cómo ejecutar

El script principal es `main.py`. Por defecto (cuando se ejecuta como script) realiza lo siguiente:

- Recorre `./img/sets/color_images/` y `./img/sets/gray_images/`.
- Para cada imagen, la reduce (función `reduce_image` en `tools.py`).
- Ejecuta, en orden, los métodos:
  1. `local_lagrange_bilinear_model`
  2. `global_lagrange_model`
  3. `randomize_model`
- Registra tiempo de ejecución y error de interpolación en `logs/`.

Ejecutar:

```bash
python3 main.py
```

Notas:
- `main.py` llama a `browse_files(path, set_name)` y crea logs en `./logs/log_<metodo>_<set>.txt`.
- Los resultados de interpolación se guardan (o están preparados para guardarse) en `img/interpolated/<metodo>/`.

## Qué hace cada script / módulo

- `tools.py`:
  - `reduce_image(image)` -> devuelve la imagen reducida (cada 2 píxeles) y su tamaño.
  - `comparar_error(original, interpolated)` -> calcula error mediante norma L2 relativa y lo imprime.
  - `calc_time` -> decorador para medir tiempos de ejecución.

- `main.py`:
  - Orquesta el flujo: lectura de archivos, reducción, aplicación de métodos y escritura de logs.

- Modelos (`global_lagrange.py`, `local_lagrange.py`, `randomize.py`):
  - Cada módulo expone una función que toma la imagen reducida y la información (tupla) y debe devolver la imagen interpolada, tiempo de ejecución y un identificador del tipo (según convención en el código).

## Logs y resultados

- Los logs se almacenan en `logs/` y contienen, para cada archivo procesado: nombre, tiempo de ejecución y error calculado.
- Al final, `main.py` imprime un promedio de errores por método.

## Documentación adicional

La carpeta `md/` contiene documentación y apuntes del proyecto, entre ellos:

- `1_0_origen.md` — origen del proyecto y objetivos.
- `2_1_Mbilineal.md`, `2_2_MBicubico.md`, `2_3_MAleatorio.md` — explicaciones de los métodos de interpolación.
- `2_5_CComputacional.md` — consideraciones computacionales.
- `3_1MBilinealLagrange.md` — detalles del método bilineal Lagrange local.

Revisa esos archivos para mayor contexto teórico y decisiones experimentales.

## Buenas prácticas y notas

- Si trabajas con muchas imágenes, considera ajustar la forma en que se guardan/visualizan para evitar saturar memoria.
- Añadir un `requirements.txt` y/o un pequeño script de setup facilitará replicar el entorno.

## Próximos pasos sugeridos

- Añadir un `requirements.txt` o `pyproject.toml`.
- Crear un script CLI (opciones con `argparse`) para seleccionar carpetas de entrada, métodos a ejecutar y activar/desactivar guardado de imágenes.
- Añadir algunos tests unitarios para `tools.py` (p. ej. `comparar_error`, `reduce_image`).


