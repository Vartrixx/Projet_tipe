import math

# Dictionnaire des noms des notes (tempérament égal)
NOTES = {
    0: "C", 1: "C#", 2: "D", 3: "D#", 4: "E", 5: "F", 6: "F#", 7: "G", 8: "G#", 9: "A", 10: "A#", 11: "B"
}

# Fréquence de référence pour la note A4
A4_FREQ = 440.0
A4_INDEX = 57  # Index de A4 dans une octave (C0 est l'index 0)
t_quadru_croche = 0.015625


def frequency_to_note(frequency):
    """
    Convertit une fréquence (en Hz) en note musicale.

    Paramètres :
        frequency (float) : La fréquence à convertir.

    Retourne :
        note (str) : Le nom de la note (par ex. A4, C#5).
    """
    if frequency <= 0:
        return "Invalid frequency"

    # Calcul du demi-ton le plus proche
    semitones_from_a4 = 12 * math.log2(frequency / A4_FREQ)
    nearest_note_index = round(A4_INDEX + semitones_from_a4)

    # Déterminer le nom de la note et l'octave
    note_name = NOTES[nearest_note_index % 12]
    octave = nearest_note_index // 12

    return f"{note_name}{octave}"

def convert_frequencies_to_notes(resultats):
    Liste = []
    for k in range(len(resultats)):
        temps,list_freq = resultats[k]
        temps = round(temps,3)
        dic = {}
        for i in range(len(list_freq)):
            amplitude,freq = list_freq[i]
            note = frequency_to_note(freq)
            if amplitude >= 700 and not(note in dic):
                dic[note] = temps
        if dic == {}:
            dic['r'] = temps
        Liste.append((temps,dic))
    return Liste
