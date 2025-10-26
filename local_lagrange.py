from tools import calc_time, generate_base_image
import numpy as np

@calc_time
def local_lagrange_bilinear_model(reduced_image:np.ndarray, info:list) -> np.ndarray:
    def interpolate_pixel(p00:float, p01:float, p10:float, p11:float, dx:float, dy:float) -> float:
        # forma I(x,y)=p00​(1−dx)(1−dy)+p10​(dx)(1−dy)+p01​(1−dx)(dy)+p11​(dx)(dy)
        return (
            p00 * (1 - dx) * (1 - dy) + p10 * dx * (1 - dy) +
            p01 * (1 - dx) * dy + p11 * dx * dy
        )

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

            dx = (col - left) / 2 if right > left else 0
            dy = (row - top) / 2 if bottom > top else 0

            for channel in range(channels):
                top_left = interpolated_image[top, left, channel]
                bottom_left = interpolated_image[bottom, left, channel]
                top_right = interpolated_image[top, right, channel]
                bottom_right = interpolated_image[bottom, right, channel]

                interpolated_value = interpolate_pixel(
                    top_left, bottom_left, top_right, bottom_right, dx, dy
                )
                interpolated_image[row, col, channel] = interpolated_value

    return np.clip(interpolated_image, 0, 255).astype(np.uint8)

if __name__ == "__main__":
    import cv2
    import tools

    path = "./img/sets/gray_images/bird.tif"
    og_img = cv2.imread(path)
    rc_img, size = tools.reduce_image(og_img)
    information: list = [f"{path} reducida", size]

    ip_image, exec_time, tipo = local_lagrange_bilinear_model(rc_img, [f"{path} reducida", size])
    
    img_gris = cv2.cvtColor(rc_img, cv2.COLOR_BGR2GRAY)
    np.savetxt('rc_image_rgb.csv', img_gris, delimiter=',', fmt='%d')

    _ = tools.comparar_error(og_img, ip_image)

    cv2.imshow(f"{path} original", og_img)
    cv2.imshow(f"{path} reducida", rc_img)
    cv2.imshow(f"{path} interpolada", ip_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()