import random

def get_random_number(start: int = 0, end: int = 100) -> int:
    """
    Генерує випадкове число у діапазоні від start до end.
    """
    return random.randint(start, end)
