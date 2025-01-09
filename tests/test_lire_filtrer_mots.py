import pytest
from generate_dicts import lire_filtrer_mots


def test_filtrage_par_longueur():
    """Vérifier que la fonction filtre correctement les mots par longueur"""
    mots = lire_filtrer_mots("data_test/filetest1.txt", 6)
    assert mots == ["ECOUTE", "ARRETE", "CAMION"]


def test_filtrage_avec_accent():
    """Vérifie que les mots avec des accents sont bien transformés"""
    mots = lire_filtrer_mots("data_test/filetest1.txt", 5)
    assert mots == ["BOITE"]


def test_fichier_vide():
    """Vérifie que la fonction renvoie une erreur si le fichier est vide"""
    with pytest.raises(ValueError):
        lire_filtrer_mots('data_test/filetest_empty.txt', 6)
