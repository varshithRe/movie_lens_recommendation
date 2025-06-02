#tests for item based collaborative filter method
import pytest
from src.item_recom import get_similar_movies

def test_get_similar_movies_valid_title():
    titles = get_similar_movies('Godfather')

    assert isinstance(titles, list)
    assert len(titles) == 6
    assert all(isinstance(title, str) for title in titles)

def test_get_similar_movies_invalid_title():

    with pytest.raises(ValueError):
        get_similar_movies('No movie')