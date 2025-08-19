# def handle_greet(msg: str):
#     if msg in ["привіт", "hi", "hello", "хай"]:
#         return "Вітаю! Я міні chat-bot, як я можу вам допомогти сьогодні?"
#     return None


def handle_greet(msg: str):
    if msg in ["привіт", "hi", "hello", "хай", "q", "чого хоче лана", "чого хоче Лана"]:
        if msg in ["q", "чого хоче лана", "чого хоче Лана"]:
            return "Світлана хоче зіграти у гру 'правда або брехня'"
        return "Вітаю! Я міні chat-bot, як я можу вам допомогти сьогодні?"
    return None