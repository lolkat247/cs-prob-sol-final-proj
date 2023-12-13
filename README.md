# SPIDAM - Acoustic Modeling

## Overview

The SPIDAM (Scientific Python Interactive Data Acoustic Modeling) project is an interactive data analysis and modeling platform designed for acoustic analysis, particularly for assessing voice intelligibility in enclosed spaces. The platform provides tools for importing, cleaning, visualizing, analyzing, and modeling audio data with a focus on calculating reverberation time (RT60) and its impact on sound clarity.

## Background

Enclosed spaces with improper acoustic treatment can lead to long reverberation times, which can impair voice intelligibility and learning. The SPIDAM project aims to address this issue by enabling users to measure and analyze RT60, which is the time required for sound to fade away after the source has stopped. The goal is to engineer solutions that create a short and consistent reverb time across the audible frequency spectrum (20Hz – 20kHz) to maximize voice intelligibility.

## Features

- **Import Data**: Load audio files from various sources and handle different formats (e.g., WAV, MP3).
- **Clean Data**: Provide tools to handle missing values, remove metadata, and resolve inconsistencies in channel format.
- **Data Analysis**: Generate summary statistics, visualize waveforms, and identify RT60 values over three frequency ranges.
- **Data Modeling**: Visualize RT60 data for each frequency range and display the peak resonant frequency.
- **Reporting**: Calculate the difference in RT60 time to achieve optimal voice intelligibility.

## Installation

To set up the SPIDAM project, you will need to install the required Python packages. You can install them using the following command:

```bash
pip install -r requirements.txt
```

## Usage

To run the SPIDAM application, execute the `main.py` script:

```bash
python main.py
```

The graphical user interface (GUI) will launch, allowing you to load audio files, visualize data, and perform acoustic analysis.

## Functional Requirements

- GUI with a load button to import audio samples.
- Support for WAV and MP3 formats, with conversion to WAV if necessary.
- Metadata removal and handling of multi-channel audio.
- Six plots: waveform, RT60 for Low, Mid, High frequencies, and an additional plot of your choice.
- Text output for duration, frequency of greatest amplitude, and RT60 differences.

## Design Requirements

The application follows the Model-View-Controller (MVC) design pattern:

- **Model**: Manages the state information, such as audio data and analysis results.
- **View**: Presents the model to the user and handles user interactions.
- **Controller**: Manages the flow of the application and sequences interactions between the user and the system.

## Version Control

The project uses Git/Github for source control. The public URL to the Github repository will be provided, along with a Gitlog indicating weekly activity and contributions by group members.

## Report Requirements

The final report will document the project and discoveries, following the provided template.

## Deliverables

- Python application in the specified format (zipped directory).
- Audio sample data in WAV format.
- Gitlog.
- Written report.

## References

1. Valente, Michael; Holly Hosford-Dunn; Ross J. Roeser (2008). Audiology. Thieme. pp. 425–426. ISBN 978-1-58890-520-8.
2. Lloyd, Llewelyn Southworth (1970). Music and Sound. Ayer Publishing. pp. 169. ISBN 978-0-8369-5188-2.
3. "Reverberation Time RT60 Measurement". www.nti-audio.com.
4. Bistafa SR, Bradley JS. Reverberation time and maximum background-noise level for classrooms from a comparative study of speech intelligibility metrics. J Acoust Soc Am. 2000 Feb;107(2):861-75. doi: 10.1121/1.428268. PMID: 10687696.
5. [Reverberation - Wikipedia](https://en.wikipedia.org/wiki/Reverberation)

## Extra Credit

The GUI includes a button that toggles the display of low, mid, and high RT60 plots for enhanced analysis.
