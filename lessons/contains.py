"""An example of a list utility algorithm."""

# Function with 2 parameters:
# needle - what we are searching for
# haystack - what we're searching for


def contains(needle: str, haystack: list[str]) -> bool:
    index: int = 0
    while index < len(haystack):
        if haystack[index] == needle:
            return True
        else:
            index += 1

    return False
