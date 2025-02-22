from typing import List, Union, Tuple

n: int = 5

name: str = "Guido van Rossum"


def sum(a: int, b: int) -> int:
    return a + b

# Define a list of integers
numbers: List[int] = [1, 2, 3, 4, 5]

# Define a tuple containing an integer and a string
data: Tuple[int, str] = (1, "Guido van Rossum")

# Define a variable that can be either an integer or a string
value: Union[int, str] = 5
