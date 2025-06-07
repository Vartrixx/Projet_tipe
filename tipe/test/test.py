import pyaudio
import wave

# Paramètres d'enregistrement
FORMAT = pyaudio.paInt16  # Format de l'audio
CHANNELS = 1              # Mono
RATE = 44100              # Taux d'échantillonnage
CHUNK = 1024              # Taille du bloc
TIMEOUT = 3               # Temps d'enregistrement en secondes

def test_microphone():
    p = pyaudio.PyAudio()

    print("Test du micro en cours... Parle dans ton micro.")
    
    # Ouvrir le flux audio pour l'enregistrement
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    
    frames = []
    
    # Enregistrer pendant un certain temps
    for i in range(0, int(RATE / CHUNK * TIMEOUT)):
        data = stream.read(CHUNK)
        frames.append(data)
    
    # Arrêter l'enregistrement et fermer le flux
    print("Enregistrement terminé.")
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    # Sauvegarder le fichier audio pour l'écouter
    wf = wave.open("test_microphone.wav", 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    
    print("Fichier audio 'test_microphone.wav' créé. Écoute-le pour vérifier.")

if __name__ == "__main__":
    test_microphone()
