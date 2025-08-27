import cv2
from skimage import data, color
import matplotlib.pyplot as plt
import numpy as np
from skimage import img_as_float

img_rgb = img_as_float(data.astronaut())
img = color.rgb2gray(img_rgb)

def contrast_stretch_minmax(img):
    a, b = img.min(), img.max()
    stretched = (img - a) / (b - a)
    return stretched

def contrast_stretch_percentile(img, low, high):
    a, b = np.percentile(img, (low, high))
    stretched = np.clip(img, a, b)
    stretched = (stretched - a) / (b - a)
    return stretched

cs_minmax = contrast_stretch_minmax(img)
cs_p1 = contrast_stretch_percentile(img, 2, 98)
cs_p2 = contrast_stretch_percentile(img, 40, 60)

fig, axes = plt.subplots(1,4, figsize=(15,5))
axes[0].imshow(img, cmap="gray", vmin=0, vmax=1); axes[0].set_title("Original"); axes[0].axis("off")
axes[1].imshow(cs_minmax, cmap="gray", vmin=0, vmax=1); axes[1].set_title("Min–Max"); axes[1].axis("off")
axes[2].imshow(cs_p1, cmap="gray", vmin=0, vmax=1); axes[2].set_title("P2–98"); axes[2].axis("off")
axes[3].imshow(cs_p2, cmap="gray", vmin=0, vmax=1); axes[3].set_title("P20–80"); axes[3].axis("off")
plt.show()
