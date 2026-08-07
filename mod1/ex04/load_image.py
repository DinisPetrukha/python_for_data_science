import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def ft_load(path: str) -> np.array:
    """
    Load an image from a given path, print its shape, and return its RGB.

    Args:
        path (str): The file path to the image (.jpg or .jpeg).

    Returns:
        np.ndarray: A NumPy array containing the image pixel data,
        or an empty array if an error occurs.
    """
    try:
        assert (
            path.lower().endswith(('.jpg', '.jpeg'))
            ), "file should be an .jpg / .jpeg"
        img = Image.open(path)
        array_img = np.array(img)
        height, length, channels = array_img.shape
        # print(f"The shape of the image is: ({height}, {length}, {channels})")

        return array_img

    except FileNotFoundError as msg:
        print(f"{msg}")
    except Image.UnidentifiedImageError as msg:
        print(f"Error: {msg}")
    except AssertionError as msg:
        print(f"AssertionError: {msg}")

    return np.array([])


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
        f"The shape of image is: ({y_slice}, {x_slice}, {channels}) "
        f"or ({y_slice}, {x_slice})")
    print(zoom_img)

    plt.imshow(zoom_img, "grey")
    plt.savefig("zoom_output.png")

    return zoom_img


def main():
    """Main function to test the ft_load image loader."""
    print(ft_load("landscape.jpg"))


if __name__ == "__main__":
    main()
