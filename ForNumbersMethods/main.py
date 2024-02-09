import math, os

import numexpr


def try_import_numexpr():
    try:
        from numexpr import evaluate

    except Exception:
        print(Exception)
        os.system("pip install numexpr")
        from numexpr import evaluate


# Сделано Козловским Дмитрием ПР-22.101.
y_string = ""
def set_formule():
    global y_string
    while y_string == "":
        try:
            print("---Введите вашу функцию для вычисления, обязательно придерживаясь правил ввода---",
                  "\n---Правила ввода можете посмореть, введя команду \"help\" без кавычек---")
            y_string = str(input("[Введите функцию]: "))

            if y_string.lower() == "help":
                write_help()
                y_string = ""

        except ValueError as va:
            print("---Ошибка ввода!---")
            print(va)


def y_result(_x: float) -> float:
    global y_string
    return float(numexpr.evaluate(y_string.replace(" x ", str(_x))))


def write_help():
    print("\n---Спецификация ввода функций---",
          "\n\tВводить десятичные числа через точку. [К примеру, 2.4]",
          "\n\tДля возведения в степень нужно писать слитно число, две звёздочки и степень. ",
          "[К примеру, 2**4 = 16]",
          "\n\tДля записи более сложных функций нужно добавлять приписку \"math.\". ",
          "[К примеру, синус икс записывается как math.sin( x )]",
          "\n\tДля вписания одной неизвесной переменной икс нужно отделить её с ОБЕИХ сторон пробелами. ",
          "[К примеру, квадратный корень из икс будет записываться как math.sqrt( x )]",
          "\n\tОбязательно указывайте приоритет (порядок) выполнения операций с помощью скобочек. ",
          "[К примеру, (2 + 2) * 2 = 8]",
          "\n\tЧисла Pi и Эйлера записываются как math.pi и math.e соответственно.",
          "\n\tЛогариф записывается как math.log(число в степени, основание). ",
          "[К примеру, натуральный логарифм записывается как math.log(1, math.e)]",
          "\n\tТангенс и котангенс записываются как math.tan( x ) и (1 / math.tan( x )) соответствено",
          "\n\n\tПример правильно записанной функции: math.sin(2 *  x ) - math.log( x )")


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
    try_import_numexpr()
    print("---Добро пожаловать в программу---\n")
    set_formule()

    App = Program()
    App.set_abe()
    os.system("pause")
