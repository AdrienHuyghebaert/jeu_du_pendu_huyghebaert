import unicodedata
import os
import string
import random


# Cette procédure permet de dire bonjour à l'utilisateur.
def faire_introduction():
    print("Vous avez choisi de lancer une partie du jeu du pendu")
    print("Veuillez ne pas rentrer de lettre avec des accents lors de vos tentatives\n")


# Cette fonction permet de demander à l'utilisateur si il souhaite
# utliser sa liste de mots personnelle ou celle par défaut
# et de retourner un mot au hasard.
def choisir_liste():
    print("Le jeu possède une liste de mots par défaut, mais vous pouvez jouer avec la vôtre.")
    choix_liste_mots = input("Si vous souhaitez utiliser votre liste de mots, rentrez 'oui', sinon rentrez 'non' :\n")

    # Cette boucle "while" permet de d'assurer tant que l'utilisateur n'a pas rentré autre chose que oui ou non
    mot = ""
    while mot == "":
        if choix_liste_mots == 'non':
            with open("mots_pendu_defaut.txt", 'r', encoding='utf-8') as fio:
                mots = fio.read().splitlines()
            mot = random.choice(mots)
            return mot

        elif choix_liste_mots == 'oui':
            nom_fichier = input("Rentrez le nom de votre fichier :\n")
            chemin_fichier = input("Rentrez le chemin pour accèder à votre fichier :\n")
            fichier_utilisateur = os.path.join(chemin_fichier, nom_fichier + '.txt')
            with open(fichier_utilisateur, 'r', encoding='utf8') as fio:
                mots = fio.read().splitlines()
            mot = random.choice(mots)
            return mot

        else:
            choix_liste_mots = input("Choix non valide. Veuillez rentrez 'oui' ou 'non' :\n")


# Cette fonction permet de demander à l'utilisateur
# combien il souhaite d'essais pour trouver le mot.
def choisir_nombre_essais():
    print("\nPar défaut, le jeu propose de trouver le mot en 6 essais.")
    changement_nb_essais = int(input("Si vous souhaitez changer le nombre d'essais, tapez '1', sinon tapez '2' :\n"))

    if changement_nb_essais == 2:
        nombre_essais = 6
        return nombre_essais

    elif changement_nb_essais == 1:
        nombre_essais = int(input("Combien d'essais souhaitez-vous ? (Rentrez un nombre entier)\n"))
        return nombre_essais


# Cette fonction permet de supprimer les éventuels accents du mot.
def supprimer_accents(mot_choisi):
    mot_sans_accents = unicodedata.normalize('NFKD', mot_choisi).encode('ASCII', 'ignore').decode('utf-8')
    return mot_sans_accents


# Cette fonction permet de transformer le mot qui était de type
# en chaine de caractères en type liste pour faciliter l'analyse.
def passer_le_mot_en_liste(mot_sans_accents):
    mot_liste = list(mot_sans_accents)
    return mot_liste


# Cette fonction va regarder si la lettre que l'utilisateur rentre
# est présente dans le mot à trouver.
# Si oui elle affiche la lettre à la place du tiret.
def tester_lettre_trouvee(mot_liste, lettre_utilisateur, mot_recherche_liste):
    # Cette variable permet de savoir combien de lettres ont été trouvées
    lettre_trouvee = 0
    for i in range(len(mot_recherche_liste)):
        if mot_liste[i] == lettre_utilisateur:
            mot_recherche_liste[i] = lettre_utilisateur
            lettre_trouvee += 1
    return lettre_trouvee, mot_recherche_liste


# Cette fonction propose à l'utilisateur de rejour ou non au jeu du pendu
def proposer_rejouer():
    print("Souhaitez-vous refaire une partie ?")
    choix = str(input("Répondez par 'oui' ou 'non'\n"))
    while choix != 'oui' and choix != 'non':
        choix = str(input("Entrée invalide. Répondez par 'oui' ou 'non'\n"))
    if choix == 'oui':
        jeu_du_pendu()
    else :
        print("Très bien. Vous allez quitter le jeu.")


# Cette fonction permet de donner un indice à l'utilisateur si il ne lui reste qu'un seul essai et si il le souhaite.
# Renvoie une lettre qui n'est pas dans le mot à trouver et qui n'a pas été encore donnée.
def donner_indice(liste_utilisateur_testees, mot_liste, alphabet_liste):
    ensemble_valeurs_utilisees = set(liste_utilisateur_testees + mot_liste)
    ensemble_alphabet = set(alphabet_liste)

    # Soustraire les lettres déjà utilisées (donnez par l'utilisateur ou bien constituants le mot)
    # aux lettres de l'alphabet afin d'avoir que des lettres qui ne sont pas dans le mot.
    lettres_indice = list(ensemble_alphabet - ensemble_valeurs_utilisees)

    # Choisir aléatoirement une lettre indice parmi les lettres disponibles
    indice = random.choice(lettres_indice)
    return indice

# Ceci est la fonction principale qui appelle les autres fonctions et procédures.
def jeu_du_pendu():
    faire_introduction()
    mot_choisi = choisir_liste()  # Extraire de la liste choisie le mot.
    nombre_essais = choisir_nombre_essais()
    mot_sans_accents = supprimer_accents(mot_choisi)  # Suppression des éventuels accents dans le mot.
    mot_liste = passer_le_mot_en_liste(mot_sans_accents)  # Le mot passe du type string à liste.
    print(mot_liste)

    alphabet_liste = list(string.ascii_lowercase)  # Liste des lettres de l'alphabet.
    lettres_utilisateur_testees = []  # Initialisaion d'une liste qui regroupe les lettres testées par l'utilisateur.
    mot_recherche_liste = ['_' for i in range(len(mot_choisi))]  # Initialisation de l'affichage du mot à trouver.
    mot_recherche_string = ''.join(mot_recherche_liste)
    lettres_a_trouver = len(mot_choisi)  # Compteur qui permet de savoir combien de lettres il y a à trouver.
    utilisation_indice = 1  # Ce compteur permet de savoir combien de fois, l'indice a été utilisé.
    indice = []  # Initialisation de la variable indice.

    # Boucle pour les différentes tentatives.
    while lettres_a_trouver != 0 and nombre_essais != 0:

        print(f"Voici où vous en êtes de votre recherche : {mot_recherche_string}")
        if lettres_utilisateur_testees != []:
            if indice != []:
                print(f"Ces lettres {lettres_utilisateur_testees + indice} ne sont pas dans le mot à trouver.")
            else:
                print(f"Ces lettres {lettres_utilisateur_testees} ne sont pas dans le mot à trouver.")
        print(f"Il vous reste {nombre_essais} essais.")
        lettre_utilisateur = str(input("Veuillez rentrer une lettre :\n"))
        print("\n\n\n\n\n")

        lettre_trouvee, mot_recherche_liste = tester_lettre_trouvee(mot_liste, lettre_utilisateur, mot_recherche_liste)

        # Si l'utilisateur a trouvé au moins 1 lettre.
        if lettre_trouvee != 0:
            mot_recherche_string = ''.join(mot_recherche_liste)  # Passage en chaine de caractères pour l'affichage
            lettres_a_trouver -= lettre_trouvee  # Changer le nombre de lettres encore à trouver
            print(lettres_a_trouver)
            print(f"Il y a {lettre_trouvee} {lettre_utilisateur} dans le mot à trouver.")

        # Si l'utilisateur n'a pas trouvé de lettre.
        elif lettre_trouvee == 0:
            nombre_essais -= 1
            print(f"Dommage, il n'y a pas de {lettre_utilisateur} dans le mot.")
            lettres_utilisateur_testees.append(lettre_utilisateur)

        # Si il ne reste plus qu'un seul essai à l'utilisateur, lui proposer un indice.
        if nombre_essais == 1 and utilisation_indice == 1:
            utilisation_indice = 0  # L'utilisateur n'aura plus le droit à un indice
            print("Attention vous n'avez plus qu'un seul essai pour trouver votre mot")
            choix_indice = str(input("Si vous voulez un indice marquez 'indice', sinon marquez 'non'\n"))
            while choix_indice != 'indice' and choix_indice !='non':
                choix_indice = str(input("Entrée invalide. Si vous voulez un indice marquez 'indice', sinon marquez 'non'\n"))
            print("\n\n\n\n\n")
            if choix_indice == 'indice':
                indice = list(donner_indice(lettres_utilisateur_testees, mot_liste, alphabet_liste))
                print(f"La lettre {indice} n'est pas dans le mot.\n")

    if nombre_essais == 0:
        print(f"Dommage vous avez perdu. Le mot à trouver était {mot_sans_accents}.")
        proposer_rejouer()
    elif lettres_a_trouver == 0:
        print(f"Bravo ! Vous avez le mot. C'était {mot_sans_accents}")
        proposer_rejouer()


jeu_du_pendu()
