import sine_wave

# Generate a sine wave of frequency 440Hz, sampled at 44100Hz, for 1 second
x, y = sine_wave.generate_sine_wave(440, 44100, 1)

# Plot the sine wave
sine_wave.plot_sine_wave(x, y, title="440Hz Sine Wave")