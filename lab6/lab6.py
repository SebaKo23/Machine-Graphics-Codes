from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def zakres(e, r):
    return [(i, j) for i in range(e) for j in range(r)]


# zad 1
obraz = Image.open("obraz.jpg")
inicjaly = Image.open("inicjaly.bmp")

# zad 2
im1 = obraz.copy()
ima1 = obraz.copy()
ini1 = inicjaly.copy()
w, h = obraz.size
u, o = inicjaly.size


def wstaw_inicjaly(obraz, inicjaly, m, n, kolor):
    for i, j in zakres(u, o):
        if i + m < w and j + n < h:
            if inicjaly.getpixel((i, j)) == 0:
                obraz.putpixel((i + m, j + n), kolor)
    return obraz


res = wstaw_inicjaly(im1, ini1, (w - u), (h - o), (255, 0, 0))
res.save("obraz1.png")


def rozjasnij_obraz_z_maska(obraz, inicjaly, m, n, x, y, z):
    im2 = obraz.copy()
    for i, j in zakres(u, o):
        if i + m < w and j + n < h:
            if inicjaly.getpixel((i, j)) == 0:
                p = obraz.getpixel((i + m, j + n))
                im2.putpixel((i + m, j + n), (p[0] + x, p[1] + y, p[2] + z))
    return im2


res2 = rozjasnij_obraz_z_maska(ima1, ini1, (w // 2), (h // 2), 64, 128, 128)
res2.save("obraz2.png")


# zad 3
def wstaw_inicjaly_load(obraz, inicjaly, m, n, kolor):
    obrazpix = obraz.load()
    inicjalypix = inicjaly.load()
    for i, j in zakres(u, o):
        if i + m < w and j + n < h:
            if inicjalypix[i, j] == 0:
                obrazpix[i + m, j + n] = kolor
    return obraz


def rozjasnij_obraz_z_maska_load(obraz, inicjaly, m, n, x, y, z):
    im2 = obraz.copy()
    obrazpix = obraz.load()
    inicjalypix = inicjaly.load()
    im2pix = im2.load()
    for i, j in zakres(u, o):
        if i + m < w and j + n < h:
            if inicjalypix[i, j] == 0:
                p = obrazpix[i + m, j + n]
                im2pix[i + m, j + n] = (p[0] + x, p[1] + y, p[2] + z)
    return im2


# zad 4
im4 = obraz.copy()
imline = obraz.copy()


def kontrast(obraz, wsp_kontrastu):
    mn = ((255 + wsp_kontrastu) / 255) ** 2
    return obraz.point(lambda i: 128 + (i - 128) * mn)


kontrast1 = kontrast(im4, 32)
kontrast2 = kontrast(im4, 64)
kontrast3 = kontrast(im4, 128)

plt.figure(figsize=(32, 16))
plt.subplot(2, 2, 1)
plt.imshow(im4)
plt.axis('off')
plt.subplot(2, 2, 2)
plt.imshow(kontrast1)
plt.axis('off')
plt.subplot(2, 2, 3)
plt.imshow(kontrast2)
plt.axis('off')
plt.subplot(2, 2, 4)
plt.imshow(kontrast3)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig("fig1.png")
plt.show()


def transformacja_logarytmiczna(obraz):
    return obraz.point(lambda i: 255 * np.log(1 + i / 255))


def filtr_liniowy(obraz, a, b):
    w, h = obraz.size
    pixele = obraz.load()
    for i, j in zakres(w, h):
        pixele[i, j] = (pixele[i, j][0] * a + b, pixele[i, j][1] * a + b, pixele[i, j][2] * a + b)
    return obraz


transform = transformacja_logarytmiczna(im4)
filtr = filtr_liniowy(imline, 2, -100)

plt.figure(figsize=(32, 16))
plt.subplot(3, 1, 1)
plt.imshow(im4)
plt.axis('off')
plt.subplot(3, 1, 2)
plt.imshow(transform)
plt.axis('off')
plt.subplot(3, 1, 3)
plt.imshow(filtr)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig("fig2.png")
plt.show()


def transformacja_gamma(obraz, gamma):
    return obraz.point(lambda i: (i / 255) ** (1 / gamma) * 255)


gamma1 = transformacja_gamma(im4, 4.4)
gamma2 = transformacja_gamma(im4, 10)
gamma3 = transformacja_gamma(im4, 30.5)

plt.figure(figsize=(32, 16))
plt.subplot(2, 2, 1)
plt.imshow(im4)
plt.axis('off')
plt.subplot(2, 2, 2)
plt.imshow(gamma1)
plt.axis('off')
plt.subplot(2, 2, 3)
plt.imshow(gamma2)
plt.axis('off')
plt.subplot(2, 2, 4)
plt.imshow(gamma3)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig("fig3.png")
plt.show()


# zad 6
def rozjasnij(obraz):
    T = np.array(obraz, dtype='uint8')
    for rr in range(T.shape[0]):
        for gg in range(T.shape[1]):
            for bb in range(T.shape[2]):
                if T[rr, gg, bb] + 100 > 255:
                    T[rr, gg, bb] = 255
                else:
                    T[rr, gg, bb] += 100
    return Image.fromarray(T, "RGB")
