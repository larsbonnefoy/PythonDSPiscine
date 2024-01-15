from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_blue, ft_green, ft_grey

img = ft_load("landscape.jpg")
ft_invert(img)
ft_red(img)
ft_green(img)
ft_blue(img)
ft_grey(img)
print(ft_invert.__doc__)
