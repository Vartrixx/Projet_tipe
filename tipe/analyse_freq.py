import numpy as np
import librosa

def analyse_frequence(audio, sample_rate):
    # Transformée de Fourier à court terme (STFT)
    stft = np.abs(librosa.stft(audio))
    # Calcul des fréquences dominantes
    freqs = librosa.fft_frequencies(sr=sample_rate)
    times = librosa.frames_to_time(range(stft.shape[1]), sr=sample_rate)
    result = []

    for i in range(stft.shape[1]):  # Parcours des fenêtres temporelles
        magnitude = stft[:, i]
        freq_index = np.argmax(magnitude)  # Indice de la fréquence dominante
        dominant_freq = freqs[freq_index]
        result.append((times[i], dominant_freq))  # Ajout de temps et fréquence dominante

    return result

