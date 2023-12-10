from pydub import AudioSegment
from scipy.io import wavfile
import numpy as np
import os
import numpy as np
from scipy.fft import fft
import numpy as np
from scipy.signal import hilbert
from scipy.io import wavfile
from scipy.optimize import curve_fit

class AudioModel:
    def __init__(self):
        self.file_path = None
        self.sample_rate = None
        self.data = None
        self.duration = None
        self.frequency = None

    def load_audio(self, file_path):
        # Load the audio file
        audio = AudioSegment.from_file(file_path)

        # Convert to wav if necessary
        if file_path.endswith('.mp3'):
            audio.export("converted.wav", format="wav")
            file_path = "converted.wav"

        # Read the sample rate and data from the WAV file
        self.sample_rate, self.data = wavfile.read(file_path)

        # Check if the audio has two channels (stereo) and convert to mono if necessary
        if self.data.ndim == 2:
            self.data = self.data.mean(axis=1)

        # Calculate the duration of the audio file
        self.duration = len(self.data) / self.sample_rate

        # Set the file path
        self.file_path = file_path

        # Remove the temporary converted file if it was created
        if file_path == "converted.wav":
            os.remove(file_path)

    def calculate_peak_resonant_frequency(self):
        # Perform the FFT on the audio data
        N = len(self.data)
        audio_fft = fft(self.data)
        # Get the power spectrum
        power_spectrum = np.abs(audio_fft[:N // 2]) ** 2
        # Find the frequency with the maximum power in the spectrum
        freqs = np.fft.fftfreq(N, 1 / self.sample_rate)
        peak_freq_index = np.argmax(power_spectrum)
        self.frequency = freqs[peak_freq_index]

    def get_waveform_data(self):
        # Return the time and amplitude data for the waveform
        times = np.arange(len(self.data)) / float(self.sample_rate)
        return times, self.data
    
    def calculate_rt60(self):
        # Ensure the signal is mono
        if self.data.ndim == 2:
            self.data = self.data.mean(axis=1)

        # Apply a windowing function (e.g., Hann window) to the signal
        window = np.hanning(len(self.data))
        windowed_signal = self.data * window

        # Calculate the energy envelope using the Hilbert transform
        analytic_signal = hilbert(windowed_signal)
        amplitude_envelope = np.abs(analytic_signal)

        # Convert the energy envelope to decibels
        energy_db = 20 * np.log10(amplitude_envelope)

        # Find the decay curve after the clap sound has stopped
        # This is a simplified approach; in practice, you would need to detect the end of the clap
        decay_start_index = np.argmax(energy_db)
        decay_curve = energy_db[decay_start_index:]

        # Define an exponential decay function to fit
        def decay_function(t, rt60):
            return -60 * (t / rt60)

        # Fit the decay curve to find the RT60 value
        time_axis = np.arange(len(decay_curve)) / self.sample_rate
        popt, _ = curve_fit(decay_function, time_axis, decay_curve, p0=[1.0])

        # The RT60 value is the fitted parameter
        rt60_value = popt[0]
        return rt60_value