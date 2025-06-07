import sounddevice as sd
import numpy as np

def enregistrement(SAMPLE_RATE,DURATION):
    print("Enregistrement en cours...")
    audio = sd.rec(int(SAMPLE_RATE * DURATION), samplerate=SAMPLE_RATE, channels=1, dtype='float64')
    sd.wait()  # Attendre la fin de l'enregistrement
    print("Enregistrement terminé.")
    # Convertir en un tableau numpy
    audio = np.squeeze(audio)
    return audio
