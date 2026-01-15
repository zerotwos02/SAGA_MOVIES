from __future__ import annotations

from typing import List


def lire_panier(texte_panier: str) -> List[str]:
    """
    Convertit le texte d'entrée (un film par ligne) en liste de titres.

    - Ignore les lignes vides.
    - Supprime les espaces inutiles en début/fin de ligne.
    """
    lignes = texte_panier.splitlines()
    titres: List[str] = []

    for ligne in lignes:
        titre = ligne.strip()
        if titre:  # ignore les lignes vides
            titres.append(titre)

    return titres
