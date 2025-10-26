from local_lagrange import local_lagrange_bilinear_model
from global_lagrange import global_lagrange_model
from randomize import randomize_model
from tools import reduce_image, calc_time, comparar_error, show_image
import os
import cv2
from collections import defaultdict
import numpy as np

@calc_time
def browse_files(path: str, set_name) -> None:
    files = os.listdir(path)
    log_file_handles = {}
    
    errors_by_type = defaultdict(list)

    try:
        for file in files:
            print(f"\n === {path}{file} ===")
            og_image = cv2.imread(f"{path}/{file}")
            rc_image, size = reduce_image(og_image)
            information: list = [f"{path}/{file} reducida", size]
            
            png_filename = file.replace(".tif", ".png")
            
            cv2.imwrite(f"./img/originals/{png_filename}", og_image)

            methods_to_run = [
                #local_lagrange_bilinear_model,
                global_lagrange_model,
                #randomize_model    
            ]
            
            for interpolation_func in methods_to_run:
                try:
                    ip_image, exec_time, tipo = interpolation_func(rc_image, information)
                    tipo_upper = tipo.upper()
                    tipo_lower = tipo.lower()

                    if tipo_upper not in log_file_handles:
                        log_filename = f"log_{tipo_lower}_{set_name}.txt"
                        print(f"Creando log: {log_filename}")
                        log_file_handles[tipo_upper] = open(log_filename, "w")
                        log_file_handles[tipo_upper].write(f"--- LOG DE INTERPOLACIÓN: {tipo_upper} ({set_name}) ---\n\n")

                    output_dir = f"./img/interpolated/{tipo_lower}/"
                    os.makedirs(output_dir, exist_ok=True)
                    
                    output_path = f"{output_dir}{png_filename}"
                    cv2.imwrite(output_path, ip_image)

                    err = comparar_error(og_image, ip_image)
                    errors_by_type[tipo_upper].append(err)
                    
                    txt_file = log_file_handles[tipo_upper]
                    txt_file.write(f"Archivo: {path}{file}\n")
                    txt_file.write(f"\tTiempo: {exec_time:.2f}s\n")
                    txt_file.write(f"\tError: {err:.2f}%\n\n")
                
                except Exception as e:
                    tipo_nombre = interpolation_func.__name__
                    print(f"Error al procesar {tipo_nombre} en {file}: {e}")

            cv2.imshow("./img/sets/gray_images/bird.tif original", og_image)
            cv2.imshow("./img/sets/gray_images/bird.tif reducida", rc_image)
            cv2.imshow("./img/sets/gray_images/bird.tif interpolada", ip_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            break
    
    finally:
        print("\n=== PROMEDIOS FINALES ===")
        
        for tipo, error_list in errors_by_type.items():
            if error_list:
                avg_err = sum(error_list) / len(error_list)
                print(f"Promedio de errores [{tipo}]: {avg_err:.2f}%")
                
                if tipo in log_file_handles:
                    log_file_handles[tipo].write(f"\n=== PROMEDIO FINAL ===\n")
                    log_file_handles[tipo].write(f"Promedio de errores: {avg_err:.2f}%\n")
            else:
                print(f"No se registraron errores para [{tipo}]")

        print("\nCerrando archivos de log...")
        for handle in log_file_handles.values():
            handle.close()

if __name__ == "__main__":
    browse_files("./img/sets/color_images/", "color") 
    browse_files("./img/sets/gray_images/", "gray")