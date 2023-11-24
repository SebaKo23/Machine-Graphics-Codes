from PIL import Image
import math

im = Image.open('obraz.jpg')

def zakres(w, h):
    return [(i, j) for i in range(w) for j in range(h)]

# zad 1
def rysuj_kwadrat_max(obraz, m, n, k):  # m,n - srodek kwadratu, k - długość boku kwadratu
    obraz1 = obraz.copy()
    pix = obraz.load()
    pix1 = obraz1.load()
    d = int(k / 2)
    temp = [0, 0, 0]
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pixel = pix[x, y]
            temp[0] = max(temp[0], pixel[0])
            temp[1] = max(temp[1], pixel[1])
            temp[2] = max(temp[2], pixel[2])
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pix1[x, y] = (int(temp[0]), int(temp[1]), int(temp[2]))
    return obraz1

def rysuj_kwadrat_min(obraz, m, n, k):
    obraz1 = obraz.copy()
    pix = obraz.load()
    pix1 = obraz1.load()
    d = int(k / 2)
    temp = [0, 0, 0]
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pixel = pix[x, y]
            temp[0] = min(temp[0], pixel[0])
            temp[1] = min(temp[1], pixel[1])
            temp[2] = min(temp[2], pixel[2])
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pix1[x, y] = (int(temp[0]), int(temp[1]), int(temp[2]))
    return obraz1


rys_max = rysuj_kwadrat_max(im, 200, 100, 50)
rys_max2 = rysuj_kwadrat_max(rys_max, 400, 200, 100)
rys_max3 = rysuj_kwadrat_max(rys_max2, 800, 400, 200)
rys_max3.save("obraz1.png")

rys_min = rysuj_kwadrat_min(im, 200, 100, 50)
rys_min2 = rysuj_kwadrat_min(rys_min, 400, 200, 100)
rys_min3 = rysuj_kwadrat_min(rys_min2, 800, 400, 200)
rys_min3.save("obraz2.png")

# zad 2
def rysuj_kolo(obraz, m_s, n_s, m_k, n_k, r):
    obraz1 = obraz.copy()
    w, h = obraz.size
    for i, j in zakres(w, h):
        if (i-m_s)**2+(j-n_s)**2 < r**2: # wzór na koło o środku (m_s, n_s) i promieniu r
                kolor = obraz1.getpixel((i, j))
                if m_k+i-m_s < w and n_k+j-n_s < h:
                    obraz1.putpixel((m_k+i-m_s,n_k+j-n_s), kolor)
    return obraz1

rys_kolo = rysuj_kolo(im, 30, 30, 20, 400, 30)
rys_kolo.show()
rys_kolo1 = rysuj_kolo(rys_kolo, 30, 30, 20, 400, 30)
rys_kolo2 = rysuj_kolo(rys_kolo1, 30, 30, 20, 400, 30)
rys_kolo3 = rysuj_kolo(rys_kolo2, 30, 30, 20, 400, 30)
rys_kolo4 = rysuj_kolo(rys_kolo3, 30, 30, 20, 400, 30)
rys_kolo5 = rysuj_kolo(rys_kolo4, 30, 30, 20, 400, 30)