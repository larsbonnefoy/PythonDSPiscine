from load_image import ft_load

import matplotlib.pyplot as plt
import numpy as np


def rbg_to_gray(img):
    """
        Dot product on 3 channels to produce gray scale
        -> requires 'cmap=grey' in plot function
    """
    grayImage = np.dot(img[..., :3], [0.299, 0.587, 0.114])
    return grayImage


def cut_grey_image(
    img: np.array, startY: int, startX: int, squareSize: int
) -> np.array:
    """
        Cuts image from start x and y with given squareSize
    """
    zoomedImg = img[
        startY: startY + squareSize,
        startX: startX + squareSize,
    ]
    grayImage = rbg_to_gray(zoomedImg)
    return grayImage


def ft_transpose(img: np.array) -> np.array:
    """
        Transposes input array to produce a new array
    """

    rows, cols = img.shape
    transposed_array = np.empty((cols, rows), dtype=img.dtype)
    for i in range(rows):
        for j in range(cols):
            transposed_array[j, i] = img[i, j]
    return transposed_array


def main():
    img = ft_load("animal.jpeg")
    if len(img) == 0:
        print("ft_load failed")
        return
    print(img)
    print(f"Y = {np.shape(img)[0]}")
    print(f"X = {np.shape(img)[1]}")
    print(f"Number of channels = {np.shape(img)[2]}")
    cut_image = cut_grey_image(img, 50, 400, 400)
    transpose_image = ft_transpose(cut_image)
    # print(transpose_image)
    print(f"New shape after transpose = {np.shape(transpose_image)}")
    plt.imshow(transpose_image, cmap='gray', vmin=0, vmax=255)
    print(transpose_image)
    plt.show()


if __name__ == "__main__":
    main()
