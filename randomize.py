from tools import calc_time, generate_base_image
from random import randint
import numpy as np

@calc_time
def randomize_model(reduced_image:np.ndarray, info:list) -> np.ndarray:
    _, _, channels = info[1]
    interpolated_image = generate_base_image(reduced_image, info[1])
    
    for row in range(interpolated_image.shape[0]):
        for col in range(interpolated_image.shape[1]):
            if row % 2 == 0 and col % 2 == 0:
                continue

            top = max((row // 2) * 2, 0)
            left = max((col // 2) * 2, 0)
            bottom = min(top + 2, interpolated_image.shape[0] - 1)
            right = min(left + 2, interpolated_image.shape[1] - 1)

            

            for channel in range(channels):
                top_left = interpolated_image[top, left, channel]
                bottom_left = interpolated_image[bottom, left, channel]
                top_right = interpolated_image[top, right, channel]
                bottom_right = interpolated_image[bottom, right, channel]
                
                min_val = int(min(top_left, top_right, bottom_left, bottom_right))
                max_val = int(max(top_left, top_right, bottom_left, bottom_right))
                interpolated_value = randint(min_val, max_val)
                
                interpolated_image[row, col, channel] = interpolated_value

    return np.clip(interpolated_image, 0, 255).astype(np.uint8)