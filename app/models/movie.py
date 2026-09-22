class Movie:
    """Classe représentant un film avec un titre et un prix (par défaut: BASE_PRICE)."""
    BASE_PRICE = 20
    def __init__(self, title: str):
        self.title = title
        self.price = self.BASE_PRICE