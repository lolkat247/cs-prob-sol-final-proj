from audio_model import AudioModel
from main_view import MainView

class AudioController:
    def __init__(self):
        self.model = AudioModel()
        self.view = MainView(self)

    def load_audio_file(self, file_path):
        pass

    def clean_audio_data(self):
        pass

    def analyze_audio(self):
        pass

    def run(self): self.view.run()