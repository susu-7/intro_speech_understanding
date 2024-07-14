import numpy as np

def fourier_synthesis(num_harmonics, X, T0):
    N = len(X)
    n = np.arange(N)
    x = np.zeros(N)
    for l in range(1, num_harmonics + 1):
        index = l * N // T0
        magnitude = np.abs(X[index])
        phase = np.angle(X[index])
        x += (2 / N) * magnitude * np.cos(2 * np.pi * l * n / T0 + phase)
    return x


