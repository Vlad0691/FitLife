# Проект FitLife - MVP версия 1.0
from datetime import datetime
# Попросил нейросеть название модуля и функцию для определения времени

import sys
# Попросил нейросеть подсказать как исправить ошибки связанные с UTF-8,
# при использовании pytest
# Принудительно используем UTF-8 для stdout и stderr
if sys.stdout.encoding != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")
if sys.stderr.encoding != "utf-8":
    sys.stderr.reconfigure(encoding="utf-8")

WATER_PER_KG = 30
WATER_LIRER_ML = 1000
# 1. Знакомство
# Получаем текущий час (0–23)
what_time_is_it = datetime.now().hour

# Определяем приветствие в зависимости от времени
# Этих команд и функций не было в 1 первом спринте,
# но они были в вводной части, если время меньше или равно a или меньше b,
# то будет time_of_today
if 5 <= what_time_is_it < 11:
    time_of_today = 'Доброе утро'
elif 11 <= what_time_is_it < 16:
    time_of_today = 'Добрый день'
elif 16 <= what_time_is_it < 21:
    time_of_today = 'Добрый вечер'
else:
    time_of_today = 'Доброй ночи'

# Запрашиваем имя с автоматически подобранным приветствием
user_name = input(f'{time_of_today}, введите ваше имя: ')

# Спроси возраст и сохрани в переменную user_age
# (не забудь преобразовать в число)
user_age = int(input('Введите ваш возраст: '))

# Определяем правильную форму слова, чтобы при выводе не писал всегда г.

if user_age in (1, 21, 31, 41, 51, 61, 71, 81, 91, 101):
    age_word = 'год'
elif user_age in (
    2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44,
    52, 53, 54, 62, 63, 64, 72, 73, 74,
    82, 83, 84, 92, 93, 94, 102, 103, 104,
):
    age_word = 'года'
elif (
    5 <= user_age <= 20 or 25 <= user_age <= 30 or 35 <= user_age <= 40
    or 45 <= user_age <= 50 or 55 <= user_age <= 60 or 65 <= user_age <= 70
    or 75 <= user_age <= 80 or 85 <= user_age <= 90 or 95 <= user_age <= 100
):
    age_word = 'лет'

# 2. Сбор данных
# Запроси вес (в кг) и сохрани в user_weight (тип float)
user_weight = float(input('Введите свой вес в килограммах: '))
# Запроси рост (в метрах, например 1.75) и сохрани в user_height (тип float)
user_height = float(input(
    'Введите свой рост в метрах '
    'используя точку, например 1.75: '
))

# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
bmi = user_weight / (user_height ** 2)
bmi = round(bmi, 1)
# Рассчитай bmi (Индекс массы тела)
# Подсчет воды: вес * 30 мл
# Рассчитай water_l
water_ml = user_weight * WATER_PER_KG
water_l = water_ml / WATER_LIRER_ML


# 4. Вывод красивого результата
# Используй f-строку, чтобы вывести приветствие,
# например: "Привет, Иван!"
# Выведи возраст, ИМТ (округленный до 1 знака) и норму воды.
print()
print(f'Отчет для пользователя: {user_name} ({user_age} {age_word})')
print(f'Твой Индекс Массы Тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_l:.1f} л. в день')
print("Расчет окончен. Будьте здоровы!")
