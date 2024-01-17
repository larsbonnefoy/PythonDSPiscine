from load_image import ft_load

import matplotlib.pyplot as plt
import numpy as np


def rbg_to_gray(img):
    """
        One way of changing all 3 channels to a combination of greyscale
    """
    grayImage = np.zeros(img.shape)
    R = np.array(img[:, :, 0])
    G = np.array(img[:, :, 1])
    B = np.array(img[:, :, 2])

    R = R * 0.299
    G = G * 0.587
    B = B * 0.114

    Avg = R + G + B
    grayImage = img.copy()

    for i in range(3):
        grayImage[:, :, i] = Avg

    return grayImage


def rbg_to_gray2(img):
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
    grayImage = rbg_to_gray2(zoomedImg)
    return grayImage


def main():
    img = ft_load("animal.jpeg")
    if len(img) == 0:
        print("Ft_load failed")
        return
    print(img)
    print(f"Y = {np.shape(img)[0]}")
    print(f"X = {np.shape(img)[1]}")
    print(f"Number of channels = {np.shape(img)[2]}")
    finalImage = cut_grey_image(img, 50, 400, 400)
    print(f"New shape after slicing= {np.shape(finalImage)}")
    plt.imshow(finalImage, cmap='gray', vmin=0, vmax=255)
    print(finalImage)
    plt.show()


if __name__ == "__main__":
    main()
