import numpy as np
from massa import massa  

g = 9.82
konstant = 0.05

def krafter(hx, hy, t):
    m = massa(t)
    h = np.sqrt(hx**2 + hy**2)
    Kx = -konstant * h * hx
    Ky = -konstant * h * hy - m * g
    return np.array([Kx, Ky])
