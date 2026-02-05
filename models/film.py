from models.genre import Genre


class Film:
    def __init__(self, title: str, genre: Genre, duration: int, directors: list[str],
                 cast: list[str], country: str, year: int, description: str):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.directors = directors
        self.cast = cast
        self.country = country
        self.year = year
        self.description = description
