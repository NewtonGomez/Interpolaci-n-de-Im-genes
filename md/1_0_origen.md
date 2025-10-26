# Introducción

## Origen de las Imágenes

Para el desarrollo de este estudio se empleó un conjunto de imágenes
obtenido del repositorio en línea de la *Universidad de Waterloo*. Este
repositorio es ampliamente utilizado en el ámbito académico para la
evaluación de algoritmos de procesamiento digital de imágenes, ya que
proporciona material estandarizado que permite realizar comparaciones
objetivas entre diferentes métodos de análisis y reconstrucción visual.

## Descripción de las Imágenes

El repositorio incluye dos conjuntos principales de imágenes: Colour Set
y Greyscale Set 1.

-   **Colour Set:** Este conjunto contiene ocho imágenes, de las cuales
    cinco son fotografías y tres corresponden a ejemplos de arte
    generado por computadora.

-   **Greyscale Set 1:** Este conjunto contiene doce imágenes, algunas
    fotográficas y otras sintéticas. Una de ellas es un montaje
    compuesto por cuatro piezas más pequeñas. Esta diversidad de tipos
    de imágenes permite evaluar el rendimiento de algoritmos de
    procesamiento en distintos contextos visuales. Todas las imágenes
    poseen una resolución de 256$\times$`<!-- -->`{=html}256 píxeles con
    una profundidad de 8 bits.

## Objetivo del Estudio

El objetivo principal de este trabajo es evaluar la capacidad de
distintas técnicas de interpolación para recuperar imágenes digitales a
partir de versiones reducidas en resolución, utilizando un conjunto de
imágenes de referencia en escala de grises y a color. La metodología
propuesta permitirá comparar el desempeño de ambas técnicas en términos
de calidad visual y precisión de reconstrucción.

-   Determinar cuál de las metodologías de interpolación ofrece un mejor
    equilibrio entre calidad y rendimiento en la recuperación de
    imágenes.

-   Analizar el costo computacional de cada técnica, identificando su
    eficiencia y escalabilidad.

## Hipótesis

Al comparar el modelo bilineal tradicional con la variante basada en
planos locales, se espera observar diferencias significativas en la
calidad de reconstrucción y el error de interpolación, lo que permitirá
identificar las causas de la pérdida de desempeño.
