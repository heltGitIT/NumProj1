from krafter import krafter
from massa import massa
import numpy as np
from tetaFunc import tetaFunc
km = 700

def raketDyn(t, state, tetaFunc):
    x, y, hx, hy = state
    m = massa(t)
    teta = tetaFunc(t, state)
    ux = km * np.cos(teta)
    uy = km * np.sin(teta)
    Kx, Ky = krafter(hx, hy, t)
    ax = (Kx + ux * 0.4) / m
    ay = (Ky + uy * 0.4) / m
    return [hx, hy, ax, ay]
