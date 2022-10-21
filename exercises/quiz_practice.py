"""Practice for Quiz 3."""

def average_grades(x: dict[str, list[int]]) -> dict[str, float]:
    result: dict[str, float] = {}
    average: float = 0
    i: int = 0
    for student in x:
        for grade in student:
            average += grade
        average = average / 3
        result[student] = average
        average = 0
        i = 0
    
    return result