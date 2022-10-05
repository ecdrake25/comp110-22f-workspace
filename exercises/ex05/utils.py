"""EX05 Utility Functions."""

__author__ = "730467957"


def only_evens(x: list[int]) -> list[int]:
    """Returns only the even elements of input parameter."""
    i: int = 0
    result: list[int] = list()
    while i < len(x):
        if x[i] % 2 == 0:
            result.append(x[i])
        i += 1
    return result


def concat(x: list[int], y: list[int]) -> list[int]:
    """Combines two lists."""
    i: int = 0
    new: list[int] = list()
    while i < len(x):
        new.append(x[i])
        i += 1

    i = 0
    while i < len(y):
        new.append(y[i])
        i += 1
    return new


def sub(a: list[int], b: int, c: int) -> list[int]:
    """Creates new list containing certain indices."""
    outcome: list[int] = list()
    if b < 0:
        b = 0
    if c > len(a):
        c = len(a) - 1
    else: 
        c -= 1
    if len(a) == 0 or b > len(a) or c <= 0:
        return list()
    outcome.append(a[b])
    outcome.append(a[c])
    return outcome