import pytest
from solver import generate_valid_words




def test_generate_valid_words_start_d():
    """On sait que la première lettre du mot est un D"""
    assert generate_valid_words(
        possible_words=["DEVANT", "ENTREE", "PORTER", "GAUCHE"],
        letters_in_secret=[('D', 0)],
        letters_not_in_secret=[]
    ) == ["DEVANT"]


def test_liste_vide():
    """Verifie que si la liste des mots possibles est vide, la fonction renvoie une liste vide."""
    assert generate_valid_words(
        possible_words=[],
        letters_in_secret=[('D', 0)],
        letters_not_in_secret=[]
    ) == []



def test_aucune_lettre_jouee():
    """Vérifie que, lorsque l'utilisateur n'a joué aucune lettre, la liste des mots possibles reste inchangée."""
    assert  generate_valid_words(
        possible_words=["DEVANT", "ENTREE", "PORTER", "GAUCHE"],
        letters_in_secret=[],
        letters_not_in_secret=[]
    ) == ["DEVANT", "ENTREE", "PORTER", "GAUCHE"]

def test_e1_no_c():
    """On sait que la deuxième lettre du mot est un E, et que le mot ne contient pas de C"""
    assert generate_valid_words(
        possible_words=["DEVANT", "PERDRE", "CERNER", "GAUCHE"],
        letters_in_secret=[('E', 1)],
        letters_not_in_secret=['C']
    ) == ["DEVANT", "PERDRE"]