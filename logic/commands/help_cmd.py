from logic.help_text import HELP_MESSAGE

def handle_help(msg: str):
    if msg in ["help", "допомога", "поміч"]:
        return HELP_MESSAGE
    return None
