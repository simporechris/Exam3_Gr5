import pytest
from Q2 import afficher_jours_examens


def test1():
    horaire_examen = "jeudi"
    resultat_attendue= afficher_jours_examens(horaire_examen)
    assert horaire_examen == resultat_attendue