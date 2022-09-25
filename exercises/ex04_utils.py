"""List Utility Functions."""

__author__ = "730467957"


def all(haystack: list[int], needle: int) -> bool:
    """Checking list for given int."""
    if len(haystack) == 0:
        return False
    index: int = 0
    while index < len(haystack):
        if needle == haystack[index]:
            index += 1
        else:
            return False
    return True


def max(input: list[int]) -> int:
    """Returns largest number in the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    index: int = 0
    position: int = 0
    while index < len(input) and position < len(input):
        if input[index] >= input[position]:
            position += 1
        else:
            index += 1
            position = 0
    return input[index]


def is_equal(one: list[int], two: list[int]) -> bool:
    """Checking for equal lists."""
    if len(one) != len(two):
        return False
    i: int = 0
    while i < len(one) and i < len(two):
        if one[i] == two[i]:
            i += 1
        else:
            return False
    return True