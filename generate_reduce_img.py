from tools import reduce_image
import cv2
import os

path = "./img/sets/gray_images/"
files = os.listdir(path)
log_file_handles = {}

for file in files:
    print(f"\n === {path}{file} ===")
    og_image = cv2.imread(f"{path}/{file}")
    rc_image, size = reduce_image(og_image)
    
    png_filename = file.replace(".tif", ".png")
    
    cv2.imwrite(f"./img/reduced/{png_filename}", rc_image)