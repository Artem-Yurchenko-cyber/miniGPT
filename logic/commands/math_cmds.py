import re
import math
from logic.math.add import add_numbers
from logic.math.multiply import multiply_numbers
from logic.math.subtract import subtract_numbers
from logic.math.divide import divide_numbers
from logic.math.power import power_numbers
from logic.math.root import root_numbers
from logic.math.factorial import factorial_number

def handle_math(msg: str):
    # Символьна математика (підтримка +, -, *, /, **, sqrt(), factorial())
    if re.fullmatch(r"[0-9\+\-\*\/\^\!\s\(\)]+", msg):
        try:
            # Замінюємо ^ на ** для Python
            expr = msg.replace("^", "**")

            # Замінюємо ! на factorial()
            if "!" in expr:
                expr = re.sub(r"(\d+)!", r"math.factorial(\1)", expr)

            return str(eval(expr, {"__builtins__": None}, {"math": math}))
        except ZeroDivisionError:
            return "Ділення на нуль неможливе."
        except Exception:
            return "Помилка у виразі."

    # Математика словами
    nums = list(map(int, re.findall(r"\d+", msg)))

    if "додай" in msg or "add" in msg:
        return str(add_numbers(nums))

    if "помнож" in msg or "multiply" in msg:
        return str(multiply_numbers(nums))

    if "відніми" in msg or "subtract" in msg:
        return str(subtract_numbers(nums))

    if "поділи" in msg or "divide" in msg:
        return str(divide_numbers(nums))

    if "корінь" in msg or "root" in msg:
        if len(nums) == 2:
            return str(root_numbers(nums[1], nums[0]))  # root power, number
        return "Формат: корінь <ступінь> з <числа>"

    if "степінь" in msg or "power" in msg:
        if len(nums) == 2:
            return str(power_numbers(nums[0], nums[1]))
        return "Формат: число <a> до степеня <b>"

    if "факторіал" in msg or "factorial" in msg:
        if len(nums) == 1:
            return str(factorial_number(nums[0]))
        return "Формат: факторіал <числа>"

    return None
