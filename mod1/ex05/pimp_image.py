import numpy as np
from load_image import ft_load
import matplotlib.pyplot as plt


def ft_invert(img: np.array):
    """Inverts the color of the image received."""
    return_img = 255 - img

    plt.imshow(return_img)
    plt.savefig("invert.png")

    return return_img


def ft_red(img: np.array):
    """Applies a red filter by setting green and blue channels to zero."""
    return_img = img.copy()
    return_img[:, :, 1:3] = 0

    plt.imshow(return_img)
    plt.savefig("red.png")

    return return_img


def ft_green(img: np.array):
    """Applies a green filter by setting blue and red channels to zero."""
    return_img = img.copy()
    return_img[:, :, [0, 2]] = 0

    plt.imshow(return_img)
    plt.savefig("green.png")

    return return_img


def ft_blue(img: np.array):
    """Applies a blue filter by setting red and green channels to zero."""
    return_img = img.copy()
    return_img[:, :, [0, 1]] = 0

    plt.imshow(return_img)
    plt.savefig("blue.png")

    return return_img


def ft_grey(img: np.array):
    """Applies a red filter by setting green and blue channels to zero."""
    # Mean of the 3 RGB colors
    return_img = np.mean(img, axis=-1)

    plt.imshow(return_img, "grey")
    plt.savefig("grey.png")

    return return_img


def main():
    path = "landscape.jpg"
    array_img = ft_load(path)

    ft_invert(array_img)
    ft_red(array_img)
    ft_green(array_img)
    ft_blue(array_img)
    ft_grey(array_img)


if __name__ == "__main__":
    main()
