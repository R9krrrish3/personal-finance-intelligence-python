from datetime import datetime


def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def validate_amount(amount):
    try:
        value = float(amount)
        return value > 0
    except ValueError:
        return False


def normalize_category(category):
    return category.strip().lower()
