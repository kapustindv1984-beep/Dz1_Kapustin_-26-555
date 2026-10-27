from typing import List, Dict, Tuple, Set, Any
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

# --- Этап 1: Разминка ---

def average_rating(movies: List[Dict[str, Any]]) -> float:
    if not movies:
        return 0.0
    total = sum(m["rating"] for m in movies)
    return round(total / len(movies), 1)


def catalog_age_stats(movies: List[Dict[str, Any]], current_year: int = 2026) -> Tuple[int, int, int]:
    if not movies:
        return (0, 0, 0)
    ages = [current_year - m["year"] for m in movies]
    oldest = max(ages)
    newest = min(ages)
    avg_ceil = math.ceil(sum(ages) / len(ages))
    return oldest, newest, avg_ceil


def duration_in_hours(minutes: int) -> str:
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}ч {mins}м"


# --- Этап 2: Условия и match ---

def rating_tier(rating: float) -> str:
    # Обязательный тернарный оператор
    if rating >= 9:
        return "шедевр"
    elif rating < 5:
        return "слабо"
    else:
        # Здесь тернарный используется явно
        return "хорошо" if rating >= 7 else "средне"


def decade_label(year: int) -> str:
    # match True + case _ if для диапазонов — как в задании
    match True:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"


# --- Этап 3: Циклы ---

def print_non_comedy(movies: List[Dict[str, Any]]) -> None:
    for m in movies:
        if "comedy" in m["genres"]:
            continue
        print(m["title"])


def find_first_masterpiece(movies: List[Dict[str, Any]]) -> None:
    i = 0
    while i < len(movies):
        if movies[i]["rating"] > 9.0:
            print(f"Первый шедевр: {movies[i]['title']} ({movies[i]['rating']})")
            break
        i += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies: List[Dict[str, Any]], threshold: int = 120) -> int:
    count = 0
    for m in movies:
        if m["duration_min"] > threshold:
            count += 1
    return count


# --- Этап 4: Строки ---

def normalize_title(title: str) -> str:
    words = title.split(" ")
    normalized = []
    for w in words:
        if not w:
            continue
        normalized.append(w[0].upper() + w[1:].lower())
    return " ".join(normalized)


def make_slug(title: str) -> str:
    normalized = normalize_title(title)
    lower = normalized.lower()
    return lower.replace(" ", "-")


def format_report_line(movie: Dict[str, Any]) -> str:
    title = movie["title"]
    year = movie["year"]
    rating = movie["rating"]
    duration_str = duration_in_hours(movie["duration_min"])
    # genres — это set, поэтому сортируем и делаем строку
    genres_sorted = sorted(movie["genres"])
    genres_str = ", ".join(genres_sorted)
    return f'"{title}" ({year}) — {rating}/10, {duration_str}, жанры: {genres_str}'


# --- Этап 5: Списки ---

def titles_sorted_by_rating(movies: List[Dict[str, Any]]) -> List[str]:
    sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
    return [m["title"] for m in sorted_movies]


def top_n_by_rating(movies: List[Dict[str, Any]], n: int = 3) -> List[Tuple[str, float]]:
    sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
    result = [(m["title"], m["rating"]) for m in sorted_movies[:n]]
    return result


# --- Этап 6: Словари ---

def count_by_genre(movies: List[Dict[str, Any]]) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for m in movies:
        for g in m["genres"]:
            counts[g] = counts.get(g, 0) + 1
    return counts


def actor_filmography(movies: List[Dict[str, Any]]) -> Dict[str, List[str]]:
    filmography: Dict[str, List[str]] = {}
    for m in movies:
        for actor in m["actors"]:
            filmography.setdefault(actor, []).append(m["title"])
    return filmography


def high_rating_titles_dict(movies: List[Dict[str, Any]]) -> Dict[str, float]:
    avg = average_rating(movies)
    return {m["title"]: m["rating"] for m in movies if m["rating"] > avg}


# --- Этап 7: Множества ---

def all_genres(movies: List[Dict[str, Any]]) -> Set[str]:
    genres = set()
    for m in movies:
        genres.update(m["genres"])
    return genres


def common_actors(movie1: Dict[str, Any], movie2: Dict[str, Any]) -> Set[str]:
    set1 = set(movie1["actors"])
    set2 = set(movie2["actors"])
    return set1 & set2


def genres_only_in_one(movies_a: List[Dict[str, Any]], movies_b: List[Dict[str, Any]]) -> Set[str]:
    set_a = set()
    set_b = set()
    for m in movies_a:
        set_a.update(m["genres"])
    for m in movies_b:
        set_b.update(m["genres"])
    return set_a - set_b


# --- Этап 8: Итераторы и генераторы ---

def iter_high_rated(movies: List[Dict[str, Any]], min_rating: float = 8.0):
    for m in movies:
        if m["rating"] >= min_rating:
            yield m


def total_duration_high_rated(movies: List[Dict[str, Any]], min_rating: float = 7.0) -> int:
    return sum(m["duration_min"] for m in movies if m["rating"] > min_rating)


# --- Этап 9: Итоговый отчёт ---

def build_report(movies: List[Dict[str, Any]]) -> None:
    avg_rating = average_rating(movies)
    oldest, newest, avg_age = catalog_age_stats(movies)

    top_3 = top_n_by_rating(movies, 3)
    genre_counts = count_by_genre(movies)
    all_g = all_genres(movies)

    print("ОТЧЁТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {avg_rating}")
    print(f"Средний возраст фильмов: {avg_age} лет")
    print()

    print("Топ-3 фильма:")
    for title, rating in top_3:
        movie = next((m for m in movies if m["title"] == title), None)
        if movie:
            print("  " + format_report_line(movie))
    print()

    print("Фильмов по жанрам:")
    # Сортировка по убыванию количества
    for genre, count in sorted(genre_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {genre} — {count}")
    print()

    all_genres_list = sorted(all_g)
    print("Все жанры каталога:", ", ".join(all_genres_list))


if __name__ == "__main__":
    build_report(movies)