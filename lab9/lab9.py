from PIL import Image
import numpy as np
from PIL import ImageChops, ImageOps
from PIL import ImageStat as stat
import matplotlib.pyplot as plt

# zad 1
obraz = Image.open("zeby.png")
print(obraz.mode)
obraz1 = obraz.convert('L')
print(obraz1.mode)


# zad 2
def histogram_norm(obraz):
    w, h = obraz.size
    N = w * h
    hist_norm = []
    histogram = obraz.histogram()
    for i in range(256):
        hist_norm.append(histogram[i] / N)
    return hist_norm


def histogram_cumul(histogram):
    hist_cumul = [histogram[0]]
    for i in range(1, 256):
        hist_cumul.append(hist_cumul[i - 1] + histogram[i])
    return hist_cumul


def histogram_equalizer(im):
    hist = histogram_norm(im)
    hist_cumulative = histogram_cumul(hist)
    im1 = im.point(lambda i: int(255 * hist_cumulative[i]))
    return im1


histogram1 = histogram_norm(obraz1)
plt.title("histogram1")
plt.bar(range(256), histogram1[:], color='b', alpha=0.8)
plt.show()

histogram2 = histogram_cumul(histogram1)
plt.title("histogram2")
plt.bar(range(256), histogram2[:], color='b', alpha=0.8)
plt.show()

eq = histogram_equalizer(obraz1)
eq.save("equalized.png")
histogram3 = eq.histogram()
plt.title("histogram3")
plt.bar(range(256), histogram3[:], color='b', alpha=0.8)
plt.show()

# zad 3
imEq = ImageOps.equalize(obraz1)
imEq.save("equalized1.png")


# zad 4
def konwertuj1(obraz, w_r, w_g, w_b):
    if not w_r + w_g + w_b == 1 or 0 <= w_r <= 1 or 0 <= w_g <= 1 or 0 <= w_b <= 1:
        return 0
    T = np.array(obraz)
    L = np.round(T[:, :, 0] * w_r + T[:, :, 1] * w_g + T[:, :, 2] * w_b).astype(np.uint8)
    return Image.fromarray(L, mode="L")


mgla = Image.open("mgla.jpg")
mgL1 = konwertuj1(mgla, 0.299, 0.587, 0.114)
mgL = mgla.convert("L")
