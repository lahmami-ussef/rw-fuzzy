import numpy as np
import pytest

from app.fuzzy.membership import triangular


def test_sommet_vaut_1():
    assert triangular(0.40, 0.10, 0.40, 0.70) == 1.0


def test_pieds_valent_0():
    assert triangular(0.10, 0.10, 0.40, 0.70) == 0.0
    assert triangular(0.70, 0.10, 0.40, 0.70) == 0.0


def test_milieu_des_cotes():
    assert triangular(0.25, 0.10, 0.40, 0.70) == pytest.approx(0.5)
    assert triangular(0.55, 0.10, 0.40, 0.70) == pytest.approx(0.5)


def test_hors_ensemble():
    assert triangular(-1, 0.10, 0.40, 0.70) == 0.0
    assert triangular(5, 0.10, 0.40, 0.70) == 0.0


def test_epaulement_gauche_faible():
    # Goals Faible = Tri(0, 0, 0.30)
    assert triangular(0.0, 0, 0, 0.30) == 1.0
    assert triangular(0.15, 0, 0, 0.30) == pytest.approx(0.5)
    assert triangular(0.30, 0, 0, 0.30) == 0.0


def test_epaulement_droit_eleve_corrige():
    # Goals Élevé corrigé = Tri(0.40, 1, 1)
    assert triangular(1.0, 0.40, 1, 1) == 1.0
    assert triangular(0.70, 0.40, 1, 1) == pytest.approx(0.5)
    assert triangular(0.40, 0.40, 1, 1) == 0.0


def test_defaut_de_l_ancien_eleve():
    # Avec l'ancien Tri(0.40, 0.70, 1), un joueur à 1.0 but/90 n'avait aucun degré.
    assert triangular(1.0, 0.40, 0.70, 1) == 0.0


def test_tableau():
    resultat = triangular(np.array([0.10, 0.25, 0.40]), 0.10, 0.40, 0.70)
    assert resultat == pytest.approx([0.0, 0.5, 1.0])


def test_parametres_invalides():
    with pytest.raises(ValueError):
        triangular(1, 5, 2, 8)