from audio_model import AudioModel
from main_view import MainView
import matplotlib.pyplot as plt
from pydub import AudioSegment
from tkinter import filedialog
import os
import numpy as np
from scipy.io import wavfile
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc

class AudioController:
    def __init__(self):
        self.model = AudioModel()
        self.view = MainView(self)
        self.wav_data = None

    def load_audio_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3")])
        if file_path:
            # update the file_label with the selected file name
            self.view.file_label.config(text=file_path)

            # load the audio file and perform any necessary processing
            audio = AudioSegment.from_file(file_path)

            # convert to wav
            audio.export("converted.wav", format="wav")

            # read the sample rate and data from the converted WAV file
            sample_rate, data = wavfile.read("converted.wav")

            # Check if the audio has two channels (stereo)
            if data.ndim == 2:
                # Convert stereo to mono by averaging the two channels
                data = data.mean(axis=1)

            # update the duration_label with the duration of the audio file
            duration = len(data) / sample_rate
            if duration: self.view.duration_label.config(text=f"Duration:\n{duration:.2f} seconds")

            # update the frequency_label with the peak resonant frequency
            frequency = self.calculate_peak_resonant_frequency()  # TODO: Implement this method
            if frequency: self.view.frequency_label.config(text=f"Peak Resonant Frequency:\n{frequency:.2f} Hz")

            # update the waveform plot
            times = np.arange(len(data)) / float(sample_rate)
            self.view.waveform_ax.clear()
            self.view.waveform_ax.plot(times, data)
            self.view.waveform_canvas.draw()

            # Apply customizations to the plot
            self.view.waveform_ax.set_title('Audio Waveform', fontsize=14, fontweight='bold')
            self.view.waveform_ax.set_xlabel('Time (s)', fontsize=12)
            self.view.waveform_ax.set_ylabel('Amplitude', fontsize=12)
            self.view.waveform_ax.grid(True)
            self.view.waveform_ax.plot(times, data, color='royalblue', linewidth=1.5)

            # Use a tight layout to optimize spacing
            self.view.waveform_fig.tight_layout()

            self.view.waveform_canvas.draw()

            # remove the temporary file
            os.remove("converted.wav")

    def calculate_peak_resonant_frequency(self):
        pass

    def combine_plots(self):
        # get the data for the individual plots
        data1 = self.get_data_for_plot(self.view.tab1)
        data2 = self.get_data_for_plot(self.view.tab2)
        data3 = self.get_data_for_plot(self.view.tab3)

        # create a new figure
        fig, ax = plt.subplots()

        # plot the data
        ax.plot(data1, label='RT60 Low')
        ax.plot(data2, label='RT60 Mid')
        ax.plot(data3, label='RT60 High')

        # add a legend
        ax.legend()

        # display the plot
        plt.show()

    def run(self): self.view.run()