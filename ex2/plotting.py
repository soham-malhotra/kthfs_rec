
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from math import pi, exp, sin

class FunctionPlotter:
    def __init__(self, t_start=0, t_end=10, num_points=1000):
        self.t_start = t_start
        self.t_end = t_end
        self.num_points = num_points
        self.t = np.linspace(t_start, t_end, num_points)  # Generate time points
        self.h_t = self.calculate_h(self.t)  # Calculate h(t)

    def lambda_fn(self, t):
        return 5 * np.sin(2 * pi * t)

    def calculate_h(self, t):
        # Calculate h(t) = 3 * pi * exp(-lambda(t))
        lambda_val = self.lambda_fn(t)
        return 3 * pi * np.exp(-lambda_val)

    def plt_fn(self):
        plt.plot(self.t, self.h_t, label="h(t) = 3*pi*exp(-lambda(t))", color='blue', linestyle='--')
        plt.title("Plot of h(t)")
        plt.xlabel("Time t")
        plt.ylabel("h(t)")
        plt.grid(True)
        plt.legend()
        plt.show()


if __name__ == "__main__":
    # Create an instance of the static plotter and visualize
    plot = FunctionPlotter(t_start=0, t_end=5, num_points=1000)
    plot.plt_fn()
