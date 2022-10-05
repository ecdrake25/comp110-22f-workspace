"""EX05 Utility Test."""

__author__ = "730467957"


from utils import only_evens
from utils import sub
from utils import concat


def test_only_evens_empty() -> None:
    """Tests an empty list."""
    x: list[int] = []
    assert only_evens(x) == []


def test_only_evens() -> None:
    """Short list test."""
    x: list[int] = [1, 2, 3]
    assert only_evens(x) == [2]


def test_only_evens_long() -> None:
    """Tests a long list."""
    x: list[int] = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert only_evens(x) == [8, 6, 4, 2, 0]


def test_concat_empty() -> None:
    """Tests a single empty string."""
    x: list[int] = list()
    y: list[int] = [3, 4, 5]
    assert concat(x, y) == [3, 4, 5]


def test_concat_empty_both() -> None:
    """Tests two empty strings."""
    x: list[int] = list()
    y: list[int] = list()
    assert concat(x, y) == []


def test_concat() -> None:
    """Two lists of different lengths."""
    x: list[int] = [1, 2]
    y: list[int] = [8, 6, 5, 4]
    assert concat(x, y) == [1, 2, 8, 6, 5, 4]


def test_sub_edge() -> None:
    """Empty list is provided."""
    a: list[int] = list()
    b: int = 0
    c: int = 4
    assert sub(a, b, c) == []


def test_sub_negative() -> None:
    """Start index is negative."""
    a: list[int] = [1, 2, 3, 4]
    b: int = -1
    c: int = 3
    assert sub(a, b, c) == [1, 3]


def test_sub_end() -> None:
    """End index is too large."""
    a: list[int] = [2, 4, 6, 8]
    b: int = 1
    c: int = 5
    assert sub(a, b, c) == [4, 8]


def test_sub_0() -> None:
    """End is at most 0."""
    a: list[int] = [2, 4, 6, 8]
    b: int = 1
    c: int = 0
    assert sub(a, b, c) == []