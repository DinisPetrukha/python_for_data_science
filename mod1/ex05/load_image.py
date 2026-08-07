import numpy as np
from PIL import Image


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
        print(f"The shape of the image is: ({height}, {length}, {channels})")
        print(array_img)

        return array_img

    except FileNotFoundError as msg:
        print(f"{msg}")
    except Image.UnidentifiedImageError as msg:
        print(f"Error: {msg}")
    except AssertionError as msg:
        print(f"AssertionError: {msg}")

    return np.array([])


def main():
    """Main function to test the ft_load image loader."""
    print(ft_load("landscape.jpg"))


if __name__ == "__main__":
    main()
