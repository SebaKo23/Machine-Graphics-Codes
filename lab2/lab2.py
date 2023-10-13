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

def rysuj_ramke(w, h, grub):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    for i in range(h):
         tab[grub:h - grub, grub:w - grub] = 1
    tab1 = tab.astype(np.bool_)
    return tab1

tab = rysuj_ramke(480, 320, 10)
im_ramka = Image.fromarray(tab)
im_ramka.show()
