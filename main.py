import wfdb
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, find_peaks

# Read ECG
record = wfdb.rdrecord("data/100")
ecg = record.p_signal[:, 0]
fs = record.fs

# First 1000 samples
signal = ecg[:1000]

# ---------------- Filter ----------------
cutoff = 40
b, a = butter(4, cutoff / (fs / 2), btype='low')
filtered = filtfilt(b, a, signal)

# ---------------- R-Peaks ----------------
peaks, _ = find_peaks(filtered, height=0.5, distance=150)

# Heart Rate
rr = np.diff(peaks) / fs
heart_rate = 60 / np.mean(rr)

# ---------------- FFT ----------------
fft = np.fft.fft(filtered)
magnitude = np.abs(fft)
frequency = np.fft.fftfreq(len(filtered), d=1/fs)

half = len(filtered) // 2

# ---------------- Dashboard ----------------

# Figure 1 - Original ECG
plt.figure(figsize=(10,4))
plt.plot(signal)
plt.title("Original ECG")
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.grid(True)

# Figure 2 - Filtered ECG with R-peaks
plt.figure(figsize=(10,4))
plt.plot(filtered, label="Filtered ECG")
plt.plot(peaks, filtered[peaks], "ro", label="R-Peaks")
plt.title(f"Heart Rate = {heart_rate:.2f} BPM")
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

# Figure 3 - FFT
plt.figure(figsize=(10,4))
plt.plot(frequency[:half], magnitude[:half])
plt.title("FFT Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)

# Print Report
print("\n========== ECG REPORT ==========")
print("Sampling Frequency :", fs, "Hz")
print("Detected Beats     :", len(peaks))
print(f"Heart Rate         : {heart_rate:.2f} BPM")
print("================================")

plt.show()
