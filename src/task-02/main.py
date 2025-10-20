from typing import Callable, Generator
import re


def generator_numbers(text: str)->Generator[float, None, None]:
    """Number generator from text"""

    # Regular expression for numbers
    regex = r'\b\d+(?:\.\d+)?\b'

    for string_number in re.findall(regex, text):
        try:
            # convert the string to a float and return it via yield
            yield float(string_number)
        except ValueError:
            # skip any invalid values
            continue

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]):
    """Sums all numbers from text using the func generator."""
    return sum(func(text))

if __name__ == '__main__':
    text = """
    Загальний дохід працівника складається 
    з декількох частин: 1000.01 як основний 
    дохід, доповнений додатковими надходженнями 
    27.45 і 324.00 доларів.
    """

    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
