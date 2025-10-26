## Modelo Bilineal basado en planos locales

Este método se basa directamente en el modelo bilineal de Lagrange
descrito en la sección anterior. En lugar de desarrollar de forma
explícita los polinomios de Lagrange en ambas direcciones, se implementa
su forma reducida la cual opera dentro de planos locales definidos por
los píxeles vecinos.

El plano local se forma a partir de cuatro puntos adyacentes en la malla
de la imagen:
$$p_{00} = f(x_0,y_0), \quad p_{10} = f(x_1,y_0), \quad p_{01} = f(x_0,y_1), \quad p_{11} = f(x_1,y_1)$$

Interpolamos primero respecto a $x$, dentro de cada fila del bloque:

$$f(x,y_0) = p_{00}(1-dx) + p_{10}dx, \quad 
f(x,y_1) = p_{01}(1-dx) + p_{11}dx$$

donde

$$dx = \frac{x - x_0}{x_1 - x_0}$$

Luego, interpolamos respecto a $y$ utilizando los resultados anteriores:

$$f(x,y) = f(x,y_0)(1-dy) + f(x,y_1) dy$$

con

$$dy = \frac{y - y_0}{y_1 - y_0}$$

Sustituyendo $f(x,y_0)$ y $f(x,y_1)$, obtenemos la fórmula bilineal
completa:

$$f(x,y) = p_{00}(1-dx)(1-dy) + p_{10} dx (1-dy) + p_{01} (1-dx) dy + p_{11} dx dy$$

De este modo, la interpolación se realiza de forma local y sucesiva
sobre toda la imagen, reconstruye los valores faltantes entre los
píxeles conocidos, cada punto estimado surge de una combinación lineal
de sus cuatro vecinos inmediatos.
