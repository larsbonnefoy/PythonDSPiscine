import PIL as PIL
from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    """
        Loads an image, prints its format and its pixel content in RGB format
    """
    # convert the PIL.Image.Image object into an 8-bit (dtype=uint8) numpy
    # array.
    try:
        img = np.asarray(Image.open(path))
        print("The shape of the image is " + str(np.shape(img)))
        return img
    except FileNotFoundError as fnfe:
        print(f"FileNotFoundError: {fnfe}")
    except AttributeError as ae:
        print(f"AttributeError: {ae}")
    except PermissionError as pe:
        print(f"PermissionError: {pe}")
    except PIL.UnidentifiedImageError as ui:
        print(f"Unvalid file format: {ui}")
    return []
