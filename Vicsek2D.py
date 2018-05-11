# Following code implements the Vicsek model in 2D from PRL 75 1226 (1995)

# Importing packages
import numpy as np
import matplotlib.pyplot as plt


class Vicsek2D:
    def __init__(self, N, eta):
        # Initialize simulation
        self.L = 25  # length of the square 2D region to be simulated
        self.N = N  # number of particles in the 2D region
        self.rho = N/self.L**2  # density of particles in the simulation
        self.eta = eta  # noise in the system
        self.r = 1  # interaction radius
        self.dt = 1.0  # time step
        self.v = 0.03  # magnitude of velocity
        self.pos = np.random.rand(self.N, 2) * self.L  # random initial position in 2D region
        self.theta = (np.random.rand(self.N) * 2 - 1) * np.pi  # random velocity angle [-pi pi]
        self.vel = np.zeros((self.N, 2))  # initialize velocity array
        self.vel[:, 0] = self.v * np.cos(self.theta)  # velocity along x
        self.vel[:, 1] = self.v * np.sin(self.theta)  # velocity along y
        self.tt = 20  # total number of time steps

    def main(self):
        # Setup plots
        plt.ion()
        fig = plt.figure()
        ax = fig.add_subplot(111)
        fig.show()
        fig.tight_layout()
        fig.canvas.draw()
        for nn in range(self.tt):
            ax.clear()
            ax.quiver(self.pos[:, 0], self.pos[:, 1], self.vel[:, 0], self.vel[:, 1])
            fig.canvas.draw()
            self.update()

    def update(self):
        # Update position and velocity


# Ask user for parameters
print("We will simulate a square box of size 25")
N = int(input("Enter the number of particles you want in the box: "))
eta = float(input("Enter the maximum noise in the system: "))
v2d = Vicsek2D(N, eta)
print("Particle density =", v2d.rho)
