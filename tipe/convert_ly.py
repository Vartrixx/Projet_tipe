import subprocess

def generate_lilypond_code(music_dict):
    # Initialiser le document LilyPond
    lilypond_code = r"""\version '2.24.1'
    \score {
      \new Staff {
        \time 4/4
        \clef treble
        \key c \major
        """

    # Parcourir le dictionnaire et ajouter les notes au code LilyPond
    for instant, notes in sorted(music_dict.items()):
        for note, duration in notes:
            lilypond_code += f"{note}{duration} "

    # Finaliser le document LilyPond
    lilypond_code += r"""
      }
    }
    """
    return lilypond_code

def save_to_ly_file(lilypond_code, filename):
    with open(filename, 'w') as file:
        file.write(lilypond_code)

def generate_pdf(filename):
    # Utiliser subprocess pour exécuter la commande LilyPond
    try:
        subprocess.run(["lilypond", filename], check=True)
        print(f"Le fichier PDF a été généré avec succès à partir de {filename}.")
    except subprocess.CalledProcessError as e:
        print(f"Une erreur s'est produite lors de la génération du PDF : {e}")




# Exemple de dictionnaire d'instants et de notes
#music_dict = {0: [("c'", 2), ("e'", 16)],1: [("d'", 4), ("f'", 4)],2: [("e'", 4), ("g'", 4)],3: [("f'", 4), ("a'", 4)]}

# Générer le code LilyPond
##lilypond_code = generate_lilypond_code(music_dict)

# Sauvegarder le code dans un fichier .ly
##ly_filename = "partition.ly"
##save_to_ly_file(lilypond_code, ly_filename)

# Générer le fichier PDF à partir du fichier .ly
##generate_pdf(ly_filename)

def create_lilypond_file_mistral(dictionary, filename):
    with open(filename, 'w') as f:
        f.write("\\version \"2.24.1\"\n")
        f.write("\\header {\n")
        f.write("  title = \"Generated Score\"\n")
        f.write("  composer = \"Python Script\"\n")
        f.write("}\n\n")
        f.write("\\score {\n")
        f.write("  \\new Staff {\n")
        f.write("    \\time 4/4\n")
        f.write("    \\key c \\major\n")
        f.write("    \\clef treble\n")

        # Iterate over the dictionary and write the notes
        for time, notes in dictionary.items():
            for note, duration in notes:
                f.write(f"    {note}{duration} ")

        f.write("\n  }\n")
        f.write("  \\layout { }\n")
        f.write("  \\midi { }\n")
        f.write("}\n")

# Exemple d'utilisation
dictionary = {
    1: [("c'4", 1), ("d'4", 1)],
    2: [("e'4", 1), ("f'4", 1)],
    3: [("g'4", 1), ("a'4", 1)],
    4: [("b'4", 1), ("c''4", 1)]
}

#create_lilypond_file_mistral(dictionary, "output.ly")



