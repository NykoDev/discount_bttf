from app.models.movie import Movie
from app.services.discount import Discount

class Cart:
    """Classe représentant un panier de films avec une liste de films (objet Movie) et un prix total."""

    def __init__(self, movies : list[Movie]):
        self.movies = movies or []

    @property
    def total_price(self):
        return sum([movie.price for movie in self.movies])

    def apply_discount(self, discount: Discount):
        """Applique une réduction sur les films du panier en utilisant l'objet Discount fourni."""
        discount.apply(self.movies)