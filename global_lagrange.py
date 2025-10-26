import numpy as np
import tools
import cv2

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

    x0 = 2 * np.arange(1, A_orig.shape[1] + 1).astype(np.float64)
    y0 = 2 * np.arange(1, A_orig.shape[0] + 1).astype(np.float64)

    x = np.arange(1, np.max(x0) + 1, dtype=np.float64)
    y = np.arange(1, np.max(y0) + 1, dtype=np.float64)

    LagraX = np.array([[CoefLagraX(x0, i_py, k) for k in x] for i_py in range(len(x0))]).T

    LagraY = np.array([[CoefLagraX(y0, i_py, k) for k in y] for i_py in range(len(y0))]).T

    if A_orig.ndim == 3:
        interpolated_channels = []
        num_channels = A_orig.shape[2]
        
        for c in range(num_channels):
            A_channel = A_orig[:, :, c]
            
            C_channel = LagraY.dot(A_channel).dot(LagraX.T)
            
            interpolated_channels.append(C_channel)
        A = np.stack(interpolated_channels, axis=-1)

    elif A_orig.ndim == 2:
        A = LagraY.dot(A_orig).dot(LagraX.T)
        
    else:
        raise ValueError(f"La imagen de entrada tiene una forma inesperada: {A_orig.shape}")
    print(A)
    return np.clip(A, 0, 255).astype(np.uint8)


if __name__ == "__main__":
    path = "./img/sets/gray_images/bird.tif"
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