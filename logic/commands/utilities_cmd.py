from logic.utilities.randomizer import get_random_number
# тут пізніше підключимо unit_converter, datetime_utils

def handle_utilities(message: str) -> str | None:
    """
    Обробляє всі утиліти (Step 2).
    """
    # пробуємо рандомайзер
    response = get_random_number(message)
    if response:
        return response

    # якщо жодна утиліта не підійшла
    return None
