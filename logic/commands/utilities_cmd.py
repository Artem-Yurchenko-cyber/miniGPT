from logic.utilities import randomizer, datetime_utils, unit_converter

def handle_utilities(message: str) -> str:
    if message.startswith("random"):
        return randomizer.get_random_number()

    if message.startswith("time"):
        parts = message.split()
        if len(parts) == 1:
            return datetime_utils.get_current_time()
        elif len(parts) == 2:
            return datetime_utils.get_time_in_country(parts[1])
        else:
            return "Формат: 'time' або 'time usa'."

    if message.startswith("date"):
        parts = message.split()
        if len(parts) == 2 and parts[1].startswith("+"):
            try:
                days = int(parts[1][1:])
                return datetime_utils.get_date_after_days(days)
            except ValueError:
                return "Невірний формат числа."
        return "Формат: 'date +N'."

    if message.startswith("convert"):
        parts = message.split()
        if len(parts) != 4:
            return "Формат: convert <число> <звідки> <куди>"

        try:
            value = float(parts[1])
        except ValueError:
            return "Невірне число."

        unit_from = parts[2].lower()
        unit_to = parts[3].lower()

        # Визначаємо тип конвертації
        if unit_from in ["km", "m", "cm", "mm", "um", "nm"]:
            return unit_converter.convert_length(value, unit_from, unit_to)
        elif unit_from in ["kg", "g", "mg", "t"]:
            return unit_converter.convert_mass(value, unit_from, unit_to)
        elif unit_from in ["h", "min", "s"]:
            return unit_converter.convert_time(value, unit_from, unit_to)
        elif unit_from in ["c", "f", "k"]:
            return unit_converter.convert_temperature(value, unit_from, unit_to)
        else:
            return "Невідомі одиниці для конвертації."

    return None
