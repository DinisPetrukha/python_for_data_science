import numpy as np
from load_image import ft_load
from load_image import zoom
import matplotlib.pyplot as plt


def transpose(img: np.array) -> np.array:
    """
    Transposes a 3D image array into a 2D transposed image array.

    Args:
        img (np.array): A 3D NumPy array representing the cropped image
                        with shape (height, width, channels).

    Returns:
        np.array: A 2D NumPy array containing the transposed pixel values
                  with shape (width, height).
    """
    height, width = img.shape[0], img.shape[1]
    transposed_img = np.zeros((height, width), dtype=img.dtype)

    for y in range(height):
        for x in range(width):
            transposed_img[x][y] = img[y][x][0]

    plt.imshow(transposed_img, "grey")
    plt.savefig("transpose_output.png")

    height, width = transposed_img.shape[0], transposed_img.shape[1]

    print(f"New shape after Transpose: ({height}, {width})")

    return transposed_img


def main():
    """
    Loads an image, applies a zoom transformation, prints its initial state,
    transposes the zoomed image manually, and saves/displays the result.
    """
    path = "animal.jpeg"
    array_img = ft_load(path)
    zoom_img = zoom(array_img, 400, 400)

    print(zoom_img)
    print(transpose(zoom_img))


if __name__ == "__main__":
    main()
