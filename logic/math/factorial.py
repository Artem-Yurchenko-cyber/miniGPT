import math
def factorial_number(n: int) -> int:
    """Обчислює факторіал числа"""
    if n < 0:
        raise ValueError("Факторіал визначений лише для невід'ємних чисел")
    return math.factorial(n)