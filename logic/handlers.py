from logic.commands.greet_cmd import handle_greet
from logic.commands.math_cmds import handle_math
from logic.commands.utilities_cmd import handle_utilities

COMMAND_HANDLERS = [
    handle_greet,
    handle_math,
    handle_utilities,
]


def handle_message(message: str) -> str:
    if not message:
        return "Напишіть щось, щоб я міг відповісти."

    msg = message.strip().lower()

    for handler in COMMAND_HANDLERS:
        response = handler(msg)
        if response is not None:
            return response

    return "Не зрозумів команду. Перегляньте інструкцію із користування, яка розташована праворуч зверху."
