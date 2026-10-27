from typing import List, Dict, Tuple
import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

def average_rating(movies: List[Dict]) -> float:
    if not movies:
        return 0.0
    total = sum(movie["rating"] for movie in movies)
    return round(total / len(movies), 1)

def catalog_age_stats(movies: List[Dict], current_year: int = 2026) -> Tuple[int, int, int]:
    if not movies:
        return (0, 0, 0)
    ages = [current_year - movie["year"] for movie in movies]
    oldest_age = max(ages)
    newest_age = min(ages)
    average_age = math.ceil(sum(ages) / len(ages))
    return oldest_age, newest_age, average_age

def duration_in_hours(minutes: int) -> str:
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}ч {mins}м"

def rating_tier(rating: float) -> str:
    if rating >= 9:
        return "шедевр"
    elif rating < 5:
        return "слабо"
    else:
        return "хорошо" if rating >= 7 else "средне"

def decade_label(year: int) -> str:
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"

def print_non_comedy(movies: List[Dict]) -> None:
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])

def find_first_masterpiece(movies: List[Dict]) -> None:
    i = 0
    while i < len(movies):
        if movies[i]["rating"] > 9.0:
            print(f"Первый шедевр: {movies[i]['title']} ({movies[i]['rating']})")
            break
        i += 1
    else:
        print("Шедевров не найдено")

def main():
    print("ОТЧЕТ ПО КАТАЛОГУ")
    avg_rating = average_rating(movies)
    print(f"Средний рейтинг: {avg_rating}")

    oldest, newest, avg_age = catalog_age_stats(movies)
    print(f"Средний возраст фильмов: {avg_age} лет")
    print(f"Самый старый фильм: {oldest} лет, самый новый: {newest} лет")

    # Топ-3 по рейтингу
    sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
    print("\nТоп-3 фильма:")
    for m in sorted_movies[:3]:
        genres_str = ", ".join(m["genres"])
        print(f'  "{m["title"]}" ({m["year"]}) — {m["rating"]}/10, {duration_in_hours(m["duration_min"])}, жанры: {genres_str}')

    # Подсчёт жанров
    genre_counts: Dict[str, int] = {}
    for m in movies:
        for g in m["genres"]:
            genre_counts[g] = genre_counts.get(g, 0) + 1

    print("\nФильмов по жанрам:")
    for g, c in sorted(genre_counts.items()):
        print(f"  {g} — {c}")

    all_genres = sorted(genre_counts.keys())
    print(f"\nВсе жанры каталога: {', '.join(all_genres)}")

    print("\nФильмы без жанра comedy:")
    print_non_comedy(movies)

    print("\nПоиск первого шедевра (рейтинг > 9.0):")
    find_first_masterpiece(movies)

if __name__ == "__main__":
    main()
