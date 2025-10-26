import time
import numpy as np
import cv2

def calc_time(func:any):
    def wrapper(*args:any, **kwargs:any) -> any:
        begin = time.time()
        solution = func(*args, **kwargs)
        end = time.time()
        elapsed = end - begin
        print(f"La función '{func.__name__}' tardó {elapsed:.4f} segundos en ejecutarse")
        return solution, elapsed, func.__name__
    return wrapper

def show_image(image:np.ndarray, information:list) -> None:
    def array_a_imagen(arr:np.ndarray) -> np.ndarray:
        arr = np.clip(arr, 0, 255).astype(np.uint8)
        return (arr if arr.ndim == 2 else
                arr[:, :, 0] if arr.shape[2] == 1 else
                cv2.cvtColor(arr, cv2.COLOR_RGB2BGR) if arr.shape[2] == 3 else
                (_ for _ in ()).throw(ValueError("El array debe tener 1 o 3 canales")))
    
    print(f"informacion de la imagen {information[0]} {information[1]}")
    cv2.imshow(information[0], array_a_imagen(image))

def reduce_image(image:np.ndarray) -> tuple:
    return image[::2, ::2], image[::2,::2].shape

def generate_base_image(rc_image:np.ndarray, info:tuple) -> np.ndarray:
    height, width, channels = info
    new_img = np.zeros((height*2, width*2, channels))
    
    new_img[::2, ::2] = rc_image

    return new_img

def comparar_error(original: np.ndarray, interpolated: np.ndarray) -> float:
    def calc_l2_norm(matrix: np.ndarray) -> float:
        return np.sqrt(np.sum(np.square(matrix)))

    if original.shape != interpolated.shape:
        print("Las imagenes no tienen el mismo")
        print(original.shape, interpolated.shape)
        return 0.00

    er_matrix = (calc_l2_norm(original - interpolated) / calc_l2_norm(original)) * 100
    print(f"Error de la interpolación (norma euclidiana) es: {er_matrix:.2f}%")

    return er_matrix
