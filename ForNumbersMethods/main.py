import math, os

# Сделано Козловским Дмитрием ПР-22.101.

def y_result(_x: float) -> float:
    return float(round((math.sin(2 * _x) - math.log(_x, math.e)), 8))


class Program(object):

    def __init__(self):

        self.a = 0.0
        self.b = 0.0
        self.c = 0.0
        self.e = 0.0

    def set_abe(self):

        try:

            self.a = float(input("Введите левую границу отрезка: "))
            self.b = float(input("Введите правую границу отрезка: "))
            self.e = float(input("Введите минимальную точность результата: "))

            if self.a > self.b:

                print("Начало отрезка больше, чем его конец")
                answer = input("Желаете их поменять местами?[Да/Нет]: ").lower()

                if answer == "да":
                    temp = self.a
                    self.a = self.b
                    self.b = temp
                    print(f"Теперь начальная граница: {self.a}, а конечная граница: {self.b}")
                    self.start_calculation()

                elif answer == "нет":
                    self.set_abe()

                else:
                    print("Команда не распознана. Выход...")

            else:
                self.start_calculation()

        except ValueError as ve:
            print("--- Ошибка пользователя. Некорректный ввод ---")
            # print(ve)
            self.set_abe()

    def start_calculation(self):
        x = self.a

        while self.b - self.a >= self.e:

            self.c = (self.b + self.a) / 2

            if y_result(self.a) * y_result(self.c) > 0:
                self.a = self.c
                # print(f"a = {self.a}\nb = {self.b}")

            elif y_result(self.a) * y_result(self.c) < 0:
                self.b = self.c
                # print(f"a = {self.a}\nb = {self.b}")

            elif y_result(self.a) == 0.0:
                # print(f"a = {self.a}\nb = {self.b}")
                print("Результат перемножения функций равен нулю...")

        print(f"---\nРезультат равен: {round((self.a + self.b) / 2, len(str(self.e)) - 2)}")
        print(f"Величина ошибки: {(self.b - self.a) / 2}")


if __name__ == '__main__':
    print("---Добро пожаловать в программу---\nЗаданная функция этой программы y = sin(2x) - ln(x).\n")
    App = Program()
    App.set_abe()
    os.system("pause")
