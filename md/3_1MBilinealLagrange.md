La metodología aplicada en este trabajo consistió en un proceso
estructurado para analizar y comparar distintos métodos de interpolación
en imágenes, considerando tanto versiones a color como en escala de
grises.

## Selección de conjuntos de datos

Para la etapa experimental se utilizaron dos grupos de imágenes: el
**Color Set** y el **Greyscale Set**. El primero incluye imágenes en
formato RGB con información completa de los tres canales de color (rojo,
verde y azul), mientras que el segundo agrupa versiones equivalentes en
escala de grises, donde cada píxel se representa por un único valor de
intensidad luminosa.

## Construcción de modelos

Con base en el marco teórico de la interpolación bilinieal, se
desarrollaron tres enfoques metodológicos que difieren en la forma de
estimar los valores intermedios entre los píxeles conocidos. Cada modelo
fue implementado bajo las mismas condiciones de entrada, tanto para el
conjunto a color como para el de escala de grises.

1.  **Modelo Interpolación bilineal de Lagrange.** Este método aplica el
    principio de interpolación en dos direcciones: primero en el eje
    horizontal y posteriormente en el eje vertical, lo que permite
    obtener una aproximación continua de la superficie bidimensional que
    representa la imagen. En cada etapa, se construyen polinomios que
    pasan exactamente por los puntos conocidos.

2.  **Modelo Interpolación bilineal basada en planos locales.** En este
    método, la imagen se divide en regiones elementales de $2\times2$
    píxeles. Cada región define un plano local sobre el cual se estima
    la intensidad de los píxeles intermedios mediante una combinación
    lineal de los valores en los vértices. Este procedimiento se aplica
    de manera independiente a cada canal de color en las imágenes RGB y
    de forma única en las imágenes en escala de grises. El resultado es
    una reconstrucción continua que conserva la suavidad local del
    contenido original.

3.  **Método aleatorio.** Este enfoque se emplea como referencia
    comparativa. En lugar de seguir una relación funcional determinada,
    los valores intermedios se asignan de manera aleatoria dentro del
    rango definido por los píxeles vecinos. De esta forma, se obtiene
    una base de comparación para contrastar los efectos de las técnicas
    planteadas, evaluando la influencia del orden y continuidad visual.

Cada uno de estos modelos se fundamenta en el **marco teórico** de la
interpolación donde se proporciona una formulación general, el cual
describe cómo estimar valores desconocidos a partir de una función
continua que aproxima los datos discretos originales.

## Métrica de desempeño

Se analizó la diferencia global entre la imagen original y la imagen
interpolada, con el objetivo de medir la precisión del proceso de
reconstrucción. Asimismo, se tomó en cuenta el costo computacional de
cada técnica, considerando el tiempo de ejecución.
