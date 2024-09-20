# angle_search.py
import numpy as np
from scipy.integrate import solve_ivp
from raketDyn import raketDyn

def test_angles():
    best_angle = None
    min_distance = float('inf')
    
    for theta_m in np.linspace(0, 2 * np.pi, 36):  # Testa vinklar från 0 till 360 grader
        initial_state = [0, 0, 0, 0]
        t_span = (0, 15)
        t_eval = np.linspace(0, 15, 1000)

        # Lös differentialekvationerna
        sol = solve_ivp(raketDyn, t_span, initial_state, args=(theta_m,), t_eval=t_eval)
        
        # Beräkna avståndet till målet
        final_x, final_y = sol.y[0][-1], sol.y[1][-1]
        distance = np.sqrt((final_x - 80)**2 + (final_y - 60)**2)
        
        if distance < min_distance:
            min_distance = distance
            best_angle = theta_m

    return best_angle
