import matplotlib.image as mpimg
import numpy as np


def rgb_to_gray_lightness(img):
    max_val = np.max(img, axis=2)
    min_val = np.min(img, axis=2)
    gray_image = (max_val + min_val) / 2
    return gray_image


def rgb_to_gray_average(img):
    gray_image = np.mean(img, axis=2)
    return gray_image


def rgb_to_gray_luminosity(img):
    gray_image = 0.21 * img[:, :, 0] + 0.72 * \
        img[:, :, 1] + 0.07 * img[:, :, 2]
    return gray_image


img = mpimg.imread('Module2/Week1/dog.jpeg')

gray_img_lightness = rgb_to_gray_lightness(img)
print(gray_img_lightness[0, 0])

gray_img_average = rgb_to_gray_average(img)
print(gray_img_average[0, 0])

gray_img_luminosity = rgb_to_gray_luminosity(img)
print(gray_img_luminosity[0, 0])
