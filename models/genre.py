from enum import Enum


class Genre(str, Enum):
    ACTION = "action"
    COMEDY = "comedy"
    DRAMA = "drama"
    HORROR = "horror"
    ROMANCE = "romance"
    SCIENCE_FICTION = "sci-fi"

    def __str__(self):
        return self.value
