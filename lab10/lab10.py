from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageFilter
from PIL import ImageChops
from PIL import ImageOps
from PIL import ImageStat as stat

# zad 1
obraz = Image.open("obraz.png")
print(obraz.size, obraz.mode)

w, h = obraz.size
s_w = 0.15
s_h = 0.27
resample_method = ['NEAREST', 'LANCZOS', 'BILINEAR', 'BICUBIC', 'BOX', 'HAMMING']
im_N = obraz.resize((int(w * s_w), int(h * s_h)), 0)
plt.figure(figsize=(20, 16))
i = 1
for t in range(6):
    file_name = "resample_" + str(resample_method[t])
    im_r = obraz.resize((int(w * s_w), int(h * s_h)), t)
    plt.subplot(6, 2, i)
    plt.title(str(file_name))
    plt.imshow(im_r)
    plt.axis('off')
    i += 1
    diff = ImageChops.difference(im_N, im_r)
    s = stat.Stat(diff)
    plt.subplot(6, 2, i)
    plt.title('srednia' + str(np.round(s.mean, 2)))
    plt.imshow(diff)
    plt.axis('off')
    i += 1
    plt.savefig("fig1.png")

# zad 2
