from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt
from random import randint

# zad 1
im3png = Image.open("im3.png")
im3jpg = Image.open("im3.jpg")
diff = ImageChops.difference(im3png, im3jpg)
diff.save("diff.png")

def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema) # max i min
    print("count ", s.count) # zlicza
    print("mean ", s.mean) # srednia
    print("median ", s.median) # mediana
    print("stddev ", s.stddev) # odchylenie standardowe

statystyki(diff)

hist = diff.histogram()
p=0
print(hist[p])
print(hist[256+p])
print(hist[2*256+p])

def rysuj_histogram_RGB(obraz):
    hist = obraz.histogram()
    plt.title("histogram")
    plt.bar(range(256), hist[:256], color='r', alpha=0.5)
    plt.bar(range(256), hist[256:2 * 256], color='g', alpha=0.4)
    plt.bar(range(256), hist[2*256:], color='b', alpha=0.3)
    plt.show()

rysuj_histogram_RGB(diff)

def zlicz_roznice_srednia_RGB(obraz, wsp):
    t_obraz = np.asarray(obraz)
    h, w, d = t_obraz.shape
    zlicz = 0
    for i in range(h):
        for j in range(w):
                if np.mean(t_obraz[i, j, :]) > wsp:
                    zlicz = zlicz + 1
    procent = zlicz/(h*w)
    return zlicz, procent

def zlicz_roznice_suma_RGB(obraz, wsp):
    t_obraz = np.asarray(obraz)
    h, w, d = t_obraz.shape
    zlicz = 0
    for i in range(h):
        for j in range(w):
                if sum(t_obraz[i, j, :]) > wsp:
                    if (t_obraz[i, j, 0] + t_obraz[i, j, 1] + t_obraz[i, j, 2]) > wsp:
                        zlicz = zlicz + 1
    procent = zlicz/(h*w)
    return zlicz, procent

wsp = 10
zlicz, procent = zlicz_roznice_srednia_RGB(diff, wsp)
print('liczba niepasujących pikseli = ' , zlicz)
print('procent niepasujących pikseli = ' , procent)
zlicz1, procent1 = zlicz_roznice_suma_RGB(diff, wsp)
print('liczba niepasujących pikseli = ' , zlicz1)
print('procent niepasujących pikseli = ' , procent1)

zlicz, procent = zlicz_roznice_srednia_RGB(diff, wsp)
print('liczba niepasujących pikseli = ' , zlicz)
print('procent niepasujących pikseli = ' , procent)
zlicz1, procent1 = zlicz_roznice_suma_RGB(diff, wsp)
print('liczba niepasujących pikseli = ' , zlicz1)
print('procent niepasujących pikseli = ' , procent1)

# zad 2
obraz = Image.open("obraz.jpg")
obraz.save("obraz1.jpg")
obraz1 = Image.open("obraz1.jpg")
obraz1.save("obraz2.jpg")
obraz2 = Image.open("obraz2.jpg")
obraz2.save("obraz3.jpg")
obraz3 = Image.open("obraz3.jpg")
obraz3.save("obraz4.jpg")
obraz4 = Image.open("obraz4.jpg")
obraz4.save("obraz5.jpg")

# zad 3
# def odkoduj(obraz1, obraz2):
#     odkoduj1 = np.asarray(obraz1)
#     odkoduj2 = np.asarray(obraz2)
#     h, w, d = odkoduj1.shape
#     for i in range(h):
#         for j in range(w):
