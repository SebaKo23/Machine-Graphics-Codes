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
print(inicjaly_bool)

# zad6a
inicjaly_uint8 = np.loadtxt("inicjaly.txt", dtype=np.uint8)
print(inicjaly_uint8)

inicjaly_uint8_obraz = Image.fromarray(inicjaly_uint8)
inicjaly_uint8_obraz.show()