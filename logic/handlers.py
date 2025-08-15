import re
from logic.help_text import HELP_MESSAGE

def handle_message(message: str) -> str:
    if not message:
        return "Напишіть щось, щоб я міг відповісти."

    msg = message.strip().lower()

    # Привітання
    if msg in ["привіт", "hi", "hello", "хай"]:
        return "Вітаю! " + HELP_MESSAGE

    # Help
    if msg in ["help", "допомога", "поміч"]:
        return HELP_MESSAGE

    # Математичні операції
    math_match = re.search(r"(\d+)\s*([\+\-\*/])\s*(\d+)", msg)
    if math_match:
        num1 = int(math_match.group(1))
        op = math_match.group(2)
        num2 = int(math_match.group(3))
        if op == "+":
            return str(num1 + num2)
        elif op == "-":
            return str(num1 - num2)
        elif op == "*":
            return str(num1 * num2)
        elif op == "/":
            if num2 != 0:
                return str(num1 / num2)
            else:
                return "Ділення на нуль неможливе."

    # Математика словами (укр/англ)
    if "додай" in msg or "add" in msg:
        nums = list(map(int, re.findall(r"\d+", msg)))
        if len(nums) == 2:
            return str(nums[0] + nums[1])

    if "помнож" in msg or "multiply" in msg:
        nums = list(map(int, re.findall(r"\d+", msg)))
        if len(nums) == 2:
            return str(nums[0] * nums[1])

    return "Не зрозумів команду. Напиши 'help', щоб побачити список можливостей."
