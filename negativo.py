import matplotlib.pyplot as plt
from skimage import data, color, util, img_as_float

img_rgb = img_as_float(data.astronaut())
img_gray = color.rgb2gray(img_rgb)

neg_rgb  = util.invert(img_rgb)
neg_gray = util.invert(img_gray)

fig, axes = plt.subplots(2,2, figsize=(10,8))
axes[0,0].imshow(img_rgb);  axes[0,0].set_title("RGB");  axes[0,0].axis("off")
axes[0,1].imshow(neg_rgb);  axes[0,1].set_title("RGB Negativo"); axes[0,1].axis("off")
axes[1,0].imshow(img_gray, cmap="gray", vmin=0, vmax=1); axes[1,0].set_title("Gray"); axes[1,0].axis("off")
axes[1,1].imshow(neg_gray, cmap="gray", vmin=0, vmax=1); axes[1,1].set_title("Gray Negativo"); axes[1,1].axis("off")
plt.tight_layout(); plt.show()
