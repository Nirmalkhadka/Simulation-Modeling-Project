# Imports the tkinter module, which is the standard GUI (Graphical User Interface) toolkit for Python.
import tkinter as tk
# The ttk module provides access to themed Tkinter widgets with a modern look and feel.
from tkinter import ttk

# Imports the matplotlib.pyplot module, which is used for creating visualizations such as plots and charts.
import matplotlib.pyplot as plt

# This class is necessary for embedding Matplotlib figures into Tkinter applications.
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Add this import

# Imports the numpy module, a powerful library for numerical operations in Python.
import numpy as np

def plot_trajectory():
    # Extract values from entry widgets
    initial_velocity = float(velocity_entry.get())
    angle_deg = float(angle_entry.get())
    
    # Convert angle from degrees to radians
    angle_rad = np.deg2rad(angle_deg)
    
    # Time array
    t_max = 2 * initial_velocity * np.sin(angle_rad) / 9.81 # g=9.81
    t = np.linspace(0, t_max, 100) #it show range 100 is for sample
    
    # Projectile motion equations
    x = initial_velocity * np.cos(angle_rad) * t
    y = initial_velocity * np.sin(angle_rad) * t - 0.5 * 9.81 * t**2
    
    # Create a new figure
    # creating a Matplotlib figure and axis for plotting
    fig, ax = plt.subplots()
    
    # Plot trajectory
    # This line uses the plot method of the Matplotlib ax (axis) object to plot the projectile motion trajectory.
    ax.plot(x, y)

    # This line sets the title of the plot to "Projectile Motion" using the set_title method of the ax object.
    ax.set_title("Projectile Motion")

    # These lines set the labels for the x-axis and y-axis, respectively, using the set_xlabel and set_ylabel methods of the ax object.
    ax.set_xlabel("Horizontal Distance (m)")
    ax.set_ylabel("Vertical Height (m)")
    
    # Display the plot in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=3, column=0, columnspan=2)  # Changed row to 3

# Create main window
window = tk.Tk()
window.title("Projectile Motion Simulation")

# Labels and Entry widgets for input
ttk.Label(window, text="Initial Velocity (m/s)").grid(row=0, column=0)
velocity_entry = ttk.Entry(window)
velocity_entry.grid(row=0, column=1)

ttk.Label(window, text="Launch Angle (degrees)").grid(row=1, column=0)
angle_entry = ttk.Entry(window)
angle_entry.grid(row=1, column=1)

# Button to plot the trajectory
plot_button = ttk.Button(window, text="Plot Trajectory", command=plot_trajectory)
plot_button.grid(row=2, column=0, columnspan=2)

# Run the main loop
window.mainloop()
