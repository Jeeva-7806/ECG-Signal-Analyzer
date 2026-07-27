# ECG Signal Analyzer

## Overview
This project analyzes real ECG signals from the MIT-BIH Arrhythmia Database using Python. It filters ECG signals, detects R-peaks, calculates heart rate (BPM), and performs FFT analysis.

## Features
- Read real ECG data
- Butterworth low-pass filtering
- R-peak detection
- Heart rate (BPM) calculation
- Fast Fourier Transform (FFT)
- ECG waveform visualization
- Frequency spectrum analysis

## Technologies Used
- Python
- NumPy
- SciPy
- Matplotlib
- WFDB

## Dataset
MIT-BIH Arrhythmia Database (Record 100)

## Results
- Heart Rate: ~74.48 BPM
- R-peaks detected successfully
- FFT spectrum generated
- Filtered ECG visualization

## How to Run

1. Install the required libraries:

```bash
pip install -r requirements.txt
```

2. Run the program:

```bash
python main.py
```
