import random

def get_random_number(message: str) -> str | None:
    """
    Генерує випадкове число.
    - "random" або "рандом" -> число від 0 до 100
    - "random 1 10" -> число від 1 до 10
    """

    msg = message.strip().lower()
    parts = msg.split()

    if parts[0] in ["random", "рандом"]:
        if len(parts) == 3:  # приклад: "random 1 10"
            try:
                start = int(parts[1])
                end = int(parts[2])
                number = random.randint(start, end)
                return f"Випадкове число від {start} до {end}: {number}"
            except ValueError:
                return "Введіть числа правильно. Приклад: `random 1 10`"

        # тільки "random"
        return f"Ваше випадкове число: {random.randint(0, 100)}"

    return None
