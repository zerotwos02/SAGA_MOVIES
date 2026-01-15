from __future__ import annotations

"""
Règles de tarification.

- Un DVD "Back to the Future" coûte 15 €.
- Tout autre film coûte 20 €.
- La remise s'applique uniquement sur le total des DVDs "Back to the Future",
  en fonction du nombre de volets DISTINCTS présents dans le panier :
    - 2 volets distincts -> 10%
    - 3 volets distincts -> 20%
"""

PRIX_UNITAIRE_BTTF_EUR = 15
PRIX_UNITAIRE_AUTRE_FILM_EUR = 20

# Remise en fonction du nombre de volets BTTF distincts
REMISERATE_PAR_NB_VOLETS_BTTF_DISTINCTS = {
    1: 0.00,
    2: 0.10,
    3: 0.20,
}


def taux_remise_bttf(nb_volets_distincts: int) -> float:
    """
    Retourne le taux de remise à appliquer sur les DVDs BTTF,
    selon le nombre de volets distincts dans le panier.

    Par sécurité : si nb_volets_distincts est hors [1..3], on applique 0%.
    """
    return REMISERATE_PAR_NB_VOLETS_BTTF_DISTINCTS.get(nb_volets_distincts, 0.00)
