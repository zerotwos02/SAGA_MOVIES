# SAGA_MOVIES

Petit programme de commande qui calcule le prix total d’un panier de films
selon des règles de réduction spécifiques à la saga **Back to the Future**.

![frontend_demo](screenshots/frontend_demo.png)

Le panier est fourni sous forme de texte (un film par ligne) et le programme
affiche le prix total correspondant.

---

## Règles de tarification

- Un DVD  **Back to the Future** coûte **15 €**
- Tout autre film coûte **20 €**
- Une remise s’applique **uniquement** sur les DVDs *Back to the Future* :
  - **2 volets distincts** → **10 %**
  - **3 volets distincts** → **20 %**
- La remise dépend du **nombre de volets différents**, pas de la quantité achetée

---

## Format d’entrée

- Un film par ligne
- Le texte est lu depuis l’entrée standard (stdin)

Exemple :

Back to the Future 1

Back to the Future 2

La chèvre


---

## Exécution du programme

### Pré-requis
- Python **3.10+**

### Lancer le programme
```bash
python -m venv .venv
source .venv/bin/activate  # Linux / Mac
# ou .\.venv\Scripts\activate  # Windows

pip install -r requirements.txt
```
Lancer le programme
```bash
python main.py
```
Puis coller le panier dans le terminal et valider.

Ou via redirection :
``` bash
python main.py < basket.txt
```

## Tests unitaires

Les tests unitaires couvrent l’ensemble des exemples fournis dans l’énoncé.

### Lancer les tests :

pytest


### Résultat attendu :

![Tests unitaires réussis](screenshots/tests_passed.png)

### Interface Flask (optionnelle)

Une interface web minimaliste est fournie pour faciliter les tests manuels.
La logique métier reste inchangée et continue d’être utilisée par la CLI et les tests.

Lancer l’interface :
``` BASH
python -m flask --app app run
```
Puis ouvrir dans le navigateur :
``` BASH
http://127.0.0.1:5000
```

## Structure du projet
``` BASH
BTTF-PRICING/
├── bttf/                   # logique métier principale
│   ├── parser.py           # lecture et nettoyage du panier
│   ├── pricing.py          # règles de prix et remises
│   └── calculator.py       # calcul du total
├── tests/                  # tests unitaires
│   ├── conftest.py
│   └── test_examples.py
├── screenshots/            # captures d’écran (tests + interface)
│   ├── tests_passed.png
│   └── frontend_demo.png
├── app.py                  # interface Flask (optionnelle)
├── main.py                 # point d’entrée CLI
├── requirements.txt        # dépendances du projet
├── README.md
└── .gitignore
```
## Notes

- BTTF signifie Back to the Future

- Le code est volontairement simple, lisible et facilement testable


