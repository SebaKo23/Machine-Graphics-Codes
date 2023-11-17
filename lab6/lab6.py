from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def zakres(w, h):
    return [(i, j) for i in range(w) for j in range(h)]

# zad 1
obraz = Image.open("obraz.jpg")
inicjaly = Image.open("inicjaly.bmp")

# zad 2
im1 = obraz.copy()
ini1 = inicjaly.copy()
w, h = obraz.size
x, y = inicjaly.size
def wstaw_inicjaly(obraz, inicjaly, m, n, kolor):
    for i, j in zakres(x, y):
        pix = inicjaly.getpixel((i, j))
        if i + m < w and j + n < h:
            if pix == 0:
                obraz.putpixel((i+m, j+n), kolor)
    return obraz

res = wstaw_inicjaly(im1, ini1, (w-x), (h-y), (255, 0, 0))
res.save("obraz1.png")

def rozjasnij_obraz_z_maska(obraz, inicjaly, m, n, x,y,z):
    im2 = obraz.copy()
    for i, j in zakres(x, y):
        if i + m < w and j + n < h:
            if inicjaly.getpixel((i, j)) == 0:
                p = obraz.getpixel((i + m, j + n))
                im2.putpixel((i + m, j + n), (p[0] + x, p[1] + y, p[2] + z))
    return im2

# zad 3
def wstaw_inicjaly_load(obraz, inicjaly, m, n, kolor):
    obrazpix = obraz.load()
    inicjalypix = inicjaly.load()
    for i, j in zakres(x, y):
        pix = inicjalypix[i, j]
        if i + m < w and j + n < h:
            if pix == 0:
                obraz.putpixel((i+m, j+n), kolor)
    return obraz

def rozjasnij_obraz_z_maska_load(obraz, inicjaly, m, n, x, y, z):
    im2 = obraz.copy()
    for i, j in zakres(x, y):
        if i + m < w and j + n < h:
            if inicjaly.getpixel((i, j)) == 0:
                p = obraz.getpixel((i + m, j + n))
                im2.putpixel((i + m, j + n), (p[0] + a, p[1] + b, p[2] + c))
    return im2

# zad 4
im4 = obraz.copy()
def kontrast(obraz, wsp_kontrastu):
    mn = ((255 + wsp_kontrastu) / 255) ** 2
    return obraz.point(lambda i: 128 + (i - 128) * mn)

def transformacja_logarytmiczna(obraz):
    return obraz.point(lambda i: 255 * np.log(1 + i / 255))

def filtr_liniowy(obraz, a, b):
    w, h = obraz.size
    pixele = obraz.load()
    for i, j in zakres(w, h):
        pixele[i, j] = (pixele[i, j][0]* a + b, pixele[i, j][1]* a + b, pixele[i, j][2]* a + b)

def transformacja_gamma(obraz, gamma):
    return obraz.point(lambda i: (i / 255) ** (1 / gamma) * 255)
# zad 6