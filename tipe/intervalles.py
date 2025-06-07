t_quadru_croche = 0.015625

def intervalles(tab_notes):
    t0,inutile = tab_notes[0]
    t1,inutile = tab_notes[1]
    T_echant = t1-t0
    n = len(tab_notes)
    partition = dict()
    for k in range(n):
        tps, notes = tab_notes[k]
        temps = round(tps/t_quadru_croche)/4
        for note in notes:
            if notes[note] != -1:
                if not(temps in partition):
                    partition[temps] = []
                c = k
                notes_suivantes = notes
                while c<n and note in notes_suivantes:
                    c += 1
                    notes_suivantes[note] = -1
                    if c != n:
                        inutile,notes_suivantes = tab_notes[c]
                duree = round(T_echant*(c-k)/t_quadru_croche)/4
                L = partition[temps]
                L.append((note_to_lilypond(note), duree))
                partition[temps] = L
    return partition

def intervalles2(tab_notes):
    t0,inutile = tab_notes[0]
    t1,inutile = tab_notes[1]
    T_echant = t1-t0
    n = len(tab_notes)
    partition = dict()
    N = round(t_quadru_croche/T_echant)
    print(T_echant,N)
    for k in range(n):
        tps, notes = tab_notes[k]
        temps = round(tps/t_quadru_croche)
        for note in notes:
            if notes[note] != -1:
                if not(temps in partition):
                    partition[temps] = []
                c = k
                tjrs_la = N
                notes_suivantes = notes
                while tjrs_la > 0 and c < n:
                    c += 1
                    notes_suivantes[note] = -1
                    if c != n:
                        tps_courant,notes_suivantes = tab_notes[c]
                    if note in notes_suivantes:
                        tjrs_la = N
                        notes_suivantes[note] = -1
                        if c != n:
                            tab_notes[c] = (tps_courant,notes_suivantes)
                    else:
                        tjrs_la -= 1
                duree = round(T_echant*(c-k)/t_quadru_croche)
                if duree != 0:
                    L = partition[temps]
                    L.append((note_to_lilypond(note), duree))
                    partition[temps] = L
    return partition

def note_to_lilypond(note):
    # Dictionnaire pour mapper les noms de notes aux noms LilyPond
    if note == 'r':
        return note
    note_names = {
        'C': 'c',
        'D': 'd',
        'E': 'e',
        'F': 'f',
        'G': 'g',
        'A': 'a',
        'B': 'b'
    }
    # Dictionnaire pour mapper les altérations aux suffixes LilyPond
    accidentals = {
        '#': 'is',
        'b': 'es',
        '': ''  # Pas d'altération
    }
    # Extraire la note et l'octave
    if len(note) < 2 or len(note) > 4:
        print(note)
        raise ValueError("Format de note invalide. Utilisez par exemple 'C4' ou 'A#3'.")
    # Extraire la note et l'octave
    name = note[0]
    accidental = ''
    octave = ''
    # Vérifier s'il y a une altération
    if note[1] in accidentals:
        accidental = note[1]
        octave = note[2]
    else:
        octave = note[1]
    # Convertir la note en notation LilyPond
    lilypond_note = note_names[name]
    if accidental in accidentals:
        lilypond_note += accidentals[accidental]
    # Ajuster l'octave
    if octave.lstrip('-').isdigit():
        octave = int(octave)
        octave = 5
        n = 4
        if octave > n:
            lilypond_note += "'" * (octave - n)
        elif octave < n:
            lilypond_note += "," * (n - octave)
    return lilypond_note


