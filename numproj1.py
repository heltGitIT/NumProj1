import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)
c = 0.05  # Air resistance coefficient (kg/m)
Ev = 700  # Exhaust velocity (m/s)
burn_rate = 0.4  # Fuel burn rate (kg/s)
initial_mass = 8.0  # Initial mass (kg)
fuel_mass = 4.0  # Total fuel mass (kg)
target_x = 80.0  # Target distance (m)
target_y = 60.0  # Target height (m)

# Define the dynamic angle of thrust
def theta_dynamic(t, state):
    y_pos = state[2]  # Rocket's height
    x_pos = state[0]  # Rocket's x-position

    # If below 20 meters, fly straight up
    if y_pos < 20.0:
        return np.pi / 2  # 90 degrees, straight up
    
    # Adjust the angle if the rocket is near the target height
    if y_pos >= 55.0:
        dx = target_x - x_pos
        dy = target_y - y_pos
        angle_adjustment = 935.8* np.pi / 180  # Convert to radians for adjustment
        return np.arctan2(dy, dx) + angle_adjustment

    # Otherwise, aim towards the target
    dx = target_x - x_pos
    dy = target_y - y_pos
    return np.arctan2(dy, dx)

# Define the ODEs for the rocket's motion
def rocket_ode(t, state):
    x, vx, y, vy = state

    # Determine mass
    if t <= 10.0:
        m = initial_mass - burn_rate * t
    else:
        m = initial_mass - fuel_mass

    F_gravity = m * g
    F_drag_x = -c * vx * np.sqrt(vx**2 + vy**2)
    F_drag_y = -c * vy * np.sqrt(vx**2 + vy**2)

    angle = theta_dynamic(t, state)  # Use the new dynamic angle function

    # Thrust dynamics
    if y >= target_y:
        m_dot = 0
    elif t <= 10.0:
        m_dot = burn_rate
    else:
        m_dot = 0

    F_thrust_x = m_dot * Ev * np.cos(angle)
    F_thrust_y = m_dot * Ev * np.sin(angle)

    # Calculate accelerations
    ax = (F_thrust_x + F_drag_x) / m
    ay = (F_thrust_y - F_gravity + F_drag_y) / m

    return [vx, ax, vy, ay]

# Implementing the RK4 method
def runge_kutta4(ode_func, y0, t_span, dt):
    t0, tf = t_span
    t = t0
    state = np.array(y0, dtype=float)  # Ensure the state is a float array
    time_points = []
    states = []

    while t < tf:
        time_points.append(t)
        states.append(state.copy())
        
        k1 = np.array(ode_func(t, state), dtype=float)  # Ensure k1 is float
        k2 = np.array(ode_func(t + dt / 2, state + dt / 2 * k1), dtype=float)  # Ensure k2 is float
        k3 = np.array(ode_func(t + dt / 2, state + dt / 2 * k2), dtype=float)  # Ensure k3 is float
        k4 = np.array(ode_func(t + dt, state + dt * k3), dtype=float)  # Ensure k4 is float

        state += dt / 6 * (k1 + 2*k2 + 2*k3 + k4)  # Update state
        t += dt  # Increment time

    return np.array(time_points), np.array(states)

# Run the simulation using the RK4 method
initial_state = [0, 0, 0, 0]  # Start at (0,0) with zero velocity
t_span = (0, 5)  # Simulation time span
dt = 0.1  # Time step for RK4

# Get results from the RK4 solver
time_points, states = runge_kutta4(rocket_ode, initial_state, t_span, dt)

# Extract x and y positions
x_positions = states[:, 0]
y_positions = states[:, 2]

# Plot the trajectory
plt.figure(figsize=(10, 6))
plt.plot(x_positions, y_positions, label="Rocket trajectory (RK4)")

# Mark the target position
plt.plot(target_x, target_y, 'ro', label='Target', markersize=10)

# Add labels and title
plt.xlabel('Horizontal Position (m)')
plt.ylabel('Vertical Position (m)')
plt.title('Rocket Trajectory using RK4 with Dynamic Angle')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
