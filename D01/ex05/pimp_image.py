import numpy as np
import matplotlib.pyplot as plt


def invert_channel(value):
    return 255 - value


def keep_color(img: np.array, color: int) -> np.array:
    for i in range(3):
        if i == color:
            continue
        img[:, :, i] = 0
    return img


def ft_invert(img: np.array) -> np.array:
    """
        Invert Colors of an image
        To invert we substract current value from max value
        R_inverted = 255 - R
        G_inverted = 255 - G
        B_inverted = 255 - B
    """
    img = img.copy()
    for i in range(3):
        img[:, :, i] = invert_channel(img[:, :, i])

    plt.imshow(img)
    plt.show()
    return img


def ft_red(img: np.array) -> np.array:
    img = img.copy()
    img = keep_color(img, 0)
    plt.imshow(img)
    plt.show()
    return img


def ft_green(img: np.array) -> np.array:
    img = img.copy()
    img = keep_color(img, 1)
    plt.imshow(img)
    plt.show()
    return []


def ft_blue(img: np.array) -> np.array:
    img = img.copy()
    img = keep_color(img, 2)
    plt.imshow(img)
    plt.show()
    return []


def ft_grey(img: np.array) -> np.array:
    """
        Dot product on 3 channels to produce gray scale
        -> requires 'cmap=grey' in plot function
    """
    grayImage = np.dot(img[..., :3], [0.299, 0.587, 0.114])
    plt.imshow(grayImage, cmap='gray', vmin=0, vmax=255)
    plt.show()
    return grayImage
