from PIL import Image
import numpy as np

inicjaly = Image.open("inicjaly.bmp")


# zad 1
def rysuj_ramke_w_obrazie(obraz, grub):
    tab_obraz = np.asarray(obraz) * 1
    h, w = tab_obraz.shape
    for i in range(h):
        for j in range(grub):
            tab_obraz[i][j] = 0
        for j in range(w - grub, w):
            tab_obraz[i][j] = 0
    for j in range(w):
        for i in range(grub):
            tab_obraz[i][j] = 0
        for i in range(h - grub, h):
            tab_obraz[i][j] = 0
    tab = tab_obraz.astype(bool)
    return Image.fromarray(tab)


# zad 2
ramka10 = rysuj_ramke_w_obrazie(inicjaly, 10)
ramka5 = rysuj_ramke_w_obrazie(inicjaly, 5)
ramka5.save("ramka5.bmp")
ramka10.save("ramka10.bmp")


# zad 3.1

def rysuj_ramke_przemiennie(w, h, grub):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    ile = int(min(w, h) / (grub * 2))
    for k in range(ile):
        tab[grub * k:h - grub * k, grub * k:w - grub * k] = k % 2
    tab1 = tab.astype(np.bool_)
    return tab1


# zad 3.2
def rysuj_pasy_pionowe(w, h, grub):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    ile = int(w / grub)
    for k in range(ile):
        for g in range(grub):
            j = k * grub + g
            for i in range(h):
                tab[i, j] = k % 2
    tab1 = tab.astype(np.bool_)
    return tab1


# zad 3.3
def rysuj_styczne_prostokaty(w, h, m, n):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    tab[:n, :m] = 0
    tab[n:, m:] = 0
    tab1 = tab.astype(np.bool_)
    return tab1


# zad 3.4
def rysuj_przeplot_poziomy(w, h, grub):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    ile = int(h / grub)
    for k in range(ile):
        for g in range(grub):
            i = k * grub + g
            for j in range(w):
                tab[i, j] = (k + g) % 2
    tab1 = tab.astype(np.bool_)
    return tab1


# zad 4
ob1 = rysuj_ramke_przemiennie(480, 320, 10)
ob2 = rysuj_pasy_pionowe(480, 320, 10)
ob3 = rysuj_styczne_prostokaty(480, 320, 100, 50)
ob4 = rysuj_przeplot_poziomy(480, 320, 10)
obraz1 = Image.fromarray(ob1)
obraz2 = Image.fromarray(ob2)
obraz3 = Image.fromarray(ob3)
obraz4 = Image.fromarray(ob4)
obraz1.save("obraz1.bmp")
obraz2.save("obraz2.bmp")
obraz3.save("obraz3.bmp")
obraz4.save("obraz4.bmp")


# zad 5
def wstaw_obraz_w_obraz(obraz_bazowy, obraz_wstawiany, m, n):
    tab_obraz_bazowy = np.asarray(obraz_bazowy) * 1
    tab_obraz_wstawiany = np.asarray(obraz_wstawiany) * 1
    h0, w0 = tab_obraz_wstawiany.shape
    h, w = tab_obraz_bazowy.shape
    n_k = min(h, n + h0)
    m_k = min(w, m + w0)
    n_p = max(0, n)
    m_p = max(0, m)
    for i in range(n_p, n_k):
        for j in range(m_p, m_k):
            tab_obraz_bazowy[i][j] = tab_obraz_wstawiany[i - n][j - m]
    tab_obraz_bazowy = tab_obraz_bazowy.astype(bool)
    return Image.fromarray(tab_obraz_bazowy)


ob_bazowy1 = Image.open("obraz2.bmp")
ob_bazowy2 = Image.open("obraz4.bmp")
ob_wstawiany = Image.open("inicjaly.bmp")
wstaw1 = wstaw_obraz_w_obraz(ob_bazowy1, ob_wstawiany, 300, 90)
wstaw2 = wstaw_obraz_w_obraz(ob_bazowy2, ob_wstawiany, 10, 290)
wstaw1.save("wstaw1.bmp")
wstaw2.save("wstaw2.bmp")
