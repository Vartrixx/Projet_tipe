bpm = int(input("Quel bpm ?"))
t_noire = 60/bpm

def l_part(tab_notes):
   for k in range(len(tab_notes)):
      duree,note = tab_notes[k]
      nb_temps = round(duree/t_noire)
      tab_notes[k] = (nb_temps,note)
   return tab_notes
