# main.py
from __future__ import annotations

import sys

from bttf.calculator import calculer_total_eur
from bttf.parser import lire_panier


def main() -> int:
    """
    Point d'entrée CLI.
    Lit le panier depuis stdin (un film par ligne) et affiche le total.
    """
    texte_panier = sys.stdin.read()
    titres = lire_panier(texte_panier)
    total = calculer_total_eur(titres)
    print(total)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
