from PIL import Image
import numpy as np


def wytnij_fragment_obrazu(obraz, m_p, n_p, m_k, n_k):
    if m_p >= m_k or n_p >= n_k:
        raise ValueError("Podano niewłaściwe współrzędne")
    tab_obraz = np.array(obraz)
    h, w = tab_obraz.shape
    m_p = max(0, min(m_p, h - 1))
    n_p = max(0, min(n_p, w - 1))
    m_k = max(0, min(m_k, h))
    n_k = max(0, min(n_k, w))
    fragment = tab_obraz[m_p:m_k, n_p:n_k]
    fragment = fragment.astype(bool)
    return Image.fromarray(fragment)


inicjaly = Image.open("inicjaly.bmp")
first_letter = wytnij_fragment_obrazu(inicjaly, 0, 0, 49, 43)
second_letter = wytnij_fragment_obrazu(inicjaly, 0, 43, 49, 99)
first_letter.save("pierwsza_litera.bmp")
second_letter.save("druga_litera.bmp")
