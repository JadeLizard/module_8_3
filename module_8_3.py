class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

class Car():
    def __init__(self, model, x, numbers):
        self.model = model
        self.vin = self.__is_valid_vin(x)
        self.numbers = self.__is_valid_numbers(numbers)

    def __is_valid_vin(self, x):
        if not isinstance(x, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if not (1000000 <= x <= 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return x


    def __is_valid_numbers(self, numbers):
         if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
         if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
         return numbers

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
