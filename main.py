import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from raketDyn import raketDyn
from tetaFunc import tetaFunc
from testVinkel import test_angles
# Initiala värden
x0, y0 = 0, 0
hx0, hy0 = 0, 0
initial_state = [x0, y0, hx0, hy0]


t_s = (0, 15)
t_e = np.linspace(0, 15, 1000)

# lösa diffekvationen mha solve_ivp
sol = solve_ivp(raketDyn, t_s, initial_state, args=(tetaFunc,), t_e=t_e, method='RK45') #Runge-Kutta

# hämta lösningen
x_varden = sol.y[0]
y_varden = sol.y[1]

# Plotta banan för raketen
plt.plot(x_varden, y_varden)

plt.scatter([80], [60], color='green', label='Mål')

plt.title('Raketens bana')

plt.xlabel('x (i meter)')

plt.ylabel('y (i meter)')

plt.grid()

plt.legend()

plt.show()
