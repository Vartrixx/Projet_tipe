from tipe import config
from tipe import enregistrement as en
from tipe import analyse_freq_mult as af
from tipe import freq_to_demi_tones_mult as ftodt
from pprint import pprint
from tipe import temps_duree as td
from tipe import intervalles as itv
from tipe import convert_ly as cly

SAMPLE_RATE = 44100*2
DURATION = 15
t_quadru_croche = 0.015625
ly_filename = input('nom de la partition :')
audio = en.enregistrement(SAMPLE_RATE,DURATION)
resultats = af.analyse_frequence(audio, SAMPLE_RATE)
tab_notes = ftodt.convert_frequencies_to_notes(resultats)
partition_temps = itv.intervalles2(tab_notes)
cly.create_lilypond_file_mistral(partition_temps, ly_filename + ".ly")
print("à cette étape")
# Générer le fichier PDF à partir du fichier .ly
cly.generate_pdf(ly_filename + " " + ".ly")

