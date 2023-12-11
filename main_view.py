import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.patches import Circle, Arc

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

        # info section
        self.info_frame = tk.Frame(self.middle_frame, width=200)
        self.info_frame.pack(side=tk.LEFT, fill=tk.Y)

        # label for displaying audio file duration
        self.duration_label = tk.Label(self.info_frame, text="Duration:\nN/A", justify=tk.LEFT)
        self.duration_label.pack(anchor='w')

        # label for displaying peak resonant frequency
        self.frequency_label = tk.Label(self.info_frame, text="Peak Resonant Frequency:\nN/A", justify=tk.LEFT)
        self.frequency_label.pack(anchor='w')

        # right side frame
        self.right_frame = tk.Frame(self.middle_frame)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # waveform plot
        self.waveform_frame = tk.Frame(self.right_frame)
        self.waveform_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=False)
        self.waveform_fig = Figure(figsize=(5, 2), dpi=100)
        self.waveform_ax = self.waveform_fig.add_subplot(111)
        self.waveform_canvas = FigureCanvasTkAgg(self.waveform_fig, master=self.waveform_frame)
        self.waveform_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # tabbed plots
        self.tab_control = ttk.Notebook(self.right_frame)
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab3 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab1, text='RT60 Low')
        self.tab_control.add(self.tab2, text='RT60 Mid')
        self.tab_control.add(self.tab3, text='RT60 High')
        self.tab_control.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Embed the figures in the tabs
        self.canvas1 = FigureCanvasTkAgg(Figure(figsize=(5, 2), dpi=100), master=self.tab1)
        self.canvas1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.canvas2 = FigureCanvasTkAgg(Figure(figsize=(5, 2), dpi=100), master=self.tab2)
        self.canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.canvas3 = FigureCanvasTkAgg(Figure(figsize=(5, 2), dpi=100), master=self.tab3)
        self.canvas3.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Button to calculate overall RT60 - This should be the only place where this button is created
        self.calc_overall_rt60_button = tk.Button(self.right_frame, text="Calculate Overall RT60", command=self.controller.calculate_and_display_overall_rt60)
        self.calc_overall_rt60_button.pack(side=tk.TOP, pady=10)  # Adjust padding as needed

    def set_file_label(self, text):
        self.file_label.config(text=text)

    def set_duration_label(self, duration):
        self.duration_label.config(text=f"Duration:\n{duration:.2f} seconds")

    def set_frequency_label(self, frequency):
        if frequency: self.frequency_label.config(text=f"Peak Resonant Frequency:\n{frequency:.2f} Hz")

    def update_waveform(self, times, data):
        self.waveform_ax.clear()
        self.waveform_ax.plot(times, data)
        self.waveform_ax.set_title('Audio Waveform', fontsize=14, fontweight='bold')
        self.waveform_ax.set_xlabel('Time (s)', fontsize=12)
        self.waveform_ax.set_ylabel('Amplitude', fontsize=12)
        self.waveform_ax.grid(True)
        self.waveform_fig.tight_layout()
        self.waveform_canvas.draw()

    def update_rt60_plot(self, canvas, rt60_value, title):
        fig = canvas.figure
        ax = fig.add_subplot(111)
        ax.clear()
        ax.bar([0], [rt60_value], width=0.5)
        ax.set_title(title)
        ax.set_ylabel('RT60 (s)')
        ax.set_ylim(0, max(rt60_value * 1.2, 0.5))  # Ensure the plot has some space above the bar
        ax.set_xticks([])
        canvas.draw()

    def run(self):
        self.root.mainloop()