# 🧮 Proyecto: Interpolación de Imágenes  
### *(Métodos de Lagrange y Método Aleatorio)*

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Estado-Activo-success)
![License](https://img.shields.io/badge/Licencia-Acad%C3%A9mica-lightgrey)

> Proyecto de métodos numéricos aplicados a **interpolación de imágenes**.  
> Compara distintos enfoques: **Lagrange Global**, **Lagrange Local Bilineal** y un **método Aleatorio de referencia**, evaluando su precisión y eficiencia computacional tanto en imágenes **a color** como **en escala de grises**.

---

## 📂 Estructura del Repositorio

```bash
├── main.py                   # Script principal del proyecto
├── global_lagrange.py        # Implementación del modelo de Lagrange global
├── local_lagrange.py         # Implementación del modelo bilineal Lagrange local
├── randomize.py              # Método aleatorio (referencia)
├── tools.py                  # Funciones auxiliares (reducción, error, temporizador)
├── generate_reduce_img.py    # Herramienta auxiliar de reducción (opcional)
│
├── img/
│   ├── sets/
│   │   ├── color_images/     # Imágenes en color de entrada
│   │   └── gray_images/      # Imágenes en escala de grises
│   ├── interpolated/         # Resultados generados por método
│   ├── originals/            # (opcional) Imágenes originales
│   └── reduced/              # (opcional) Imágenes reducidas
│
├── logs/                     # Archivos de registro por método y set
│   └── log_<metodo>_<set>.txt
│
└── md/                       # Documentación técnica (Markdown)
    ├── 1_0_origen.md
    ├── 2_1_Mbilineal.md
    ├── 2_2_MBicubico.md
    ├── 2_3_MAleatorio.md
    ├── 2_5_CComputacional.md
    └── 3_1MBilinealLagrange.md
```

---

## ⚙️ Requisitos Técnicos

- **Python 3.8+**  
- Librerías necesarias:
  numpy>=1.21.0
  opencv>=4.5.5
  ```bash
  pip install numpy opencv-python
  ```

---

## 🚀 Ejecución del Proyecto

El script principal es `main.py`, que coordina todo el flujo:

1. Recorre las carpetas de imágenes (`color_images` y `gray_images`).
2. Reduce cada imagen usando `tools.reduce_image()`.
3. Ejecuta los tres modelos de interpolación:
   - `local_lagrange_bilinear_model`
   - `global_lagrange_model`
   - `randomize_model`
4. Registra **errores y tiempos de ejecución** en los logs (`logs/`).

### Comando de ejecución

```bash
python3 main.py
```

> 📘 Los resultados se almacenan en `logs/` y las imágenes interpoladas en `img/interpolated/`.

---

## 🧠 Descripción de Módulos

| Módulo | Función principal |
|--------|-------------------|
| **main.py** | Controla el flujo de procesamiento y escritura de logs. |
| **tools.py** | Utilidades de reducción, cálculo de error y medición de tiempo. |
| **global_lagrange.py** | Interpolación **global polinómica** en toda la imagen. |
| **local_lagrange.py** | Interpolación **bilineal por regiones locales**, más eficiente. |
| **randomize.py** | Modelo **no determinista** de referencia para análisis comparativo. |

---

## 📊 Resultados y Logs

Los resultados se almacenan en `logs/` con formato:

```
Archivo: ./img/sets/color_images/lena3.tif
	Tiempo: 0.08s
	Error: 99.03%
```

Al final de cada log se calcula el **promedio de errores** por método.  
Estos valores se analizaron posteriormente y se incluyeron en los reportes del directorio `md/`.

---

## 📘 Documentación del Proyecto

> Todos los reportes están disponibles en la carpeta `md/`, convertidos desde LaTeX a Markdown.

| Archivo | Descripción |
|----------|--------------|
| `1_0_origen.md` | Introducción y objetivos del proyecto. |
| `2_1_Mbilineal.md` | Modelo bilineal de interpolación. |
| `2_2_MBicubico.md` | Comparativa con interpolación cúbica. |
| `2_3_MAleatorio.md` | Método aleatorio de referencia. |
| `2_5_CComputacional.md` | Análisis de complejidad y desempeño. |
| `3_1MBilinealLagrange.md` | Estudio del modelo Lagrange local. |

---

## 🧩 Consideraciones Técnicas

- Los errores se calculan mediante **norma L2 relativa**.
- Los tiempos de ejecución se miden con decoradores (`@calc_time`).
- El proyecto está diseñado para comparar **fidelidad vs. costo computacional**.
- Los logs sirven como base para tablas y gráficas de rendimiento.

---

## 🔬 Objetivo Académico

> Este proyecto busca demostrar la aplicabilidad de los **métodos de interpolación de Lagrange** en el procesamiento digital de imágenes, evaluando su precisión y eficiencia frente a métodos aleatorios o locales.

---

## 🏁 Próximos pasos

- Incorporar **visualización gráfica automática** de errores y tiempos.
- Agregar soporte para **interpolación cúbica y spline bicúbico**.
- Publicar resultados y comparativas en notebooks (`.ipynb`).

---

## 👥 Coautoría

**Autores principales:**
- Enrique Gomez 
- Juan Carlos Ramos
- Victoria Galvan
> Proyecto desarrollado como parte de los estudios de Métodos Numéricos — *Universidad Autónoma de Aguascalientes*
