Bonjour et bienvenue au jeu du pendu qui est réalisé dans le cadre de MGA802.
Ce script a été écrit dans le langage PYTHON.

Le but du jeu est de trouver le mot qui a été choisis aléatoirement à partir d'une liste
prédéfinie avec un nombre d'erreurs limité. Le dépôt possède une liste de mots par défaut
mais vous pouvez jouer avec votre liste de mots personnelle (au format .txt).
Pour cela il vous sera demandé lors de l'exécution du code de donner le nom du fichier
ainsi que le chemin pour y accèder.
Vous pouvez églament choisir le nombre d'erreurs permises pour trouver le mot (la valeur par défaut est 6).
Il y la possibilité de demander un indice si il ne reste plus qu'un seul essai,
ainsi que la possibilité de jouer plusieurs parties.

- Le script est composé de 8 fonctions qui s'articulent autour de la fonction principale "jeu_du_pendu".

- La fonction "faire_introduction" sert simplement à afficher un message de bienvenue ainsi que préciser qu'il ne faut rentrer que des lettres sans caractères spéciaux.

- La fonction "choisir_liste" permet de demander à l'utilisateur si il souhaite utiliser la liste par défaut ou bien utiliser sa propre liste.

- La fonction "choisir_nombre_essais" permet de demander à l'utilisateur avec combien d'essais il souhaite trouver le mot. La valeur par défaut est 6.

- La fonction "supprimer_accents" permet de supprimer les éventuels caractères spéciaux du mots qui a été pioché.

- La fonction "passer_le_mots_en_liste" permet comme son nom l'indique de transformer le mot qui était de type chaine de caractères en une liste afin de simplifier l'analyse.

- La fonction "tester_lettre_trouvee" permet de déterminer si la lettre donnée par l'utilisateur est dans le mot ou non.

- La fonction "proposer_rejouer" permet de proposer à l'utilisateur de rejouer si il le souhaite.

- La fonction "donner_indice" donne un indice à l'utilisateur si il souhaite et si il ne lui reste qu'un seul essais.


Ensuite vient la fonction principale "jeu_du_pendu" qui permet de jouer au jeu.

- Afficher à l'utilisateur le mot qu'il doit trouver avec des tirets.
- Demander à l'utilisateur de rentrer une lettre.
- Si cette dernière est contenue dans le mot, alors remplacer le tiret par cette dernière.
- Sinon ajouter cette lettre a la liste des lettres infructueuses et les afficher afin que l'utilisateur ne rentre pas 2 fois des lettres non contenues dans le mot.
- Répétez ces opérations.
- Si il ne reste plus qu'un seul essais à l'utilisateur, lui proposer d'avoir un indice. Il peut refuser cette aide.
- Cet indice sera sous la forme d'une lettre qui n'est PAS dans le mot.
- Si il n'y a plus de lettres à trouver dans le mot, alors l'utilisateur a gagné.
- Si le nombre d'essais tombe à 0, l'utilisateur a perdu.
- Dans les 2 cas, il est proposé à l'utilisateur si il veut rejouer une partie.

