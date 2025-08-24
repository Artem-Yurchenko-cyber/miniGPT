from datetime import datetime, timedelta

# Часові пояси відносно України (UTC+3 умовно)
TIME_ZONES = {
    "ukraine": 0,    # базовий
    "usa": -7,       # приклад — східне узбережжя США (Нью-Йорк)
    "japan": +6,     # Токіо
    "uk": -2,        # Лондон
    "germany": -1,   # Берлін
}

def get_current_time() -> str:
    """Повертає поточний час у форматі dd/mm/yyyy hh:mm:ss"""
    now = datetime.now()
    return now.strftime("%d/%m/%Y %H:%M:%S")

def get_time_in_country(country: str) -> str:
    """Повертає час у вибраній країні відносно України"""
    country = country.lower()
    if country not in TIME_ZONES:
        return f"Невідомо, який час у '{country}'."

    offset = TIME_ZONES[country]
    now = datetime.now() + timedelta(hours=offset)
    return f"Час у {country.capitalize()}: {now.strftime('%d/%m/%Y %H:%M:%S')}"

def get_date_after_days(days: int) -> str:
    """Повертає дату через N днів"""
    future = datetime.now() + timedelta(days=days)
    return f"Дата через {days} днів: {future.strftime('%d/%m/%Y')}"
