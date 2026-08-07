import numpy as np
from load_image import ft_load
import matplotlib.pyplot as plt


def zoom(img: np.array, y_slice: int, x_slice: int) -> np.array:
    """Crops and zooms into the center of an image array.

    Calculates the center coordinates of the input image and extracts a
    centered region specified by the slice dimensions while preserving the
    3D shape. Prints the resulting array shape and data, then saves
    the cropped image to a PNG file.

    Parameters
    ----------
    img : np.array
        The input image represented as a NumPy array (H x W x C).
    y_slice : int
        The height (in pixels) of the cropped zoom area.
    x_slice : int
        The width (in pixels) of the cropped zoom area.

    Returns
    -------
    np.array
        The cropped image array.
    """
    height, width = img.shape[0], img.shape[1]
    center_y, center_x = height // 2, width // 2

    y_start = center_y - (y_slice // 2)
    y_end = center_y + (y_slice // 2)

    x_start = center_x - (x_slice // 2)
    x_end = center_x + (x_slice // 2)

    zoom_img = img[y_start:y_end, x_start:x_end, 0:1]

    channels = zoom_img.shape[2]

    print(
        f"New shape after slicing: ({y_slice}, {x_slice}, {channels}) "
        f"or ({y_slice}, {x_slice})")
    print(zoom_img)

    plt.imshow(zoom_img, "grey")
    plt.savefig("zoom_output.png")


def main():
    """
    Main function to load an image and apply the zoom operation.

    Loads an image from disk into a NumPy array, displays its initial
    structure, and calls the zoom function to extract a 400x400 central region.
    """
    path = "animal.jpeg"
    img_array = ft_load(path)
    print(img_array)

    zoom(img_array, 400, 400)


if __name__ == "__main__":
    main()
