#Histogramme
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import pprint
# Paramètres d'enregistrement
duration = 15  # Durée de l'enregistrement en secondes
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
import librosa.display
import matplotlib.pyplot as plt

# Charger un fichier audio
file_path = 'output.wav'
signal, sample_rate = librosa.load(file_path)

# Appliquer la transformation de Fourier à court terme (STFT)
stft = librosa.stft(signal)

# Calculer les fréquences pour chaque bin
frequencies = librosa.fft_frequencies(sr=sample_rate)

# Trouver l'index correspondant à 256 Hz
index_256Hz = np.where(frequencies <= 256)[0][-1]

# Atténuer les basses fréquences
stft_modified = stft.copy()
stft_modified[:index_256Hz, :] *= 0.1  # Réduire l'amplitude à 10%
# Convertir en dB pour une meilleure visualisation
stft_db = librosa.amplitude_to_db(abs(stft))

# Afficher le spectrogramme
plt.figure(figsize=(14, 5))
librosa.display.specshow(stft_db, sr=sample_rate, x_axis='time', y_axis='log')
plt.colorbar()
plt.title('Spectrogramme')
plt.show()
