import math
import os
from sympy import *


# Сделано Козловским Дмитрием ПР-22.101.
y_string = ""
x = Symbol('x')


def rewrite_formule_math(_formule: str) -> str:
    if "sin" in _formule:
        _formule = _formule.replace("sin", "math.sin")
    if "cos" in _formule:
        _formule = _formule.replace("cos", "math.cos")
    if "tan" in _formule:
        _formule = _formule.replace("tan", "math.tan")
    if "ctan" in _formule:
        _formule = _formule.replace("ctan", "1 / math.tan")
    if "log" in _formule:
        _formule = _formule.replace("log", "math.log")
    if " e " in _formule:
        _formule = _formule.replace(" e ", " 2.71182818284")
    if " pi " in _formule:
        _formule = _formule.replace(" pi ", "3.14")
    if "sympy." in _formule:
        _formule = _formule.replace("sympy.", "math.")

    # print(_formule)
    return _formule


def rewrite_formule_sympy(_formule: str) -> str:
    if "math." in _formule:
        _formule = _formule.replace("math.", "")
        # _formule = _formule.replace("math.", "sympy.")
    return _formule


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
    y_string_w = y_string
    y_string_w = rewrite_formule_math(y_string)
    y_string_w = rewrite_formule_sympy(y_string_w)
    # return float(eval(y_string_w.replace(" x ", str(_x))))
    return float(eval(y_string_w.replace("x", str(_x))))


def y_first_derivative_result(_x: float) -> float:
    global y_string, x
    y_string_fd_w = rewrite_formule_math(y_string)
    y_string_fd_w = rewrite_formule_sympy(y_string_fd_w)
    y_string_fd_w = diff(y_string_fd_w)
    # print(y_string_fd_w)

    return float(eval(str(y_string_fd_w).replace("x", str(_x))))


def y_second_derivative_result(_x: float) -> float:
    global y_string, x
    y_string_sd_w = rewrite_formule_math(y_string)
    y_string_sd_w = rewrite_formule_sympy(y_string_sd_w)
    y_string_sd_w = diff(y_string_sd_w)
    y_string_sd_w = diff(y_string_sd_w)
    # print(y_string_sd_w)

    return float(eval(str(y_string_sd_w).replace("x", str(_x))))


def write_help():
    print("\n---Спецификация ввода функций---",
          "\n\tВводить десятичные числа через точку. [К примеру, 2.4]",
          "\n\tДля возведения в степень нужно писать слитно число, две звёздочки и степень. ",
          "[К примеру, 2**4 = 16]",
          # "\n\tДля записи более сложных функций нужно добавлять приписку \"math.\". ",
          # "[К примеру, синус икс записывается как math.sin( x )]",
          # "\n\tДля вписания одной неизвесной переменной икс нужно отделить её с ОБЕИХ сторон пробелами. ",
          # "[К примеру, квадратный корень из икс будет записываться как sqrt( x )]",
          "\n\tОбязательно указывайте приоритет (порядок) выполнения операций с помощью скобочек. ",
          "[К примеру, (2 + 2) * 2 = 8]",
          "\n\tЧисла Pi и Эйлера записываются как pi и e соответственно.",
          "\n\tЛогариф записывается как log(число в степени, основание). ",
          "[К примеру, натуральный логарифм записывается как log(1, e )]",
          "\n\tКотангенс записываются как ctan( x )",
          "\n\n\tПример правильно записанной функции: sin(2 * x) - log(x, e )\n")


def choose_method() -> str:
    print("\n---Введите метод расчёта---",
          "\n* Метод половинного деления - mhd *",
          "\n* Метод касательных - mk *",
          "\n* Метод хорд - mh *")

    answer = ""
    while True:
        answer = str(input("[mhd | mk | mh]: "))
        answer = answer.lower()

        if answer == "mhd" or answer == "mk" or answer == "mh":
            break
    return answer


class Program(object):

    def __init__(self):
        pass
        self.a = 0.0
        self.b = 0.0
        self.c = 0.0
        self.e = 0.0
        self.bool_continue = False

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
                    self.bool_continue = True

                elif answer == "нет":
                    self.set_abe()

                else:
                    print("Команда не распознана. Выход...")

            else:
                self.bool_continue = True

        except ValueError as ve:
            print("--- Ошибка пользователя. Некорректный ввод ---")
            print(ve)
            self.set_abe()


class Calculation(Program):
    def start_calculation_mhd(self):
        while self.b - self.a >= self.e:

            self.c = (self.b + self.a) / 2

            if y_result(self.a) * y_result(self.c) > 0:
                self.a = self.c
                # print(f">0\na = {self.a}\nb = {self.b}")

            elif y_result(self.a) * y_result(self.c) < 0:
                self.b = self.c
                # print(f"<0\na = {self.a}\nb = {self.b}")

            elif y_result(self.a) == 0.0:
                # print(f"a = {self.a}\nb = {self.b}")
                print("Результат перемножения функций равен нулю...")

        # print(f"a = {self.a}\nb = {self.b}\ne = {self.e}")
        print(f"---\nРезультат равен: {round((self.a + self.b) / 2, len(str(self.e)) - 2)}")
        print(f"Величина ошибки: {(self.b - self.a) / 2}")

    def start_calculation_mk(self):
        x_s = 0
        # print(y_first_derivative_result(self.a))
        # print(y_second_derivative_result(self.a))
        if self.a * y_second_derivative_result(self.a) > 0:
            x_s = self.a
        elif self.b * y_second_derivative_result(self.b) < 0:
            x_s = self.b
        # print(x_s)

        while abs(y_result(x_s) / y_first_derivative_result(x_s)) >= self.e:
            x_s_temp = x_s - (y_result(x_s) / y_first_derivative_result(x_s))
            x_s = x_s_temp
        print("Результат вычисления: {0}".format(x_s))

    def start_calculation_mh(self):
        pass


if __name__ == '__main__':
    print("---Добро пожаловать в программу---\n")
    set_formule()

    App = Program()

    Method = Calculation()
    Method.set_abe()

    answer_method = choose_method()
    if answer_method == "mhd":
        Method.start_calculation_mhd()

    elif answer_method == "mk":
        Method.start_calculation_mk()

    elif answer_method == "mh":
        Method.start_calculation_mh()
    else:
        print("Error on stage choose method to calculation class.")

    os.system("pause")

# test function: math.sin( 2 * x ) - math.log( x , math.e)
# or sin( 2 * x ) - log( x , e )
