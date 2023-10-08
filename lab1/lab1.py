from PIL import Image
import numpy as np

# zad2
inicjaly = Image.open("inicjaly.bmp")
print("---------- informacje o obrazie ----------")
print("tryb:", inicjaly.mode)
print("format:", inicjaly.format)
print("rozmiar:", inicjaly.size)

# zad3
inicjaly2 = Image.open("inicjaly.bmp")
obraz_text = np.asarray(inicjaly2)
obraz_text = obraz_text * 1
inicjaly_text = open('inicjaly.txt', 'w')
for rows in obraz_text:
    for item in rows:
        inicjaly_text.write(str(item) + ' ')
    inicjaly_text.write('\n')

inicjaly_text.close()

# zad4a
dane_obrazka = np.asarray(inicjaly)
print("---------------- informacje o tablicy obrazu----------------")
print("typ danych tablicy:", dane_obrazka.dtype)
print("rozmiar tablicy:", dane_obrazka.shape)
print("liczba elementow:", dane_obrazka.size)
print("wymiar tablicy:", dane_obrazka.ndim)
print("rozmiar wyrazu tablicy:", dane_obrazka.itemsize)
print("***************************************")

# 4b
print("(50,30)", dane_obrazka[30][50])
print("(90,40)", dane_obrazka[40][90])
print("(99,0)", dane_obrazka[0][99])

# zad5
inicjaly_bool = np.loadtxt("inicjaly.txt", dtype=np.bool_)
print("---------------- informacje o tablicy obrazu (bool)----------------")
print("typ danych tablicy:", inicjaly_bool.dtype)
print("rozmiar tablicy:", inicjaly_bool.shape)
print("liczba elementow:", inicjaly_bool.size)
print("wymiar tablicy:", inicjaly_bool.ndim)
print("rozmiar wyrazu tablicy:", inicjaly_bool.itemsize)
print("***************************************")

# zad6a
inicjaly_uint8 = np.loadtxt("inicjaly.txt", dtype=np.uint8)
print("---------------- informacje o tablicy obrazu (uint8)----------------")
print("typ danych tablicy:", inicjaly_uint8.dtype)
print("rozmiar tablicy:", inicjaly_uint8.shape)
print("liczba elementow:", inicjaly_uint8.size)
print("wymiar tablicy:", inicjaly_uint8.ndim)
print("rozmiar wyrazu tablicy:", inicjaly_uint8.itemsize)
print("***************************************")

inicjaly_uint8_obraz = Image.fromarray(inicjaly_uint8)
print("---------- informacje o obrazie uint8 ----------")
print("tryb:", inicjaly_uint8_obraz.mode)
print("format:", inicjaly_uint8_obraz.format)
print("rozmiar:", inicjaly_uint8_obraz.size)
inicjaly_uint8_obraz.show()
