import sys
from datetime import datetime

# Попросил нейросеть название модуля и функцию для определения времени

WATER_RECOMMENDATION_ML_PER_KG = 30
ML_IN_LITER_WATER = 1000
MORNING_START_HOUR = 5
DAY_START_HOUR = 11
EVENING_START_HOUR = 16
NIGHT_START_HOUR = 21
AGE_ENDINGS_FOR_GOD = (1, 21, 31, 41, 51, 61, 71, 81, 91, 101)
AGE_ENDINGS_FOR_GODA = (
    2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44,
    52, 53, 54, 62, 63, 64, 72, 73, 74,
    82, 83, 84, 92, 93, 94, 102, 103, 104,
)
AGE_LET_START_1 = 5
AGE_LET_END_1 = 20
AGE_LET_START_2 = 25
AGE_LET_END_2 = 30
AGE_LET_START_3 = 35
AGE_LET_END_3 = 40
AGE_LET_START_4 = 45
AGE_LET_END_4 = 50
AGE_LET_START_5 = 55
AGE_LET_END_5 = 60
AGE_LET_START_6 = 65
AGE_LET_END_6 = 70
AGE_LET_START_7 = 75
AGE_LET_END_7 = 80
AGE_LET_START_8 = 85
AGE_LET_END_8 = 90
AGE_LET_START_9 = 95
AGE_LET_END_9 = 100

# Попросил нейросеть подсказать как исправить ошибки связанные с UTF-8,
# при использовании pytest
# Принудительно используем UTF-8 для stdout и stderr

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')
if sys.stderr.encoding != 'utf-8':
    sys.stderr.reconfigure(encoding='utf-8')

# 1. Знакомство
# Получаем текущий час (0–23)
what_time_is_it = datetime.now().hour

# Определяем приветствие в зависимости от времени
# Этих команд и функций не было в 1 первом спринте,
# но они были в вводной части, если время меньше или равно a или меньше b,
# то будет time_of_today
if MORNING_START_HOUR <= what_time_is_it < DAY_START_HOUR:
    time_of_today = 'Доброе утро'
elif DAY_START_HOUR <= what_time_is_it < EVENING_START_HOUR:
    time_of_today = 'Добрый день'
elif EVENING_START_HOUR <= what_time_is_it < NIGHT_START_HOUR:
    time_of_today = 'Добрый вечер'
else:
    time_of_today = 'Доброй ночи'

# Запрашиваем имя с автоматически подобранным приветствием
user_name = input(f'{time_of_today}, введите ваше имя: ').strip()

# Спроси возраст и сохрани в переменную user_age
# (не забудь преобразовать в число)
while True:
    try:
        user_age = int(input('Введите ваш возраст: '))
        break
    except ValueError:
        print('Ошибка: возраст должен быть целым числом. Попробуйте ещё раз.')

# Определяем правильную форму слова, чтобы при выводе не писал всегда г.
# Правила склонения слова "год" по русскому языку:
# 1, 21, 31... → "год"; 2–4, 22–24... → "года"; 5–20, 25–30... → "лет"
# Писать константу под каждое число я думаю не надо,будет слишком много

if user_age in AGE_ENDINGS_FOR_GOD:
    age_word = 'год'
elif user_age in AGE_ENDINGS_FOR_GODA:
    age_word = 'года'
elif (
    AGE_LET_START_1 <= user_age <= AGE_LET_END_1
    or AGE_LET_START_2 <= user_age <= AGE_LET_END_2
    or AGE_LET_START_3 <= user_age <= AGE_LET_END_3
    or AGE_LET_START_4 <= user_age <= AGE_LET_END_4
    or AGE_LET_START_5 <= user_age <= AGE_LET_END_5
    or AGE_LET_START_6 <= user_age <= AGE_LET_END_6
    or AGE_LET_START_7 <= user_age <= AGE_LET_END_7
    or AGE_LET_START_8 <= user_age <= AGE_LET_END_8
    or AGE_LET_START_9 <= user_age <= AGE_LET_END_9
):
    age_word = 'лет'

# 2. Сбор данных
# Запроси вес (в кг) и сохрани в user_weight (тип float)
while True:
    try:
        user_weight = float(input('Введите свой вес в килограммах: '))
        break
    except ValueError:
        print(
            'Ошибка: вес должен быть числом (например 70 или 70.5). '
            'Попробуйте ещё раз.',
        )

# Запроси рост (в метрах, например 1.75) и сохрани в user_height (тип float)
while True:
    try:
        user_height = float(input(
            'Введите свой рост в метрах '
            'используя точку, например 1.75: '
        ))
        break
    except ValueError:
        print(
            'Ошибка: рост должен быть числом (например 1.75).'
            ' Попробуйте ещё раз.',
        )

# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
bmi = round((user_weight / (user_height ** 2)), 1)

# Подсчет воды: вес * 30 мл
# Рассчитай water_l
water_ml = user_weight * WATER_RECOMMENDATION_ML_PER_KG
water_l = water_ml / ML_IN_LITER_WATER


# 4. Вывод красивого результата
print()
print(f'Отчет для пользователя: {user_name} ({user_age} {age_word})')
print(f'Твой Индекс Массы Тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_l:.1f} л. в день')
print('Расчет окончен. Будьте здоровы!')
