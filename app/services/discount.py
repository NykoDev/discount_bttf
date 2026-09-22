from app.models.movie import Movie

class Discount:
    BTTF_MOVIES = [f'back to the future {i}' for i in ['1','2','3']]
    BTTF_PRICE = 15
    def __init__(self):
        self.movies = []

    def count_distinct_bttf_movies(self):
        distinct_movies = set([movie.title for movie in self.movies])
        return len(distinct_movies & set(self.BTTF_MOVIES))

    def set_discount_price(self, count_bttf_movies: int):
        match count_bttf_movies:
            case 2:
                return self.BTTF_PRICE * (1 - 0.1)
            case 3:
                return self.BTTF_PRICE * (1 - 0.2)
            case _:
                return self.BTTF_PRICE


    def apply(self, movies: list[Movie]):
        self.movies = movies
        n_bttf_movies = self.count_distinct_bttf_movies()
        for movie in self.movies:
            if movie.title in self.BTTF_MOVIES:
                movie.price = self.set_discount_price(n_bttf_movies)