import numpy as np
import matplotlib.pyplot as plt

def generate_sine_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, False)
    frequencies = x * freq
    # 2pi because np.sin takes radians
    y = np.sin(frequencies * 2 * np.pi)
    return x, y

def plot_sine_wave(x, y, title="Sine Wave"):
    plt.figure(figsize=(14, 5))
    plt.title(title)
    plt.plot(x, y)
    plt.show()