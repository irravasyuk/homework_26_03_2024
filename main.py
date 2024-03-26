# Завдання 1
# До вже реалізованого класу «Дріб» додайте статичний метод, який при виклику повертає кількість створених об’єктів
# класу «Дріб».
class Fraction:
    count = 0

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        Fraction.count += 1

    @staticmethod
    def count_fraction():
        return Fraction.count

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

fraction1 = Fraction(1, 2)
fraction2 = Fraction(3, 4)

print(fraction1 + fraction2)
print(fraction1 - fraction2)
print(fraction1 * fraction2)
print(fraction1 / fraction2)

print("\nКількість створених об'єктів класу Fraction: ", Fraction.count_fraction())

# Завдання 2
# Створіть клас для конвертування температури з Цельсія
# у Фаренгейт, і навпаки. У класі має знаходитися два статичні
# методи: для конвертування з Цельсія у Фаренгейт і для конвертування з Фаренгейта у Цельсій. Також клас має розрахувати
# кількість підрахунків температури та повернути це значення
# статичним методом.
class temperature_converter:
    count = 0

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        temperature_converter.count += 1
        return (celsius * 9 / 5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        temperature_converter.count += 1
        return (fahrenheit - 32) * 5 / 9

    @staticmethod
    def get_count():
        return temperature_converter.count


celsius = float(input("Введіть температуру в градусах Цельсія: "))
fahrenheit = float(input("Введіть температуру в градусах Фаренгейт: "))

converted_fahrenheit = temperature_converter.celsius_to_fahrenheit(celsius)
converted_celsius = temperature_converter.fahrenheit_to_celsius(fahrenheit)

print(f"Конветрування з температури в градусах Целісія до градусів Фаренгейт: {converted_fahrenheit}")
print(f"Конветрування з температури в градусах Фаренгейт до градусів Целісія: {converted_celsius}")

print(f"Кількість підрахунків температури: {temperature_converter.get_count()}")

# Завдання 3
# Створіть клас для конвертування з метричної системи в
# англійську, та навпаки. Реалізуйте функціональність у вигляді
# статичних методів. Обов’язково реалізуйте конвертування
# заходів довжини.
class LengthConverter:
    count = 0

    @staticmethod
    def meters_to_foot(meters):
        LengthConverter.count += 1
        return meters * 3.2808

    @staticmethod
    def foot_to_meters(foot):
        LengthConverter.count += 1
        return foot / 3.2808

    @staticmethod
    def kilometers_to_miles(kilometers):
        LengthConverter.count += 1
        return kilometers * 0.62137

    @staticmethod
    def miles_to_kilometers(miles):
        LengthConverter.count += 1
        return miles / 0.62137

    @staticmethod
    def meters_to_yards(meters):
        LengthConverter.count += 1
        return meters * 1.094

    @staticmethod
    def yards_to_meters(yards):
        LengthConverter.count += 1
        return yards / 1.094

    @staticmethod
    def get_count():
        return LengthConverter.count

meters_len = 20
foot_len = 10
kilometers_len = 30
miles_len = 35
meters_len2 = 25
yards_len = 15

convert_to_foot = LengthConverter.meters_to_foot(meters_len)
convert_to_meters = LengthConverter.foot_to_meters(foot_len)
convert_to_miles = LengthConverter.kilometers_to_miles(kilometers_len)
convert_to_kilometers = LengthConverter.miles_to_kilometers(miles_len)
convert_to_yards = LengthConverter.meters_to_yards(meters_len2)
convert_to_meters2 = LengthConverter.yards_to_meters(yards_len)

print(f"{meters_len} метрів - {convert_to_foot} футів")
print(f"{foot_len} футів - {convert_to_meters} метрів")
print(f"{kilometers_len} кілометрів - {convert_to_miles} миль")
print(f"{miles_len} миль - {convert_to_kilometers} кілометрів")
print(f"{meters_len2} метрів - {convert_to_yards} ярдів")
print(f"{yards_len} ярдів - {convert_to_meters2} метрів")

print("Кількість підрахунків довжини: ", LengthConverter.get_count())

# Завдання 4
#  Створіть клас InformationSystem, який має атрибут data
# - словник, де ключі - це імена користувачів, а значення -
# список їх контактів. Реалізуйте методи класу для додавання
# нових користувачів та їх контактів.
class InformationSystem:
    __data = {}

    @classmethod
    def add_user(cls, user):
        if user not in cls.__data:
            cls.__data[user] = []

    @classmethod
    def add_contact(cls, user, contact):
        if user in cls.__data:
            cls.__data[user].append(contact)
        else:
            print("Такого користувача немає в системі.")

    @classmethod
    def get_data(cls):
        return cls.__data

InformationSystem.add_user("Іван")
InformationSystem.add_user("Петро")

InformationSystem.add_contact("Іван", "Юлія")
InformationSystem.add_contact("Петро", "Вікторія")
InformationSystem.add_contact("Петро", "Богдан")

print(InformationSystem.get_data())
