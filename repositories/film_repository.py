from models.film import Film
from models.genre import Genre
from utils.logger import Logger

film_file_path = "film_data.txt"


def load_film_data() -> list[Film]:
    film_list = []
    try:
        with open(film_file_path, mode="r") as data_file:
            file_lines = data_file.readlines()
        file_lines.pop(0)

        for line in file_lines:
            row = line.strip().split("|")
            if len(row) < 8:
                continue
            title = row[0]
            try:
                genre = Genre(row[1])
            except ValueError as e:
                genre = Genre.DRAMA
                Logger.error(f"{e} in film {file_lines.index(line) + 1}. Default genre given: drama")
            duration = int(row[2])
            directors = [d.strip() for d in row[3].split(",") if d.strip()]
            cast = [c.strip() for c in row[4].split(",") if c.strip()]
            country = row[5].strip()
            year = int(row[6])
            description = row[7]
            film = Film(title, genre, duration, directors, cast, country, year, description)
            film_list.append(film)

    except FileNotFoundError as e:
        Logger.error(f"File not found: {e} ")
    return film_list
