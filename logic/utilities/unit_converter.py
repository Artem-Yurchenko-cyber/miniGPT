def convert_length(value: float, unit_from: str, unit_to: str) -> str:
    """Конвертація довжини між км, м, см, мм, мкм, нм"""
    units = {
        "km": 1000,
        "m": 1,
        "cm": 0.01,
        "mm": 0.001,
        "um": 1e-6,   # мікрометр
        "nm": 1e-9,   # нанометр
    }
    if unit_from not in units or unit_to not in units:
        return "Невідомі одиниці довжини."

    meters = value * units[unit_from]
    converted = meters / units[unit_to]
    return f"{value} {unit_from} = {converted} {unit_to}"

def convert_mass(value: float, unit_from: str, unit_to: str) -> str:
    """Конвертація маси між кг, г, мг, т"""
    units = {
        "kg": 1000,
        "g": 1,
        "mg": 0.001,
        "t": 1e6,
    }
    if unit_from not in units or unit_to not in units:
        return "Невідомі одиниці маси."

    grams = value * units[unit_from]
    converted = grams / units[unit_to]
    return f"{value} {unit_from} = {converted} {unit_to}"

def convert_time(value: float, unit_from: str, unit_to: str) -> str:
    """Конвертація часу між годинами, хвилинами, секундами"""
    units = {
        "h": 3600,
        "min": 60,
        "s": 1,
    }
    if unit_from not in units or unit_to not in units:
        return "Невідомі одиниці часу."

    seconds = value * units[unit_from]
    converted = seconds / units[unit_to]
    return f"{value} {unit_from} = {converted} {unit_to}"

def convert_temperature(value: float, unit_from: str, unit_to: str) -> str:
    """Конвертація температури між C, F, K"""
    unit_from = unit_from.lower()
    unit_to = unit_to.lower()

    if unit_from == "c":
        celsius = value
    elif unit_from == "f":
        celsius = (value - 32) * 5/9
    elif unit_from == "k":
        celsius = value - 273.15
    else:
        return "Невідома одиниця температури."

    if unit_to == "c":
        return f"{value} {unit_from.upper()} = {celsius:.2f} C"
    elif unit_to == "f":
        return f"{value} {unit_from.upper()} = {(celsius * 9/5 + 32):.2f} F"
    elif unit_to == "k":
        return f"{value} {unit_from.upper()} = {(celsius + 273.15):.2f} K"
    else:
        return "Невідома одиниця температури."
