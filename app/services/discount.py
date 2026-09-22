from app.models.movie import Movie

class Discount:
    """
    Application d'une réduction sur les films.
    15€ pour un film Back to the Future (BTTF), 
    10% de réduction pour 2 films BTTF distincts, 
    20% de réduction pour 3 films BTTF distincts.
    """
    BTTF_MOVIES = [f'back to the future {i}' for i in ['1','2','3']]
    BTTF_PRICE = 15
    def __init__(self):
        self.movies = []

    def count_distinct_bttf_movies(self):
        """Compte le nombre de films BTTF distincts dans la liste de films fournie."""
        distinct_movies = set([movie.title for movie in self.movies])
        return len(distinct_movies & set(self.BTTF_MOVIES))

    def set_discount_price(self, count_bttf_movies: int):
        """Détermine le prix réduit en fonction du nombre de films BTTF distincts."""
        match count_bttf_movies:
            case 2:
                return self.BTTF_PRICE * (1 - 0.1)
            case 3:
                return self.BTTF_PRICE * (1 - 0.2)
            case _:
                return self.BTTF_PRICE


    def apply(self, movies: list[Movie]):
        """Applique le prix réduit sur les films BTTF"""
        self.movies = movies
        n_bttf_movies = self.count_distinct_bttf_movies()
        for movie in self.movies:
            if movie.title in self.BTTF_MOVIES:
                movie.price = self.set_discount_price(n_bttf_movies)