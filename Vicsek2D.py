# Following code implements the Vicsek model in 2D from PRL 75 1226 (1995)

# Importing packages
import numpy as np
import matplotlib.pyplot as plt


class Vicsek2D:
    def __init__(self, L, N, eta, r, v):
        # Initialize simulation
        self.L = L  # length of the square 2D region to be simulated
        self.N = N  # number of particles in the 2D region
        self.eta = eta  # noise in the system
        self.r = r  # interaction radius
        self.dt = 1.0  # time step
        self.v = v  # magnitude of velocity
        self.pos = np.random.rand(self.N, 2) * self.L  # random initial position in 2D region
        self.theta = (np.random.rand(self.N) * 2 - 1) * np.pi  # random velocity angle [-pi pi]
        self.vel = np.zeros(self.N, 2)  # initialize velocity array
        self.vel[:, 0] = self.v * np.cos(self.theta)  # velocity along x
        self.vel[:, 1] = self.v * np.sin(self.theta)  # velocity along y
