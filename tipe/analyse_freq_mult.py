import numpy as np
import librosa

def analyse_frequence(audio, sample_rate):
    # Transformée de Fourier à court terme (STFT)
    stft = np.abs(librosa.stft(audio))
    # Calculer les fréquences pour chaque bin
    frequencies = librosa.fft_frequencies(sr=sample_rate)
    print(frequencies)
    # Trouver l'index correspondant à 256 Hz
    index_256Hz = np.where(frequencies <= 256)[0][-1]
    # Atténuer les basses fréquences
    stft_modified = stft.copy()
    stft_modified[:index_256Hz, :] = 0.00001  # Réduire l'amplitude à 0.001%
    # Calcul des fréquences dominantes
    freqs = librosa.fft_frequencies(sr=sample_rate)
    times = librosa.frames_to_time(range(stft_modified.shape[1]), sr=sample_rate)
    result = []

    for i in range(stft_modified.shape[1]):  # Parcours des fenêtres temporelles
        magnitude = stft_modified[:, i]
        top_indices = np.argsort(magnitude)[-1:][::-1]  # Indices des 5 fréquences dominantes
        top_freqs = freqs[top_indices]
        top_magnitudes = magnitude[top_indices]
        result.append((times[i], list(zip(top_freqs, top_magnitudes))))  # Ajout de temps et fréquences dominantes avec amplitude

    return result

