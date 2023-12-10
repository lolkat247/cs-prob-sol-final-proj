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

    def update_view_with_audio_data(self):
        # Update the duration label in the view
        self.view.set_duration_label(self.model.duration)

        # Calculate and update the peak resonant frequency label in the view
        self.model.calculate_peak_resonant_frequency()
        self.view.set_frequency_label(self.model.frequency)

        # Update the waveform plot in the view
        times, data = self.model.get_waveform_data()
        self.view.update_waveform(times, data)

    def draw_smileys(self):
        # Draw smiley on the waveform plot
        self.view.draw_smiley_face()

        # Draw smileys on each tab
        self.view.draw_smiley_on_tab(self.view.canvas1, self.view.canvas1.figure.add_subplot(111))
        self.view.draw_smiley_on_tab(self.view.canvas2, self.view.canvas2.figure.add_subplot(111))
        self.view.draw_smiley_on_tab(self.view.canvas3, self.view.canvas3.figure.add_subplot(111))

    def run(self):
        self.view.run()