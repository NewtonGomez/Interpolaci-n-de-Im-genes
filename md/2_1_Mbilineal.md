## Modelo bilineal de Lagrange

Para determinar el método de interpolación de Lagrange en su forma
bilineal, consideramos la función descrita previamente. Interpolamos
primero respecto a $x$ con los valores de $y$ de cada columna
$j\in\{1,2,\dots,m\}$ en la matriz. La deducción de la fórmula está
expandida en [@samillan2025metodo]

$$f(x,y_j) = \sum_{i=0}^n f(x_i,y_j)L_i(x)$$ Donde
$$L_i(x)=\prod_{l=0,l\neq i}^n \frac{x-x_l}{x_i-x_l}$$ De modo que
obtenemos $m+1$ ecuaciones que estiman cada una de las $j$ columnas.
$$(f(x,y_0),f(x,y_1), \dots, f(x,y_m))$$

Ahora interpolamos esas funciones respecto a $y$.

$$f(x,y) = \sum_{j=0}^m f(x,y_j)L_j(x)$$ donde
$$L_j(x)=\prod_{k=0,k\neq j}^n \frac{y-y_k}{y_j-y_k}$$ Sustituyendo
$f(x,y_j)= \sum_{i=0}^n f(x_i,y_j)L_i(x)$ tenemos que
$$f(x,y) = \sum_{j=0}^m  \sum_{i=0}^n f(x_i,y_j)L_i(x)L_j(x)$$ donde
$$L_i(x)L_j(x)=\prod_{l=0,l\neq i}^n \frac{x-x_l}{x_i-x_l} \prod_{k=0,k\neq j}^n \frac{y-y_k}{y_j-y_k}$$
