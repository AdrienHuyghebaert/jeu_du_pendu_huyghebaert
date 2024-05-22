import unicodedata
import os


# Cette procédure permet de dire bonjour à l'utilisateur.
def dire_bonjour():
    print("Bonjour et bienvenue sur le jeu du pendu !\n")


# Cette fonction permet de demander à l'utilisateur si il souhaite
# utliser sa liste de mots personnelle ou celle par défaut
# et de retourner un mot au hasard.
def choisir_liste():
    print("Le jeu possède une liste de mots par défaut, mais vous pouvez jouer la vôtre.")
    choix_liste_mots = input("Si vous souhaitez utiliser votre liste de mots, rentrez oui, sinon rentrez non :\n")

    # Cette boucle "while" permet de d'assurer tant que l'utilisateur n'a pas rentré autre chose que oui ou non
    mot = ""
    while mot == "":
        if choix_liste_mots == 'non':
            with open("mots_pendu_defaut.txt", 'r', encoding='utf-8') as fio:
                mots = fio.read().splitlines()
            from random import choice
            mot = choice(mots)
            return mot

        elif choix_liste_mots == 'oui':
            nom_fichier = input("Rentrez le nom de votre fichier\n")
            chemin_fichier = input("Rentrez le chemin pour accèder à votre fichier\n")
            fichier_utilisateur = os.path.join(chemin_fichier, nom_fichier + '.txt')
            with open(fichier_utilisateur, 'r', encoding='utf8') as fio:
                mots = fio.read().splitlines()
            from random import choice
            mot = choice(mots)
            return mot

        else:
            choix_liste_mots = input("Choix non valide. Veuillez rentrer oui ou non :\n")


# Cette fonction permet de demander à l'utilisateur
# combien il souhaite d'essais pour trouver le mot
def choisir_nombre_essais():
    print("Par défaut, le jeu propose de trouver le mot en 6 tentatives.")
    changement_nb_essais = int(input("Si vous souhaitez changer le nombre de tentatives, tapez 1, sinon tapez 2 :\n"))

    if changement_nb_essais == 2:
        nombre_essais = 6
        return nombre_essais

    elif changement_nb_essais == 1:
        nombre_essais = int(input("Combien d'essais souhaitez-vous ? (Rentrez un nombre entier)\n"))
        return nombre_essais


# Cette fonction permet de supprimer les éventuels accents du mot
def supprimer_accents(mot_choisi):
    mot_sans_accents = unicodedata.normalize('NFKD', mot_choisi).encode('ASCII', 'ignore').decode('utf-8')
    return mot_sans_accents


# Ceci est la fonction principale qui appelle les autres fonctions et procédures
def jeu_du_pendu():
    dire_bonjour()
    mot_choisi = choisir_liste()
    print(mot_choisi)
    nombre_essais = choisir_nombre_essais()
    print(nombre_essais)
    mot_sans_accents = supprimer_accents(mot_choisi)
    print(mot_sans_accents)


jeu_du_pendu()
