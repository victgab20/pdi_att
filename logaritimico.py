import matplotlib.pyplot as plt
import numpy as np
from skimage import data, color, img_as_float

img_rgb  = img_as_float(data.astronaut())
img_gray = color.rgb2gray(img_rgb)

def adjust_log_manual(x, gain=1.0):
    x = np.clip(x, 0.0, 1.0)
    y = np.log1p(x) / np.log(2.0)
    y = gain * y
    return np.clip(y, 0.0, 1.0)

log1 = adjust_log_manual(img_gray, gain=0.5)
log2 = adjust_log_manual(img_gray, gain=1.0)
log3 = adjust_log_manual(img_gray, gain=2.0)
log4 = adjust_log_manual(img_gray, gain=5.0)

fig, axes = plt.subplots(1,5, figsize=(15,5))
titles = ["Original","Log gain=0.5","Log gain=1","Log gain=2","Log gain=5"]
imgs   = [img_gray, log1, log2, log3, log4]

for ax, im, t in zip(axes, imgs, titles):
    ax.imshow(im, cmap="gray", vmin=0, vmax=1)
    ax.set_title(t)
    ax.axis("off")

plt.show()
