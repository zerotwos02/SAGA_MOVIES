# tests/test_examples.py
from __future__ import annotations

from bttf.calculator import calculer_total_eur
from bttf.parser import lire_panier


def test_exemple_1():
    panier = """\
Back to the Future 1
Back to the Future 2
Back to the Future 3
"""
    titres = lire_panier(panier)
    assert calculer_total_eur(titres) == 36


def test_exemple_2():
    panier = """\
Back to the Future 1
Back to the Future 3
"""
    titres = lire_panier(panier)
    assert calculer_total_eur(titres) == 27


def test_exemple_3():
    panier = """\
Back to the Future 1
"""
    titres = lire_panier(panier)
    assert calculer_total_eur(titres) == 15


def test_exemple_4():
    panier = """\
Back to the Future 1
Back to the Future 2
Back to the Future 3
Back to the Future 2
"""
    titres = lire_panier(panier)
    assert calculer_total_eur(titres) == 48


def test_exemple_5():
    panier = """\
Back to the Future 1
Back to the Future 2
Back to the Future 3
La chèvre
"""
    titres = lire_panier(panier)
    assert calculer_total_eur(titres) == 56
