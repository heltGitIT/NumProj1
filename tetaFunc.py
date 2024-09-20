import numpy as np



def tetaFunc(t, state):
    x, y, vx, vy = state
    mal_x, mal_y = 80, 60
    angle_to_mal = np.arctan2(mal_y - y, mal_x - x)

    if y < 20:
        return np.pi / 2  # Raketen körs tills den är på 20 meter
    else:
        return np.arctan2(mal_y - y, mal_x - x)  # vinkeln till målet som raketen ska till
