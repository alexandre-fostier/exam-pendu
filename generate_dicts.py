"""
Depuis le fichier liste_mots.txt, on récupère tous les mots de 6,7,8,9,10 lettres.
et on génère 5 fichiers textes contenant les mots en fonction de leur taille (un mot par ligne, séparé par un \n):
dico_6_lettres.txt
dico_7_lettres.txt
dico_8_lettres.txt
dico_9_lettres.txt
dico_10_lettres.txt
On enlève les accents, les espaces, les tirets et les mots en double.
"""

import unicodedata


def lire_filtrer_mots(chemin_lexique:str, longueur:int):
    """Renvoie une liste de mots, en majuscule et sans accents, de longueur 'longueur' à partir d'un fichier txt"""
    liste_mots = []
    with open(chemin_lexique, 'r', encoding='utf8') as f:
        for l in f:
            # récupère le premier élément de la ligne car il y a d'autres infos dans le le fichier 'liste_mot.txt'
            mot = l.strip().split()[0]

            if len(mot) == longueur:
                # solution de ChatGPT
                mot = ''.join(c for c in unicodedata.normalize('NFD', mot) if unicodedata.category(c) != 'Mn')

                mot = mot.replace('-', '').upper()

                if mot not in liste_mots:
                    liste_mots.append(mot)
    return liste_mots


def ecrire_liste_mots(liste_mots:list, longueur:int) -> None:
    """Génère un fichier texte contenant tous les mots pour une longueur donné"""

    chemin_dico_ecriture:str = f"data/dico_{longueur}_lettres.txt"

    with open(chemin_dico_ecriture, 'w', encoding='utf-8') as file:
        file.writelines(f"{mot}\n" for mot in liste_mots)




def main(chemin:str) -> None:
    for long in range(6,11):
        # génère la liste de mot pour la longueur donné
        lst_mots = lire_filtrer_mots(chemin_lexique=chemin, longueur=long)

        # Génère un fichier texte correspondant
        ecrire_liste_mots(lst_mots, longueur=long)

if __name__ == '__main__':
    chemin = "data/liste_mots.txt"
    main(chemin= chemin)