## Modelo Aleatorio

Para determinar el modelo de interpolación aleatoria dados los puntos
$(x,y)\in\mathbb{R}^2$. El método aleatorio propuesto consiste en tomar
el rectángulo que se forma con los valores conocidos
$x_i < x_{i+1},y_j < y_{j+1}$ y en el que $(x,y)$ se encuentra para
posteriormente proporcionar un valor con la distribución aleatoria
uniforme discreta entre los valores de la función $f$ que conocemos.

### Cuando $x=x_0$ o $x=x_n$ y $y_j<y<y_{j+1}$

Este caso ocurre en la primera y la última fila, cuando el valor de
$x=x_i$ para $i\in\{0,n\}$ es decir $x_0$ o $x_n$ y el valor de $y$ se
encuentra entre $y_j$ y $y_{j+1}$. Se elige un valor entero y aleatorio
tal que $f(x_i,y_j) \leq f(x,y) \leq f(x_i,y_{j+1})$. La elección es
aleatoria y uniforme entre todos los enteros entre esos dos.

### Cuando $y=y_0$ o $y=y_m$ y $x_i<x<x_{i+1}$

Ocurre en la primera y la última columna, cuando el valor de $y=x_i$
para $j\in\{0,m\}$ es decir $y_0$ o $y_m$ y el valor de $x$ se encuentra
entre $x_i$ y $x_{i+1}$. Se elige un valor entero y aleatorio tal que
$f(x_i,y_j) \leq f(x,y) \leq f(x_{i+1},y_j)$. La elección es aleatoria y
uniforme entre todos los enteros entre esos dos.

### Cuando $x_i<x<x_{i+1}$ y $y_j<y<y_{j+1}$

Ocurre en el resto de los casos, en este caso, como tanto x como y se
encuentra entre las variables $x_i$, $x_{i+1}$ y $y_j$, $y_{j+1}$, en
este caso, el valor de $(x,y)$ se encuentra entre los valores
$$A=   \begin{pmatrix}
        f(x_i,y_j) & f(x_i,y_{j+1}) \\
        f(x_{i+1},y_j) & f(x_{i+1},y_{j+1})
    \end{pmatrix}$$

Se elige un valor entero y aleatorio tal que
$min(A) \leq f(x,y) \leq max(A)$.
