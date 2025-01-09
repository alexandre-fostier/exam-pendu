import math
from copy import copy


def generate_valid_words(possible_words:list[str], letters_in_secret:list[tuple], letters_not_in_secret:list[str]):
    """Renvoie la liste des mots valides, correspondant aux critères déjà connus"""
    valid_words = []

    for word in possible_words:
        valid = True

        # Verifie que le mot ne comporte pas de lettres exclues
        for letter in letters_not_in_secret:
            if letter in word:
                valid = False
                break

        # Vérifie que les lettres trouvées sont à la bonne place dans le mot
        for t in letters_in_secret:
            if t[0] != word[t[1]]:
                valid = False
                break

        if valid:
            valid_words.append(word)

    return valid_words




def generate_best_letters(possible_words:list, letters_not_played:list[str], letters_in_secret:list[tuple], letters_not_in_secret:list[str]):
    """Renvoie la meilleure lettre, celle qui élimine le plus de mots possibles parmi les mots restants. Pour cela, on
    simule le fait de jouer chaque lettre et on mesure combien de mots sont encore possibles après avoir joué cette
    lettre. La lettre qui, en moyenne, réduit le plus les possibilités est celle que l'on conseille à l'utilisateur."""

    moyennes = []

    for letter in letters_not_played:
        total_possibilities = 0
        for word in possible_words:
            # Trouver le ou les index de la lettre dans le mot
            indexes = [index for index, char in enumerate(word) if char == letter]
            letters_in_secret_updated = letters_in_secret.copy()
            [letters_in_secret_updated.append(('A', index)) for index in indexes]
            nb_mots_possibles = len(generate_valid_words(possible_words, letters_in_secret_updated, letters_not_in_secret))
            total_possibilities += nb_mots_possibles
        moyennes.append(total_possibilities/len(possible_words))

    # La meilleure lettre à jouer est celle avec la plus petite moyenne
    best_letter = letters_not_played[moyennes.index(min(moyennes))]

    return best_letter
