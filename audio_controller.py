from audio_model import AudioModel
from main_view import MainView
from tkinter import filedialog
import numpy as np

class AudioController:
    def __init__(self):
        self.model = AudioModel()
        self.view = MainView(self)

    def load_audio_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3")])
        if file_path:
            self.model.load_audio(file_path)
            self.view.set_file_label(file_path)
            self.update_view_with_audio_data()
            self.calculate_and_update_rt60()
            # Calculate the peak resonant frequency
            peak_frequency = self.model.calculate_peak_resonant_frequency()
            # Update the frequency label in the view
            self.view.set_frequency_label(peak_frequency)

    def update_view_with_audio_data(self):
        # Update the duration label in the view
        self.view.set_duration_label(self.model.duration)

        # Update the waveform plot in the view
        times, data = self.model.get_waveform_data()
        self.view.update_waveform(times, data)

    def calculate_and_update_rt60(self):
        # Define the frequency ranges for low, mid, and high
        low_range = (20, 250)
        mid_range = (250, 2000)
        high_range = (2000, 20000)

        # Calculate RT60 for each frequency range
        rt60_low = self.model.calculate_rt60_for_frequency_range(*low_range)
        rt60_mid = self.model.calculate_rt60_for_frequency_range(*mid_range)
        rt60_high = self.model.calculate_rt60_for_frequency_range(*high_range)

        # Update the plots with the RT60 values
        self.view.update_rt60_plot(self.view.canvas1, rt60_low, 'RT60 Low')
        self.view.update_rt60_plot(self.view.canvas2, rt60_mid, 'RT60 Mid')
        self.view.update_rt60_plot(self.view.canvas3, rt60_high, 'RT60 High')

    def calculate_and_display_overall_rt60(self):
        # Calculate the overall RT60 value
        overall_rt60 = self.model.calculate_rt60()
        # Display the overall RT60 in a popup window
        self.view.display_overall_rt60_popup(overall_rt60)

    def run(self):
        self.view.run()