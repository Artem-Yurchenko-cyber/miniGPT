def handle_greet(msg: str):
    if msg in ["привіт", "hi", "hello", "хай"]:
        return "Вітаю! Я міні chat-bot, з чим я можу вам допомогти сьогодні? напишіть 'help', щоб дізнатися мої можливості"
    return None
