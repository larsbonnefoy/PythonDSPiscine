from load_image import ft_load

import matplotlib.pyplot as plt
import numpy as np


def main():
    img = ft_load("animal.jpeg")
    print(img)
    print(f"Y = {np.shape(img)[0]}")
    print(f"X = {np.shape(img)[1]}")
    print(f"Number of channels = {np.shape(img)[2]}")
    imgplot = plt.imshow(img[:,:,1])
    plt.show()


if __name__ == "__main__":
    main()
