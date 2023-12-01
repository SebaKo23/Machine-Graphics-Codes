from PIL import Image
from PIL import ImageFilter
from PIL import ImageChops
import matplotlib.pyplot as plt

obraz = Image.open("obraz.jpg")


# zad 1


def filtruj(obraz, kernel, scale):
    im1 = obraz.copy()
    im_pix = obraz.load()
    im1_pix = im1.load()
    w, h = obraz.size
    k = len(kernel)
    d = int(k / 2)
    for x in range(d, w - d):
        for y in range(d, h - d):
            temp = [0, 0, 0]
            for a in range(k):
                for b in range(k):
                    xn = x + a - d
                    yn = y + b - d
                    pixel = im_pix[xn, yn]
                    temp[0] += pixel[0] * kernel[a][b]
                    temp[1] += pixel[1] * kernel[a][b]
                    temp[2] += pixel[2] * kernel[a][b]
            im1_pix[x, y] = (int(temp[0] / scale), int(temp[1] / scale), int(temp[2] / scale))
    return im1


kern = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
skala = 1
fi = filtruj(obraz, kern, skala)

fi.show()

# zad 2
imB = obraz.filter(ImageFilter.BLUR)
print(ImageFilter.BLUR.filterargs)
kern1 = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
imB1 = filtruj(obraz, kern1, 16)
imB1.show()

# zad 3
imL = obraz.convert('L')
imL1 = imL.filter(ImageFilter.EMBOSS)
print(ImageFilter.EMBOSS.filterargs)
# ImageFilter.EMBOSS.filterargs =
