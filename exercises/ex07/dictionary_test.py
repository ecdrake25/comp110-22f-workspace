"""Tests for EX07."""

__author__ = "730467957"

import pytest
from dictionary import invert
from dictionary import favorite_color
from dictionary import count


def test_invert_empty() -> None:
    """Tests an empty dictionary."""
    k: dict[str, str] = {}
    assert invert(k) == {}


def test_invert_short() -> None:
    """Tests a short list."""
    k: dict[str, str] = {'a': '2', 'b': '3'}
    assert invert(k) == {'2': 'a', '3': 'b'}


def test_error() -> None:
    """Tests for error."""
    with pytest.raises(KeyError):
        x: dict[str, str] = {'kris': 'jordan', 'michael': 'jordan'}
        invert(x)


def test_empty() -> None:
    """Tests an empty dictionary."""
    x: dict[str, str] = {}
    assert favorite_color(x) == ""


def test_double() -> None:
    """Tests what is returned with colors of equal frequencies."""
    x: dict[str, str] = {'emma': 'blue', 'thomas': 'blue', 'paula': 'red', 'mark': 'red'}
    assert favorite_color(x) == 'blue'


def test_example() -> None:
    """Tests a long list with variety of colors."""
    x: dict[str, str] = {'a': 'blue', 'b': 'yellow', 'c': 'green', 'd': 'purple', 'e': 'red', 'f': 'orange', 'g': 'purple'}
    assert favorite_color(x) == 'purple'


def test_empty_count() -> None:
    """Tests for an empty string."""
    x: list[str] = []
    assert count(x) == {}


def test_short() -> None:
    """Tests for a short list."""
    x: list[str] = ['dog', 'dog', 'cat']
    assert count(x) == {'dog': 2, 'cat': 1}


def test_count() -> None:
    """Tests a singular string."""
    x: list[str] = ['happy']
    assert count(x) == {'happy': 1}