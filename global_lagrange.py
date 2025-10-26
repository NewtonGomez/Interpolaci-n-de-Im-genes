import numpy as np
import tools
import cv2

import numpy as np

def _affine_scale(u, a, b):
    # Escala u de [min(u), max(u)] a [-1, 1] con protección
    u = np.asarray(u, dtype=np.float64)
    umin, umax = float(np.min(u)), float(np.max(u))
    if umax == umin:
        return np.zeros_like(u), (umin, umax)
    v = 2.0 * (u - umin) / (umax - umin) - 1.0
    return v, (umin, umax)

def _affine_unscale(v, bounds):
    umin, umax = bounds
    return (v + 1.0) * (umax - umin) / 2.0 + umin

def _barycentric_weights(x_nodes):
    # Pesos w_i con logs para magnitud y paridad para signo
    x = np.asarray(x_nodes, dtype=np.float64)  # más espacio dinámico
    n = x.size
    D = x[:, None] - x[None, :]  # matriz de diferencias
    np.fill_diagonal(D, 1.0)     # evitar log(0) en la diagonal

    # signo = producto del signo de cada (x_i - x_j)
    sign_mat = np.sign(D)
    sign_mat[np.diag_indices(n)] = 1.0
    neg_counts = (sign_mat < 0).sum(axis=1)
    signs = np.where(neg_counts % 2 == 0, 1.0, -1.0).astype(np.float64)

    # magnitud = exp(-sum(log|x_i - x_j|))
    logmag = -np.sum(np.log(np.abs(D)), axis=1, dtype=np.float64)
    # normaliza para evitar under/overflow extremo
    logmag -= np.max(logmag)
    mags = np.exp(logmag, dtype=np.float64)

    w = signs * mags
    # re-normaliza para que ||w||1 ≈ 1 (escala invariante)
    w /= np.sum(np.abs(w))
    return w.astype(np.float64)  # suficiente para armar L

def _barycentric_matrix(x_nodes, x_eval, w):
    x_nodes = np.asarray(x_nodes, dtype=np.float64)
    x_eval  = np.asarray(x_eval,  dtype=np.float64)
    n = x_nodes.size
    m = x_eval.size
    L = np.zeros((m, n), dtype=np.float64)

    for k, xk in enumerate(x_eval):
        # Si coincide con un nodo, fila canónica
        idx = np.where(np.isclose(xk, x_nodes, rtol=0, atol=1e-12))[0]
        if idx.size > 0:
            L[k, idx[0]] = 1.0
            continue

        dif = xk - x_nodes
        t = w / dif
        denom = np.sum(t)
        L[k, :] = t / denom
    return L

def _lagrange_operators(x_nodes, x_eval):
    # Reescalamos a [-1, 1] para mejorar condición
    xs, b_nodes = _affine_scale(x_nodes, None, None)
    xe, _       = _affine_scale(x_eval,  None, None)
    w = _barycentric_weights(xs)
    return _barycentric_matrix(xs, xe, w)


@tools.calc_time
def global_lagrange_model(A_orig:np.ndarray, info) -> np.ndarray:
    def CoefLagraX(x_nodes, i_py, x_val):
        """
        Calcula el coeficiente de Lagrange L_i(x_val).
        i_py: índice base 0 del nodo.
        x_nodes: array de coordenadas de los nodos.
        x_val: punto en el que se evalúa.
        """
        nodes_minus_i = np.delete(x_nodes, i_py)
        
        numer = np.prod(x_val - nodes_minus_i)
        denom = np.prod(x_nodes[i_py] - nodes_minus_i)
        
        if denom == 0:
            if x_val == x_nodes[i_py]:
                return 1.0
            else:
                return 0.0
            
        coef = numer / denom
        return coef

    x0 = 2 * np.arange(1, A_orig.shape[1] + 1, dtype=np.float64)
    y0 = 2 * np.arange(1, A_orig.shape[0] + 1, dtype=np.float64)

    x  = np.arange(1, int(np.max(x0)) + 1, dtype=np.float64)
    y  = np.arange(1, int(np.max(y0)) + 1, dtype=np.float64)

    LagraX = _lagrange_operators(x0, x)  # m_x × n_x
    LagraY = _lagrange_operators(y0, y)  # m_y × n_y

    A_work = A_orig.astype(np.float64)   # evita cast uint8 durante el cálculo

    if A_work.ndim == 3:
        chans = []
        for c in range(A_work.shape[2]):
            Cc = LagraY @ A_work[:, :, c] @ LagraX.T
            chans.append(Cc)
        A = np.stack(chans, axis=-1)
    else:
        A = LagraY @ A_work @ LagraX.T

    A = np.clip(A, 0.0, 255.0).astype(np.uint8)

    return A

if __name__ == "__main__":
    path = "./img/sets/color_images/monarch.tif"
    og_img = cv2.imread(path)
    rc_img, size = tools.reduce_image(og_img)
    information: list = [f"{path} reducida", size]

    ip_image, exec_time, tipo = global_lagrange_model(rc_img, "wfew")
    
    # 3. Guardamos los arrays 2D (¡esto sí funciona!)
    img_gris = cv2.cvtColor(rc_img, cv2.COLOR_BGR2GRAY)
    np.savetxt('rc_image_rgb.csv', img_gris, delimiter=',', fmt='%d')

    _ = tools.comparar_error(og_img, ip_image)

    cv2.imshow(f"{path} original", og_img)
    cv2.imshow(f"{path} reducida", rc_img)
    cv2.imshow(f"{path} interpolada", ip_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()