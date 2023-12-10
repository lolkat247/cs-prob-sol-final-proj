import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class MainView:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("SPIDAM - Acoustic Modeling")
        self.root.minsize(600, 400)
        self.create_widgets()

    def create_widgets(self):
        # frame top
        self.top_ribbon_frame = tk.Frame(self.root)
        self.top_ribbon_frame.pack(fill=tk.X)

        # load Button
        self.load_button = tk.Button(self.top_ribbon_frame, text="Load Audio File", command=self.controller.load_audio_file)
        self.load_button.pack(side=tk.LEFT)

        # label for displaying audio file name
        self.file_label = tk.Label(self.top_ribbon_frame, text="No file loaded")
        self.file_label.pack(side=tk.LEFT)

        # frame middle 
        self.middle_frame = tk.Frame(self.root)
        self.middle_frame.pack(fill=tk.BOTH, expand=True)

        # tabbed plots
        self.tab_control = ttk.Notebook(self.middle_frame)
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab3 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab1, text='RT60 Low')
        self.tab_control.add(self.tab2, text='RT60 Mid')
        self.tab_control.add(self.tab3, text='RT60 High')
        self.tab_control.pack(fill=tk.BOTH, expand=True)

        # button to combine plots
        self.combine_button = tk.Button(self.middle_frame, text="Combine Plots", command=self.controller.combine_plots)
        self.combine_button.pack(side=tk.BOTTOM)

    def run(self):
        self.root.mainloop()

    # Additional methods for updating the view, e.g., display results