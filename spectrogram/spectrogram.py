import matplotlib.pyplot as plot
import numpy as np
from scipy.io import wavfile

samplingFrequency, signalData = wavfile.read(r"C:\Users\harki\Downloads\weird.wav")
#weird.wav is a stereo o/p file
p = signalData[:, 0] #selection b/w 0 & 1 -> L : R channel
plot.subplot(211)
plot.title("Spectrogram of a wav file")
plot.plot(signalData)
plot.xlabel("Sample")
plot.ylabel("Amplitude")
plot.subplot(212)
plot.specgram(p, Fs=samplingFrequency)
plot.xlabel("Time")
plot.ylabel("Frequency")
plot.show()

