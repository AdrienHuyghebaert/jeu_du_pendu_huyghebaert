# Cette procédure permet de dire bonjour à l'utilisateur.
def dire_bonjour():
    print("    Bonjour et bienvenue sur le jeu du pendu !\n")


# Cette fonction permet de demander à l'utilisateur si il souhaite
# utliser sa liste de mots personnelle ou celle par défaut
# et de retourner un mot au hasard.
def choisir_liste():
    print("""\
    Le jeu possède une liste de mots par défaut.
    Mais vous pouvez ajouter la vôtre sous forme d'un fichier texte nommé "liste_mots" dans le dossier du jeu.""")

    choix_liste_mots = int(input("""
    Si vous souhaitez utiliser votre liste de mots, tapez 1
    et si vous souhaitez utiliser la liste par défaut, tapez 2: """))

    mot = ""
    while mot == "":
        if choix_liste_mots == 1:
            with open("test_liste.txt", 'r') as fio:
                mots = fio.read().splitlines()
            from random import choice
            mot = choice(mots)
            return mot

        elif choix_liste_mots == 2:
            with open("mots_pendu_defaut.txt", 'r') as fio:
                mots = fio.read().splitlines()
            from random import choice
            mot = choice(mots)
            return mot

        else:
            print("\n\n\n\n\n"
                  "    Choix non valide. Veuillez taper 1 ou 2.")

            choix_liste_mots = int(input("\n"
                                         "    Si vous souhaitez utiliser votre liste de mots, tapez 1\n"
                                         "    et si vous souhaitez utiliser la liste par défaut, tapez 2: "))


# Cette section est la partie principale du code
dire_bonjour()
mot_choisi = choisir_liste()
print(mot_choisi)
