import numpy as np
from load_image import ft_load
from PIL import Image
import matplotlib.pyplot as plt

def zoom(img: np.array, y_slice: int, x_slice: int) -> np.array:

    zoom_img = img[0:y_slice, 0:x_slice]
    print(f"New shape after slicing: ({y_slice}, {x_slice}, 1) or ({y_slice}, {x_slice})")
    print(zoom_img)

    # img_obj = Image.fromarray(zoom_img)
    # img_obj.show()
    plt.imshow(zoom_img, cmap='gray')
    plt.savefig("zoom_output.png")


def main():
    path = "animal.jpeg"
    img_array = ft_load(path)
    print(img_array)

    # Convert array back into a image object
    img_pil = Image.fromarray(img_array)

    # Transform into a grey scale image
    img_gray = img_pil.convert("L")

    # Convert back into array
    gray_array = np.array(img_gray)

    zoom(gray_array, 400, 400)

if __name__ == "__main__":
    main()