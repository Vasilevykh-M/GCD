import os
import datetime
from GCD import *


# добавление логов в отдельный файл
def push_log(file_, content, params, log = False):
    time_ = datetime.datetime.now().time()
    for i in params:
        file_.write(i + " ")
    file_.write(str(content) + (" Получено из логов" if log else "") + " ")
    file_.write(str(time_) + "\n")

def write_console(content, log = False):
    print("Result: " + str(content) + (" Получено из логов" if log else ""))

# ввод выбора пользоватея
def get_user_input():
    choice_ = input("Введите 2 числа через пробел: ")
    choice_ = choice_.split(' ')
    return choice_


# удаление файла логов, кроме созданного в данный момент
def delete_logs():
    log_lst = os.listdir("logs")
    print("File remove:")
    for log in log_lst[:-1]:
        file_rm = "logs/" + log
        print(file_rm)
        os.remove(file_rm)


# создание имени файла для логов
def create_filename():
    cur_datetime = datetime.datetime.now()
    cur_date = str(cur_datetime.date()).replace("-", "_")
    cur_time = cur_datetime.time()
    filename = r"logs/{0}_{1}_{2}_{3}_log.txt".format(cur_date, cur_time.hour, cur_time.minute, cur_time.second)
    return filename


if __name__ == '__main__':
    gcd = GCD(0, 0)

    if not os.path.isdir("logs"):
        os.mkdir("logs")

    file = open(create_filename(), 'w')

    print("Привет пользователь.\n"
          "Данная программа умеет считать НОД 2 чисел.")

    choice = get_user_input()

    while choice[0] != 'q':

        try:
            if choice[0] == "rm_logs":
                delete_logs()
                choice = get_user_input()
                continue

            gcd.a = int(float(choice[0]))
            gcd.b = int(float(choice[1]))

            if gcd.a == 0 or gcd.b == 0:
                push_log(file, 'Некорректный ввод', choice)
                write_console('Некорректный ввод')
                file.close()
                break

            if (gcd.Results.get((gcd.a, gcd.b))) is not None:
                push_log(file, gcd.Results.get((gcd.a, gcd.b)), choice, True)
                write_console(gcd.Results.get((gcd.a, gcd.b)), True)
            elif gcd.Results.get((gcd.b, gcd.a)) is not None:
                push_log(file, gcd.Results.get((gcd.b, gcd.a)), choice, True)
                write_console(gcd.Results.get((gcd.b, gcd.a)), True)
            else:
                rez = gcd.calc()
                push_log(file, rez, choice)
                write_console(rez)

        except Exception:
            push_log(file, 'Некорректный ввод', choice)
            write_console('Некорректный ввод')

        choice = get_user_input()
    print('Пока пользователь')
    file.close()
