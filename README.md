# Back To The Future

Petite application FastAPI qui calcule le prix d'un panier de films Back To The Future, avec réduction selon le nombre de films distincts de la trilogie.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Lancer l'application

Depuis la racine du projet :

```bash
uvicorn app.main:app --reload
```

L'application est accessible sur [http://localhost:8000](http://localhost:8000).

## Lancer les tests

```bash
pytest
```

## Avec Docker

```bash
docker build -t discount-bttf .
docker run -p 8000:8000 discount-bttf
```

L'application est accessible sur [http://localhost:8000](http://localhost:8000).
