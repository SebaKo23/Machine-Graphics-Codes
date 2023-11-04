from PIL import Image
import numpy as np
from PIL import ImageChops
import matplotlib.pyplot as plt

# zad 1
im1 = Image.open('obraz.jpg')
h, w = im1.size
t = (h, w)

# zad 2
T = np.array(im1)
t_r = T[:, :, 0]
t_g = T[:, :, 1]
t_b = T[:, :, 2]
im_r = Image.fromarray(t_r)
im_g = Image.fromarray(t_g)
im_b = Image.fromarray(t_b)
im2 = Image.merge('RGB', (im_r, im_g, im_b))
diff_im = ImageChops.difference(im1, im2)
plt.figure(figsize=(32, 16))
plt.subplot(3, 1, 1)
plt.imshow(im1)
plt.axis('off')
plt.subplot(3, 1, 2)
plt.imshow(im2)
plt.axis('off')
plt.subplot(3, 1, 3)
plt.imshow(diff_im)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig("fig1.png")
plt.show()

# zad 3
r, g, b = im1.split()
im3 = Image.merge('RGB', (g, b, r))
im3.save("im3.jpg")
im3.save("im3.png")
im3j = Image.open("im3.jpg")
im3p = Image.open("im3.png")
diff_im3 = ImageChops.difference(im3j, im3p)
plt.figure(figsize=(32, 16))
plt.subplot(3, 1, 1)
plt.imshow(im3j)
plt.axis('off')
plt.subplot(3, 1, 2)
plt.imshow(im3p)
plt.axis('off')
plt.subplot(3, 1, 3)
plt.imshow(diff_im3)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig("fig2.png")
plt.show()

# zad 4
ob1_1j = Image.open("obraz1_1.jpg")
ob1_1p = Image.open("obraz1_1.png")
ob1_1Nj = Image.open("obraz1_1N.jpg")
ob1_1Np = Image.open("obraz1_1N.png")
ob1_2j = Image.open("obraz1_2.jpg")
ob1_2p = Image.open("obraz1_2.png")
ob1_2Nj = Image.open("obraz1_2N.jpg")
ob1_2Np = Image.open("obraz1_2N.png")
diff_ob1_1 = ImageChops.difference(ob1_1j, ob1_1p)
diff_ob1_1N = ImageChops.difference(ob1_1Nj, ob1_1Np)
diff_ob1_2 = ImageChops.difference(ob1_2j, ob1_2p)
diff_ob1_2N = ImageChops.difference(ob1_2Nj, ob1_2Np)
plt.figure(figsize=(32, 16))
plt.subplot(4, 3, 1)
plt.imshow(ob1_1j, 'gray')
plt.axis('off')
plt.subplot(4, 3, 2)
plt.imshow(ob1_1p, 'gray')
plt.axis('off')
plt.subplot(4, 3, 3)
plt.imshow(diff_ob1_1, 'gray')
plt.axis('off')
plt.subplot(4, 3, 4)
plt.imshow(ob1_1Nj, 'gray')
plt.axis('off')
plt.subplot(4, 3, 5)
plt.imshow(ob1_1Np, 'gray')
plt.axis('off')
plt.subplot(4, 3, 6)
plt.imshow(diff_ob1_1N, 'gray')
plt.axis('off')
plt.subplot(4, 3, 7)
plt.imshow(ob1_2j, 'gray')
plt.axis('off')
plt.subplot(4, 3, 8)
plt.imshow(ob1_2p, 'gray')
plt.axis('off')
plt.subplot(4, 3, 9)
plt.imshow(diff_ob1_2, 'gray')
plt.axis('off')
plt.subplot(4, 3, 10)
plt.imshow(ob1_2Nj, 'gray')
plt.axis('off')
plt.subplot(4, 3, 11)
plt.imshow(ob1_2Np, 'gray')
plt.axis('off')
plt.subplot(4, 3, 12)
plt.imshow(diff_ob1_2N, 'gray')
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig("fig3.png")
plt.show()


# zad 5
def rysuj_ramke_przemiennie_szare(grub, zmiana_koloru):
    tab = np.zeros(t, dtype=np.uint8)
    ile = int(min(w, h) / (grub * 2))
    for k in range(ile):
        tab[grub * k:h - grub * k, grub * k:w - grub * k] = (k + zmiana_koloru) % 256
    return Image.fromarray(tab)


im4 = rysuj_ramke_przemiennie_szare(5, 100)
im4 = im4.resize(im1.size)
im4_r = Image.merge('RGB', (im4, g, b))
im4_g = Image.merge('RGB', (r, im4, b))
im4_b = Image.merge('RGB', (r, g, im4))
plt.figure(figsize=(32, 16))
plt.subplot(3, 1, 1)
plt.imshow(im4_r)
plt.axis('off')
plt.subplot(3, 1, 2)
plt.imshow(im4_g)
plt.axis('off')
plt.subplot(3, 1, 3)
plt.imshow(im4_b)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig("fig4.png")
plt.show()


# zad 6
def square(size):
    s_tab = np.zeros(t, dtype=np.uint8)
    x_start = (w - size) // 2
    x_end = x_start + size
    y_start = (h - size) // 2
    y_end = y_start + size
    s_tab[y_start:y_end, x_start:x_end] = 1 * 255
    return Image.fromarray(s_tab)


def circle(radius):
    c_tab = np.zeros(t, dtype=np.uint8)
    mid_x = w // 2
    mid_y = h // 2
    y, x = np.ogrid[:h, :w]
    mask = (x - mid_x) ** 2 + (y - mid_y) ** 2 <= radius ** 2
    c_tab[mask] = 1 * 255
    return Image.fromarray(c_tab)


def diamond(size):
    d_tab = np.zeros(t, dtype=np.uint8)
    mid_x = w // 2
    mid_y = h // 2
    y, x = np.ogrid[:h, :w]
    mask1 = abs(x - mid_x) + abs(y - mid_y) <= size // 2
    mask2 = abs(x - mid_x) + abs(y - mid_y) <= size // 2
    d_tab[mask1 & mask2] = 1 * 255
    return Image.fromarray(d_tab)


s = square(300)
c = circle(300)
d = diamond(300)
im5scd = Image.merge('RGB', (s, c, d))
im5sdc = Image.merge('RGB', (s, d, c))
im5dsc = Image.merge('RGB', (d, s, c))
im5dcs = Image.merge('RGB', (d, c, s))
im5csd = Image.merge('RGB', (c, s, d))
im5cds = Image.merge('RGB', (c, d, s))
plt.figure(figsize=(32, 16))
plt.subplot(2, 3, 1)
plt.imshow(im5scd)
plt.axis('off')
plt.subplot(2, 3, 2)
plt.imshow(im5sdc)
plt.axis('off')
plt.subplot(2, 3, 3)
plt.imshow(im5dsc)
plt.axis('off')
plt.subplot(2, 3, 4)
plt.imshow(im5dcs)
plt.axis('off')
plt.subplot(2, 3, 5)
plt.imshow(im5csd)
plt.axis('off')
plt.subplot(2, 3, 6)
plt.imshow(im5cds)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig("fig5.png")
plt.show()
