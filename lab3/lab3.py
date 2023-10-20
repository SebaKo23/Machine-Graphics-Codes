from PIL import Image
import numpy as np

# zad 1
def rysuj_pasy_pionowe_szare(w, h, grub, zmiana_koloru):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    ile = int(w / grub)
    for k in range(ile):
        for g in range(grub):
            j = k * grub + g
            for i in range(h):
                tab[i, j] = (k + zmiana_koloru) % 256
    return Image.fromarray(tab)

def rysuj_ramke_przemiennie_szare(w, h, grub, zmiana_koloru):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    ile = int(min(w, h) / (grub * 2))
    for k in range(ile):
        tab[grub * k:h - grub * k, grub * k:w - grub * k] = (k + zmiana_koloru) % 256
    return Image.fromarray(tab)

def negatyw_szare(obraz):
    tab = np.asarray(obraz)
    h, w = tab.shape
    tab_neg = tab.copy()
    for i in range(h):
        for j in range(w):
            tab_neg[i, j] = 255 - tab[i, j]
    return Image.fromarray(tab_neg)

ob1_1 = rysuj_pasy_pionowe_szare(480, 320, 10, 35)
ob1_2 = rysuj_ramke_przemiennie_szare(480, 320, 10, 70)
ob1_1_neg = negatyw_szare(ob1_1)
ob1_2_neg = negatyw_szare(ob1_2)
ob1_1.save("obraz1_1.png")
ob1_1.save("obraz1_1.jpg")
ob1_2.save("obraz1_2.png")
ob1_2.save("obraz1_2.jpg")
ob1_1_neg.save("obraz1_1N.png")
ob1_1_neg.save("obraz1_1N.jpg")
ob1_2_neg.save("obraz1_2N.png")
ob1_2_neg.save("obraz1_2N.jpg")

# zad 2

def rysuj_pasy_pionowe_kolor(w, h, grub, kolor, zmiana_koloru):
    t = (h, w, 3)
    tab = np.zeros(t, dtype=np.uint8)
    tab[:] = kolor
    ile = int(w / grub)
    for k in range(ile):
        r = (kolor[0] + k * zmiana_koloru) % 256
        g = (kolor[1] + k * zmiana_koloru) % 256
        b = (kolor[2] + k * zmiana_koloru) % 256
        for g in range(grub):
            j = k * grub + g
            for i in range(h):
                tab[i, j] = [r, g, b]
    return Image.fromarray(tab)

def rysuj_ramke_przemiennie_kolor(w, h, grub, kolor, zmiana_koloru):
    t = (h, w, 3)
    tab = np.zeros(t, dtype=np.uint8)
    tab[:] = kolor
    ile = int(min(w, h) / (grub * 2))
    for k in range(ile):
        r = (kolor[0] + k * zmiana_koloru) % 256
        g = (kolor[1] + k * zmiana_koloru) % 256
        b = (kolor[2] + k * zmiana_koloru) % 256
        tab[grub * k:h - grub * k, grub * k:w - grub * k] = [r, g, b]
    return Image.fromarray(tab)

def negatyw_kolor(obraz):
    tab = np.asarray(obraz)
    h, w, kolor = tab.shape
    tab_neg = tab.copy()
    for i in range(h):
        for j in range(w):
            for k in range(kolor):
                tab_neg[i, j] = 255 - tab[i, j]
    return Image.fromarray(tab_neg)

obraz2 = rysuj_ramke_przemiennie_kolor(480, 320, 10, [255, 255, 128], 32)
obraz2N = negatyw_kolor(obraz2)
obraz2.save("obraz2.png")
obraz2.save("obraz2.jpg")
obraz2N.save("obraz2N.png")
obraz2N.save("obraz2N.jpg")

# zad 3
def koloruj_inicjaly(obraz, kolor, zmiana_koloru):
    t_obraz = np.asarray(obraz)
    h, w = t_obraz.shape
    t =(h, w, 3)
    tab = np.ones(t, dtype=np.uint8)
    tab[:] = kolor
    for i in range(h):
        r = (kolor[0] + i * zmiana_koloru) % 256
        g = (kolor[1] + i * zmiana_koloru) % 256
        b = (kolor[2] + i * zmiana_koloru) % 256
        for j in range(w):
            if t_obraz[i, j] == False:
                tab[i, j] = [r, g, b]
            else:
                tab[i, j] = [255, 255, 255]
    return Image.fromarray(tab)

inicjaly = Image.open("inicjaly.bmp")
kolorowe_inicjaly = koloruj_inicjaly(inicjaly, [128, 0, 128], 64)
kolorowe_inicjaly.show()