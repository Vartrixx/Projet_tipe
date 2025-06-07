#Histogramme
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import pprint
# Paramètres d'enregistrement
duration = 2  # Durée de l'enregistrement en secondes
fs = 44100  # Fréquence d'échantillonnage

print("Enregistrement en cours...")
# Enregistrement de l'audio
recording = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='int16')
sd.wait()  # Attendre que l'enregistrement soit terminé
print("Enregistrement terminé.")

# Sauvegarde de l'enregistrement dans un fichier WAV
write('output.wav', fs, recording)

print("Audio enregistré dans output.wav")

import librosa
import numpy as np
import matplotlib.pyplot as plt

# Charger le fichier audio
file_path = 'output.wav'
signal, sample_rate = librosa.load(file_path)

# Appliquer la transformée de Fourier
fft_result = np.fft.fft(signal)
frequencies = np.fft.fftfreq(len(fft_result), d=1/sample_rate)

# Ne garder que les fréquences positives
positive_freq_mask = frequencies > 0
frequencies = frequencies[positive_freq_mask]
amplitudes = np.abs(fft_result)[positive_freq_mask]

# Filtrer les fréquences en dessous de 256 Hz
amplitudes[frequencies < 256] = 0

# Tracer l'histogramme
plt.figure(figsize=(10, 6))
plt.plot(frequencies, amplitudes)
plt.xlabel('Fréquence (Hz)')
plt.ylabel('Amplitude')
plt.title('Amplitude en fonction de la fréquence')
plt.grid(True)
plt.xlim(0, sample_rate / 2)  # Limiter l'axe des x à la moitié de la fréquence d'échantillonnage
plt.show()