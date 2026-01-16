from __future__ import annotations

from flask import Flask, request, render_template_string

from bttf.parser import lire_panier
from bttf.calculator import calculer_total_eur

app = Flask(__name__)

HTML = """
<!doctype html>
<html lang="fr">
  <head>
    <meta charset="utf-8" />
    <title>LA SAGA MOVIES</title>
  </head>
  <body style="max-width: 700px; margin: 40px auto; font-family: Arial, sans-serif;">
    <h1>LA SAGA MOVIES</h1>
    <p>Colle un film par ligne, puis clique sur <strong>Calculer</strong>.</p>

    <form method="post">
      <textarea name="basket" rows="10" style="width:100%;">{{ basket }}</textarea>
      <div style="margin-top: 12px;">
        <button type="submit">Calculer</button>
      </div>
    </form>

    {% if total is not none %}
      <h2>Résultat</h2>
      <p><strong>Total :</strong> {{ total }} €</p>
    {% endif %}
  </body>
</html>
"""

@app.get("/")
def home():
    return render_template_string(HTML, basket="", total=None)

@app.post("/")
def compute():
    basket_text = request.form.get("basket", "")
    titres = lire_panier(basket_text)
    total = calculer_total_eur(titres)
    return render_template_string(HTML, basket=basket_text, total=total)
