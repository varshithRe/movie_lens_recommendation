#tests for user based collaborative filtering
import pytest
from src.recommend import get_top_n

def test_get_top_n_valid_user():

    titles = get_top_n(user_id=24, n =7)

    assert isinstance(titles, list)
    assert len(titles) == 7
    assert all(isinstance(title, str) for title in titles)

def test_get_top_n_invalid_user():

    with pytest.raises(ValueError):
        get_top_n(user_id=5278728230, n = 10)
