import pyaudio

def list_audio_devices():
    # Initialisation de PyAudio
    p = pyaudio.PyAudio()
    
    # Obtenir le nombre de périphériques audio disponibles
    device_count = p.get_device_count()
    
    if device_count == 0:
        print("Aucun périphérique audio trouvé.")
        return
    
    print("Périphériques audio connectés :")
    
    # Parcourir tous les périphériques disponibles
    for i in range(device_count):
        # Récupérer les informations sur chaque périphérique
        device_info = p.get_device_info_by_index(i)
        
        # Afficher les informations pertinentes sur le périphérique
        print(f"ID: {device_info['index']}, Nom: {device_info['name']}, "
              f"Channels: {device_info['maxInputChannels']} (entrée), "
              f"Output Channels: {device_info['maxOutputChannels']} (sortie)")

    # Fermeture de PyAudio
    p.terminate()

if __name__ == '__main__':
    list_audio_devices()
