import pytest
from catalog_analysis import (
    average_rating,
    catalog_age_stats,
    duration_in_hours,
    rating_tier,
    decade_label,
    count_long_movies,
    normalize_title,
    make_slug,
    format_report_line,
    titles_sorted_by_rating,
    top_n_by_rating,
    count_by_genre,
    all_genres,
    iter_high_rated,
    build_report,
)

from catalog_analysis import movies

def test_average_rating():
    assert average_rating(movies) == 7.2

def test_duration_in_hours():
    assert duration_in_hours(118) == "1ч 58м"
    assert duration_in_hours(60) == "1ч 0м"

def test_normalize_title():
    assert normalize_title("silent hours") == "Silent Hours"

def test_make_slug():
    assert make_slug("Silent Hours") == "silent-hours"

def test_top_n_by_rating():
    top = top_n_by_rating(movies, 3)
    assert len(top) == 3
    assert top[0][0] == "The Quiet Algorithm"

def test_count_by_genre():
    counts = count_by_genre(movies)
    assert counts["drama"] >= 3

def test_all_genres():
    g = all_genres(movies)
    assert "sci-fi" in g

def test_iter_high_rated():
    high = list(iter_high_rated(movies, min_rating=8.0))
    assert len(high) >= 3

def test_build_report():
    # Просто убедимся, что функция выполняется без ошибок
    build_report(movies)