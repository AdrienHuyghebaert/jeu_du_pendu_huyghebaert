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
    while mot == "":  # Cette boucle "while" permet de d'assurer tant que l'utilisateur n'a pas rentré 1 ou 2
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


# Cette fonction permet de demander à l'utilisateur
# combien il souhaite d'essais pour trouver le mot
def choisir_nombre_essais():
    print("\n"    
          "    Par défaut, le jeu propose de trouver le mot en 6 tentatives.")
    changement_nb_essais = int(input("\n"
                                     "    Si vous souhaitez changer le nombre de tentatives, tapez 2. Sinon tapez 1 "))

    if changement_nb_essais == 1:
        nombre_essais = 6
        return nombre_essais

    elif changement_nb_essais == 2:
        nombre_essais = int(input("    Combien d'essais souhaitez-vous ? (Rentrez un nombre entier) "))
        return nombre_essais


# Cette section est la partie principale du code
dire_bonjour()
mot_choisi = choisir_liste()
print(mot_choisi)
nombre_essais = choisir_nombre_essais()
print(nombre_essais)
