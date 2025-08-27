import matplotlib.pyplot as plt
from skimage import data, color, exposure, img_as_float

img_rgb = img_as_float(data.astronaut())
img_gray = color.rgb2gray(img_rgb)

log1 = exposure.adjust_log(img_gray, gain=0.5)
log2 = exposure.adjust_log(img_gray, gain=1.0)
log3 = exposure.adjust_log(img_gray, gain=2.0)
log4 = exposure.adjust_log(img_gray, gain=5.0)

fig, axes = plt.subplots(1,5, figsize=(15,5))
titles = ["Original","Log gain=0.5","Log gain=1","Log gain=2","Log gain=5"]
imgs   = [img_gray, log1, log2, log3, log4]

for ax, im, t in zip(axes, imgs, titles):
    ax.imshow(im, cmap="gray", vmin=0, vmax=1)
    ax.set_title(t)
    ax.axis("off")

plt.show()
