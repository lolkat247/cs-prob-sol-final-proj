from audio_model import AudioModel
from main_view import MainView
import matplotlib.pyplot as plt
from pydub import AudioSegment
from tkinter import filedialog
import os

class AudioController:
    def __init__(self):
        self.model = AudioModel()
        self.view = MainView(self)
        self.wav_ = None

    def load_audio_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3")])
        if file_path:
            # update the file_label with the selected file name
            self.view.file_label.config(text=file_path)
            # load the audio file and perform any necessary processing
            audio = AudioSegment.from_file(file_path)
            # convert to wav
            audio.export("converted.wav", format="wav")
            # load the wav data into memory
            with open("converted.wav", "rb") as wav_file:
                self.wav_data = wav_file.read()
            # remove the temporary file
            os.remove("converted.wav")

    def clean_audio_data(self):
        pass

    def analyze_audio(self):
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