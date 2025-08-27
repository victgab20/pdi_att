import matplotlib.pyplot as plt
from skimage import data, color, exposure, img_as_float

img_rgb  = img_as_float(data.astronaut())
img_gray = color.rgb2gray(img_rgb)

g1 = exposure.adjust_gamma(img_gray, gamma=0.5)
g2 = exposure.adjust_gamma(img_gray, gamma=0.8)
g3 = exposure.adjust_gamma(img_gray, gamma=1.5)
g4 = exposure.adjust_gamma(img_gray, gamma=2.5)

fig, axes = plt.subplots(1,5, figsize=(15,5))
titles = ["Original","γ=0.5","γ=0.8","γ=1.5","γ=2.5"]
imgs   = [img_gray, g1, g2, g3, g4]

for ax, im, t in zip(axes, imgs, titles):
    ax.imshow(im, cmap="gray", vmin=0, vmax=1)
    ax.set_title(t)
    ax.axis("off")

plt.show()
