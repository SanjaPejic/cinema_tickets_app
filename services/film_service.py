from models.film import Film
from repositories.film_repository import load_film_data


def print_films(film_list: list[Film]) -> None:
    if not film_list:
        print("----------------------------------- No films found. -----------------------------------")
        return
    print("  | title | genre | duration_min | directors | main_cast | country | year | description")
    for i, film in enumerate(film_list):
        directors = ", ".join(film.directors)
        cast = ", ".join(film.cast)
        print(f"{i + 1}."
              f"| {film.title} | {film.genre} | {film.duration} | {directors} "
              f"| {cast} | {film.country} | {film.year} | {film.description}")


def search_films(title: str, genre: str, dur_min: int, dur_max: int, directors: list[str],
                 cast: list[str], country: str, year: int) -> list[Film]:
    film_list = load_film_data()
    searched_films = []

    title = title.strip().casefold()
    genre = genre.strip().casefold()
    directors = [d.strip().casefold() for d in directors]
    cast = [c.strip().casefold() for c in cast]
    country = country.strip().casefold()

    for film in film_list:

        film_title = film.title.casefold()
        film_genre = str(film.genre).casefold()
        film_directors = [d.casefold() for d in film.directors]
        film_cast = [c.casefold() for c in film.cast]
        film_country = film.country.casefold()

        if title and title not in film_title:
            continue
        if genre and genre != film_genre:
            continue
        if dur_min and dur_min > film.duration:
            continue
        if dur_max and dur_max < film.duration:
            continue
        if directors and not all(d in film_directors for d in directors):
            continue
        if cast and not all(c in film_cast for c in cast):
            continue
        if country and country != film_country:
            continue
        if year and year != film.year:
            continue

        searched_films.append(film)

    return searched_films
