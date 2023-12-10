import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
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

        # Draw the initial smiley face
        self.draw_smiley_face()

        # tabbed plots
        self.tab_control = ttk.Notebook(self.right_frame)
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab3 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab1, text='RT60 Low')
        self.tab_control.add(self.tab2, text='RT60 Mid')
        self.tab_control.add(self.tab3, text='RT60 High')
        self.tab_control.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Create figures and axes for each tab
        self.fig1, self.ax1 = plt.subplots()
        self.fig2, self.ax2 = plt.subplots()
        self.fig3, self.ax3 = plt.subplots()

        # Draw smiley faces on each tab
        self.draw_smiley_on_tab(self.fig1, self.ax1)
        self.draw_smiley_on_tab(self.fig2, self.ax2)
        self.draw_smiley_on_tab(self.fig3, self.ax3)

        # Embed the figures in the tabs
        self.canvas1 = FigureCanvasTkAgg(self.fig1, master=self.tab1)
        self.canvas1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.canvas2 = FigureCanvasTkAgg(self.fig2, master=self.tab2)
        self.canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.canvas3 = FigureCanvasTkAgg(self.fig3, master=self.tab3)
        self.canvas3.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def draw_smiley_face(self):
        # Clear the current plot
        self.waveform_ax.clear()

        # Set the title
        self.waveform_ax.set_title('Audio Waveform', fontsize=14, fontweight='bold')

        # Draw a smiley face
        face = Circle((0.5, 0.5), 0.4, color='yellow', fill=True)
        left_eye = Circle((0.35, 0.65), 0.05, color='black', fill=True)
        right_eye = Circle((0.65, 0.65), 0.05, color='black', fill=True)
        smile = Arc((0.5, 0.4), 0.4, 0.2, angle=0, theta1=210, theta2=330, color='black', linewidth=2)

        self.waveform_ax.add_patch(face)
        self.waveform_ax.add_patch(left_eye)
        self.waveform_ax.add_patch(right_eye)
        self.waveform_ax.add_patch(smile)

        # Hide the axes
        self.waveform_ax.axis('off')

        # Refresh the canvas
        self.waveform_canvas.draw()

    def draw_smiley_on_tab(self, fig, ax):
        # Clear the current plot
        ax.clear()

        # Draw a smiley face
        face = Circle((0.5, 0.5), 0.4, color='yellow', fill=True)
        left_eye = Circle((0.35, 0.65), 0.05, color='black', fill=True)
        right_eye = Circle((0.65, 0.65), 0.05, color='black', fill=True)
        smile = Arc((0.5, 0.4), 0.4, 0.2, angle=0, theta1=210, theta2=330, color='black', linewidth=2)

        ax.add_patch(face)
        ax.add_patch(left_eye)
        ax.add_patch(right_eye)
        ax.add_patch(smile)

        # Hide the axes
        ax.axis('off')

        # Refresh the canvas
        fig.canvas.draw()

    def run(self):
        self.root.mainloop()