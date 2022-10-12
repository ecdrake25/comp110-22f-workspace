"""EX07 Practice with Dictionaries."""

__author__ = "730467957"


def invert(k: dict[str, str]) -> dict[str, str]:
    """Invert a dictionary."""
    result: dict[str, str] = {}
    frequency: dict[str, int] = {}
    for key in k:
        result[k[key]] = key

    for key in k:
        if k[key] in frequency:
            frequency [k[key]] += 1
        else:
            frequency[k[key]] = 1

    for key in frequency:
        if frequency[key] > 1:
            raise KeyError("Duplicate key values have been found in the dictionary.")
    
    return result


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


def favorite_color(x: dict[str, str]) -> str:
    """Determines the color that appears the most frequently."""
    i: int = 0
    tracker: dict[str, int] = {}
    numbers: list[int] = []
    if x == {}:
        return {}
    for key in x:
        if x[key] in tracker:
            tracker[x[key]] += 1
        else:
            tracker[x[key]] = 1
        
    for key in tracker:
        numbers.append(tracker[key])

    maximum : int = max(numbers)

    for key in tracker:
        if maximum == tracker[key]:
            return key

    
def count(x: list[str]) -> dict[str, int]:
    """Count of the number of times the value appeared."""
    outcome: dict[str, int] = {}
    if x == []:
        return []

    for item in x:
        if item in outcome:
            outcome[item] += 1
        else:
            outcome[item] = 1
    return outcome
