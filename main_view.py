import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class MainView:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("SPIDAM - Acoustic Modeling")
        self.create_widgets()

    def create_widgets(self):
        # frame top
        self.top_ribbon_frame = tk.Frame(
            self.root, 
            width=self.root.winfo_width(), 
            height=self.root.winfo_height() * ( 1 / 8 )
        )
        self.top_ribbon_frame.pack()

        ## frame load button
        self.load_frame = tk.Frame(self.top_ribbon_frame)
        self.load_frame.pack(pady=10)

        ## load Button
        self.load_button = tk.Button(self.load_frame, padx=10, text="Load Audio File", command=self.controller.load_audio_file)
        self.load_button.pack(side=tk.LEFT)

        # frame middle 
        self.middle_frame = tk.Frame(
            self.root, 
            width=self.root.winfo_width(), 
            height=self.root.winfo_height() - self.top_ribbon_frame.winfo_height()
        )
        self.middle_frame.pack()

        ## frame middle left
        self.info_frame = tk.Frame(
            self.middle_frame, 
            width=self.root.winfo_width() * (1 / 5), 
            height=self.middle_frame.winfo_height()
        )
        self.info_frame.pack()

        ### info label
        self.plot_label = tk.Label(
            self.info_frame, 
            text="Audio Information:", 
            bg="gray", 
            width=self.info_frame.winfo_width()
        )
        self.plot_label.pack(side=tk.LEFT, padx=10)

        ## frame middle right (main content)
        self.info_frame = tk.Frame(
            self.middle_frame, 
            width=self.middle_frame.winfo_width() - self.info_frame.winfo_width(), 
            height=self.middle_frame.winfo_height()
        )
        self.info_frame.pack()

        

        # # Text Output
        # self.text_output = tk.Text(self.analysis_frame, height=10, width=50)
        # self.text_output.pack(side=tk.LEFT, padx=10)

        # # Placeholder for plots (to be replaced with actual plot widgets)
        # self.plot_label = tk.Label(self.plot_frame, text="Plots will be displayed here", bg="gray", width=50, height=10)
        # self.plot_label.pack(side=tk.LEFT, padx=10)

        # # Buttons for additional actions (e.g., cleaning data, analyzing, etc.)
        # self.clean_button = tk.Button(self.action_frame, text="Clean Data", command=self.controller.clean_audio_data)
        # self.clean_button.pack(side=tk.LEFT, padx=5)

    def run(self):
        self.root.mainloop()

    # Additional methods for updating the view, e.g., display results

    def run(self):
        self.root.mainloop()