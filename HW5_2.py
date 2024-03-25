import re
from typing import Callable

def generator_numbers(text: str):
    # Використовуємо регулярний вираз для знаходження всіх дійсних чисел у тексті
    pattern = r'\b\d+\.\d+\b'
    for income in re.finditer(pattern, text):
        yield float(income.group())

def sum_profit(text: str, func: Callable):
    # Використовуємо передану функцію для отримання генератора чисел
    numbers_generator = func(text)
    # Підсумовуємо всі числа, що повертає генератор
    total = sum(numbers_generator)
    return total

# Приклад використання:
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")