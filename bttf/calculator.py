from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Iterable, Set

from bttf.pricing import (
    PRIX_UNITAIRE_AUTRE_FILM_EUR,
    PRIX_UNITAIRE_BTTF_EUR,
    taux_remise_bttf,
)

# On reconnaît exactement : "Back to the Future 1|2|3"
_PATTERN_BTTF = re.compile(r"^Back to the Future ([123])$")


@dataclass(frozen=True)
class ResumePanier:
    """Résumé métier du panier, utile pour tester et déboguer."""
    nb_dvds_bttf: int
    volets_bttf_distincts: Set[int]
    nb_autres_films: int


def resumer_panier(titres: Iterable[str]) -> ResumePanier:
    """
    Analyse les titres et produit un résumé :
    - nombre total de DVDs BTTF
    - ensemble des volets distincts (1/2/3)
    - nombre d'autres films
    """
    nb_dvds_bttf = 0
    volets_distincts: Set[int] = set()
    nb_autres_films = 0

    for titre in titres:
        match = _PATTERN_BTTF.match(titre)
        if match:
            nb_dvds_bttf += 1
            volets_distincts.add(int(match.group(1)))
        else:
            nb_autres_films += 1

    return ResumePanier(
        nb_dvds_bttf=nb_dvds_bttf,
        volets_bttf_distincts=volets_distincts,
        nb_autres_films=nb_autres_films,
    )


def calculer_total_eur(titres: Iterable[str]) -> int:
    """
    Calcule le total du panier en euros (entier),
    selon les règles de l'énoncé.
    """
    resume = resumer_panier(titres)

    nb_volets_distincts = len(resume.volets_bttf_distincts)
    remise = taux_remise_bttf(nb_volets_distincts)

    total_bttf = resume.nb_dvds_bttf * PRIX_UNITAIRE_BTTF_EUR
    total_bttf_apres_remise = total_bttf * (1 - remise)

    total_autres = resume.nb_autres_films * PRIX_UNITAIRE_AUTRE_FILM_EUR

    total = total_bttf_apres_remise + total_autres

    # Les exemples donnent des entiers ; on arrondit proprement au plus proche.
    return int(round(total))
