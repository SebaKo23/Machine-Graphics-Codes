from PIL import Image
import numpy as np
from PIL import ImageOps
from PIL import ImageStat as stat
import matplotlib.pyplot as plt


def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe
    print("\n")


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


def histogram_equalization(im):
    hist = histogram_norm(im)
    hist_cumulative = histogram_cumul(hist)
    im1 = im.point(lambda i: int(255 * hist_cumulative[i]))
    return im1


eq = histogram_equalization(obraz1)
eq.save("equalized.png")

histogram0 = obraz1.histogram()
histogram1 = histogram_norm(obraz1)
histogram2 = histogram_cumul(histogram1)
histogram3 = eq.histogram()

plt.figure(figsize=(32, 16))
plt.subplot(2, 2, 1)
plt.title("histogram")
plt.bar(range(256), histogram0[:], color='b', alpha=0.8)
plt.axis('off')
plt.subplot(2, 2, 2)
plt.title("histogram znormalizowany")
plt.bar(range(256), histogram1[:], color='b', alpha=0.8)
plt.axis('off')
plt.subplot(2, 2, 3)
plt.title("histogram skumulowany")
plt.bar(range(256), histogram2[:], color='b', alpha=0.8)
plt.axis('off')
plt.subplot(2, 2, 4)
plt.title("histogram - po wyrównaniu")
plt.bar(range(256), histogram3[:], color='b', alpha=0.8)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.tight_layout()
plt.savefig("fig1.png")
plt.show()

print("Statystyki obraz1:")
print(statystyki(obraz1))
print("Statystyki obraz1 (po wyrównaniu):")
print(statystyki(eq))

# zad 3
imEq = ImageOps.equalize(obraz1)
imEq.save("equalized1.png")

print("Statystyki obraz1 (wyrównanie, funkcja equalize):")
print(statystyki(imEq))

plt.figure(figsize=(32, 16))
plt.subplot(1, 3, 1)
plt.title("obraz wejściowy")
plt.imshow(obraz1, "gray")
plt.axis('off')
plt.subplot(1, 3, 2)
plt.title("equalized")
plt.imshow(eq, "gray")
plt.axis('off')
plt.subplot(1, 3, 3)
plt.title("equalized1")
plt.imshow(imEq, "gray")
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.tight_layout()
plt.savefig("fig2.png")
plt.show()


# zad 4
def konwertuj1(obraz, w_r, w_g, w_b):
    if not (w_r + w_g + w_b == 1 or 0 <= w_r <= 1 or 0 <= w_g <= 1 or 0 <= w_b <= 1):
        raise ValueError("Nieprawidłowe wagi kanałów")
    T = np.array(obraz)
    L = np.round(T[:, :, 0] * w_r + T[:, :, 1] * w_g + T[:, :, 2] * w_b).astype(np.uint8)
    return Image.fromarray(L, mode="L")


def konwertuj2(obraz, w_r, w_g, w_b):
    if not (w_r + w_g + w_b == 1 or 0 <= w_r <= 1 or 0 <= w_g <= 1 or 0 <= w_b <= 1):
        raise ValueError("Nieprawidłowe wagi kanałów")
    T = np.array(obraz)
    L = np.rint(T[:, :, 0] * w_r + T[:, :, 1] * w_g + T[:, :, 2] * w_b).astype(np.uint8)
    return Image.fromarray(L, mode="L")


mgla = Image.open("mgla.jpg")
mgL1 = konwertuj1(mgla, 0.299, 0.587, 0.114)
mgL = mgla.convert("L")
mgL1.save("mgla_L1.png")
mgL.save("mgla_L.png")
print("Statystyki mgla1 (własny convert, np.round):")
print(statystyki(mgL1))
print("Statystyki mgla1 (wbudowana funkcja):")
print(statystyki(mgL))
mgL2 = konwertuj2(mgla, 0.299, 0.587, 0.114)
mgL2.save("mgla_L2.png")
print("Statystyki mgla1 (własny convert, np.rint):")
print(statystyki(mgL2))
