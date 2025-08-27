import matplotlib.pyplot as plt
import numpy as np
from skimage import data, color, img_as_float

img_rgb  = img_as_float(data.astronaut())
img_gray = color.rgb2gray(img_rgb)

def adjust_gamma_manual(x, gamma, gain=1.0):
    x = np.clip(x, 0.0, 1.0)
    return np.clip(gain * np.power(x, gamma), 0.0, 1.0)

g1 = adjust_gamma_manual(img_gray, 0.5)
g2 = adjust_gamma_manual(img_gray, 0.8)
g3 = adjust_gamma_manual(img_gray, 1.5)
g4 = adjust_gamma_manual(img_gray, 2.5)

fig, axes = plt.subplots(1,5, figsize=(15,5))
titles = ["Original","γ=0.5","γ=0.8","γ=1.5","γ=2.5"]
imgs   = [img_gray, g1, g2, g3, g4]

for ax, im, t in zip(axes, imgs, titles):
    ax.imshow(im, cmap="gray", vmin=0, vmax=1)
    ax.set_title(t)
    ax.axis("off")

plt.show()
