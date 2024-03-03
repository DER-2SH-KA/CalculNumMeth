import os
import sys

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
        _formule = _formule.replace(" e ", " 2.7182818284")
    if " pi " in _formule:
        _formule = _formule.replace(" pi ", "3.14")
    if "sympy." in _formule:
        _formule = _formule.replace("sympy.", "math.")
    if "^" in _formule:
        _formule = _formule.replace("^", "**")

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
          "\n\tЧисла Pi и Эйлера записываются как ' pi ' и ' e ' соответственно[Без кавычкек].",
          "\n\tЛогариф записывается как log(число в степени, основание). ",
          "[К примеру, натуральный логарифм записывается как log(1, e )]",
          "\n\tКотангенс записываются как ctan( x )",
          "\n\n\tПример правильно записанной функции: sin(2 * x) - log(x, e )\n")


def choose_method() -> str:
    print("\n---Введите метод расчёта---",
          "\n* Метод половинного деления - mhd *",
          "\n* Метод касательных - mk *",
          "\n* Метод хорд - mh *",
          "\n* Метод простой итерации - mui *")

    answer = ""
    while True:
        answer = str(input("[mhd | mk | mh | mui]: "))
        answer = answer.lower()

        if answer == "mhd" or answer == "mk" or answer == "mh" or answer == "mui":
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
        while abs(self.b - self.a) >= self.e:
            self.c = (self.b + self.a) / 2

            if y_result(self.a) * y_result(self.c) > 0:
                self.a = self.c
                print(f"{y_result(self.a)} * {y_result(self.c)} > 0")
                print(f">0\na = {self.a}\nb = {self.b}")

            elif y_result(self.a) * y_result(self.c) < 0:
                self.b = self.c
                print(f"{y_result(self.a)} * {y_result(self.c)} < 0")
                print(f"<0\na = {self.a}\nb = {self.b}")

            elif y_result(self.a) == 0.0:
                # print(f"a = {self.a}\nb = {self.b}")
                print("Результат перемножения функций равен нулю...")
            print(f"|{self.b} - {self.a}| >= {self.e} - {abs(self.b - self.a) >= self.e}")

        print(f"a = {self.a}\nb = {self.b}\ne = {self.e}")
        print(f"---\nРезультат равен: {round((self.a + self.b) / 2, len(str(self.e)) - 2)}")
        print(f"Величина ошибки: {round((self.b - self.a) / 2, (len(str(self.e)) - 2) * 2)}")

    def start_calculation_mk(self):
        x_s = 0.0
        iteration = 1
        # print(y_first_derivative_result(self.a))
        # print(y_second_derivative_result(self.a))
        y_s_d_a = 0.0
        y_s_d_b = 0.0

        try:
            y_s_d_a = y_second_derivative_result(self.a)
        except TypeError:
            print(f"Произошла ошибка вычисления второй производной значения {self.a}",
                  "\nПожалуйста, вычислите вторую производную вручную и введите её, ",
                  "или напишите \"exit\", если хотите прекратить вычисление.")
            while True:
                typeerroranswer = str(input("[exit/вторая производная]"))
                if typeerroranswer.lower() == "exit":
                    sys.exit()
                else:
                    y_s_d_a = float(typeerroranswer)
                    break

        try:
            y_s_d_b = y_second_derivative_result(self.b)
        except TypeError:
            print(f"Произошла ошибка вычисления второй производной значения {self.b}",
                  "\nПожалуйста, вычислите вторую производную вручную и введите её, ",
                  "или напишите \"exit\", если хотите прекратить вычисление.")
            while True:
                typeerroranswer = str(input("[exit/вторая производная]"))
                if typeerroranswer.lower() == "exit":
                    sys.exit()
                else:
                    y_s_d_b = float(typeerroranswer)
                    break

        if y_result(self.a) * y_s_d_a > 0:
            x_s = self.a
        elif y_result(self.b) * y_s_d_b > 0:
            x_s = self.b
        print(f"X0 = {x_s}")
        # print(x_s)
        x_s_temp = 0.0

        while abs(y_result(x_s) / y_first_derivative_result(x_s)) >= self.e:
            try:
                y_x_s_f_d = y_first_derivative_result(x_s)
                x_s_temp = x_s - (y_result(x_s) / y_x_s_f_d)
            except TypeError:
                print(f"Произошла ошибка вычисления производной значения {x_s}",
                      "\nПожалуйста, вычислите вторую производную вручную и введите её, ",
                      "или напишите \"exit\", если хотите прекратить вычисление.")
                while True:
                    typeerroranswer = str(input("[exit/вторая производная]"))
                    if typeerroranswer.lower() == "exit":
                        sys.exit()
                    else:
                        y_x_s_f_d = float(typeerroranswer)
                        x_s_temp = x_s - (y_result(x_s) / y_x_s_f_d)
                        break
            x_s = x_s_temp
            print(f"X{iteration} = {x_s} - {y_result(x_s)} / {y_first_derivative_result(x_s)} = {x_s}")
            iteration += 1
        print("Результат вычисления: {0}".format(round(x_s, len(str(self.e)) - 2)))

    def start_calculation_mh(self):
        x_s = 0.0
        iteration = 1
        y_s_d_a = 0.0
        y_s_d_b = 0.0
        temp_x = 10000.0
        dynamic_value = 100.0
        static_value = 0.0

        try:
            y_s_d_a = y_second_derivative_result(self.a)
        except TypeError:
            print("Не удалось вычислить вторую производную числа {0}".format(self.a))
            print("Пожалуйста введите его отдельно или напишите \"exit\" для выхода из программы.")
            typeerroranswer = str(input("[exit/число]: ")).lower()

            if typeerroranswer == "exit":
                sys.exit()
            else:
                y_s_d_a = float(typeerroranswer)

        try:
            y_s_d_b = y_second_derivative_result(self.b)
        except TypeError:
            print("Не удалось вычислить вторую производную числа {0}".format(self.b))
            print("Пожалуйста введите его отдельно или напишите \"exit\" для выхода из программы.")
            typeerroranswer = str(input("[exit/число]: ")).lower()

            if typeerroranswer == "exit":
                sys.exit()
            else:
                y_s_d_b = float(typeerroranswer)

        if (y_result(self.a) * y_s_d_a > 0) and (y_result(self.b) * y_s_d_b < 0):
            dynamic_value = self.b
            static_value = self.a
        elif (y_result(self.a) * y_s_d_a < 0) and (y_result(self.b) * y_s_d_b > 0):
            dynamic_value = self.a
            static_value = self.b

        print(f'X0 = {dynamic_value}')
        while abs(dynamic_value - temp_x) > self.e:
            temp_x = dynamic_value
            try:
                next_x = dynamic_value - (((static_value - dynamic_value) / (y_result(static_value) - y_result(dynamic_value))) * y_result(dynamic_value))
                print(f"X{iteration} = {dynamic_value} - ((({static_value} - {dynamic_value}) / ({y_result(static_value)} - {y_result(dynamic_value)})) * {y_result(dynamic_value)})")
            except Exception:
                print(f"Не удалось вычислить следующую границу числа {dynamic_value}.")
                print("Пожалуйста введите её отдельно или напишите \"exit\" для выхода из программы")
                typeerroranswer = str(input("[exit/число]: ")).lower()

                if typeerroranswer == "exit":
                    sys.exit()
                else:
                    next_x = float(typeerroranswer)
            print(f"X{iteration} = {next_x}")
            iteration += 1
            dynamic_value = next_x
        print(f"Результат вычисления: {round(dynamic_value, len(str(self.e)) - 2)}.")

    def start_calculation_mui(self):
        print("Введите формулу выраженного числа x:")
        x_formula = str(input("[Формула]: "))
        x_formula = x_formula.lower()

        if x_formula == "help":
            write_help()
            self.start_calculation_mui()

        # We are Finding q.
        # q - is max derivative of [a, b].
        x_formula = rewrite_formule_math(x_formula)
        x_formula = rewrite_formule_sympy(x_formula)
        x_div = diff(x_formula)
        x_div_a = 0.0
        x_div_b = 0.0
        print(x_div)

        try:
            x_div_a = float(eval(str(x_div).replace("x", str(self.a))))
            print(f"Производная от {self.a} = {x_div_a}")
        except TypeError as typeerror:
            print("\nОшибка вычисления максимальной производной. ",
                  "Попробуйте ввести иначе выраженный x.\n",
                  f"Или введите производную числа {self.a} самостоятельно. ")
            while True:
                typeerroranswer = str(input("[Другая формула - af/ввести самостоятельно - im]: "))
                if typeerroranswer.lower() == "af":
                    self.start_calculation_mui()
                elif typeerroranswer.lower() == "im":
                    x_div_a = float(input(f"Введите значение производной {self.a}: "))
                    break
                else:
                    print("Нераспознааная команда. Проверьте правильность ввода команды.")

        try:
            x_div_b = float(eval(str(x_div).replace("x", str(self.b))))
            print(f"Производная от {self.b} = {x_div_b}")
        except TypeError as typeerror:
            print("\nОшибка вычисления максимальной производной. ",
                  "Попробуйте ввести иначе выраженный x.\n",
                  f"Или введите производную числа {self.b} самостоятельно. ")
            while True:
                typeerroranswer = str(input("[Другая формула - af/ввести самостоятельно - im]: "))
                if typeerroranswer.lower() == "af":
                    self.start_calculation_mui()
                elif typeerroranswer.lower() == "im":
                    x_div_b = float(input(f"Введите значение производной {self.b}: "))
                    break
                else:
                    print("Нераспознааная команда. Проверьте правильность ввода команды.")

        print("x_div_a = {0}\nx_div_b = {1}".format(x_div_a, x_div_b))
        x_s = 0.0
        q = 1.0

        if abs(x_div_a) > 1.0 and abs(x_div_b) > 1.0:
            print("Формула икса (х) не подходит для метода простой итерации,\n",
                  "так как максимальный предел больше единицы.")
            print("Попробуйте ввести другую формулу икса (х)\n")
            self.start_calculation_mui()
        elif (abs(x_div_a) > abs(x_div_b)) or (abs(x_div_a) == abs(x_div_b)):
            q = x_div_a
        else:
            q = x_div_b

        if self.a > self.b or self.a == self.b:
            x_s = self.a
        else:
            x_s = self.b

        a_break = abs((self.e * (1 - q)) / q)
        # print("div_a = {0}\ndiv_b = {1}\nq = {2}\na_break = {3}".format(x_div_a, x_div_b, q, a_break))
        p = 100.0
        iteration = 1
        print(f"X0 = {x_s}")

        while abs(p) > a_break:
            try:
                next_x = float(eval(str(x_formula).replace("x", str(x_s))))
                print(f"X{iteration} = {next_x}")
            except TypeError as typeerror:
                print(f"\nОшибка вычисления значения X{iteration} при значении {x_s}. ",
                      "Попробуйте ввести иначе выраженный x.\n",
                      f"Или введите значение икс (х) числа {x_s} самостоятельно. ")
                while True:
                    typeerroranswer = str(input("[Другая формула - af/ввести самостоятельно - im]: "))
                    if typeerroranswer.lower() == "af":
                        self.start_calculation_mui()
                    elif typeerroranswer.lower() == "im":
                        next_x = float(input(f"Введите значение производной {self.b}: "))
                        break
                    else:
                        print("Нераспознааная команда. Проверьте правильность ввода команды.")
            p = x_s - next_x
            print(f"p = {p}")
            x_s = next_x
            iteration += 1

        print("Результат вычисления: {0}".format(round(x_s, len(str(self.e)) - 2)))


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
    elif answer_method == "mui":
        Method.start_calculation_mui()
    else:
        print("Error on stage choose method to calculation class.")

    os.system("pause")

# test function: math.sin( 2 * x ) - math.log( x , math.e)
# or sin( 2 * x ) - log( x , e )
