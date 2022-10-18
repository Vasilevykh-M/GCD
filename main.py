from GCD import *
import os
import datetime


# добавление логов в отдельный файл
def log_push(file_, content, params):
    time_ = datetime.datetime.now().time()
    for i in params:
        file_.write(i + " ")
    file_.write(str(content)+" ")
    print('Result: ' + str(content))
    file_.write(str(time_) + "\n")


# ввод выбора пользоватея
def choice_user():
    choice_ = input("Введите 2 числа через пробел: ")
    choice_ = choice_.split(' ')
    return choice_


# удаление файла логов, кроме созданного в данный момент
def delete_logs():
    log_lst = os.listdir("logs")
    print("File remove:")
    for log in log_lst[0:-1]:
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
    choice = choice_user()

    if not os.path.isdir("logs"):
        os.mkdir("logs")

    file = open(create_filename(), 'w')

    while choice[0] != 'q':

        try:
            if choice[0] == "rm_logs":
                delete_logs()
                choice = choice_user()
                continue

            gcd.A = int(float(choice[0]))
            gcd.B = int(float(choice[1]))

            if gcd.A == 0 or gcd.B == 0:
                log_push(file, 'Некорректный ввод', choice)
                file.close()
                break

            if (gcd.Results.get((gcd.A, gcd.B))) is not None:
                log_push(file, gcd.Results.get((gcd.A, gcd.B)), choice)
            elif gcd.Results.get((gcd.B, gcd.A)) is not None:
                log_push(file, gcd.Results.get((gcd.B, gcd.A)), choice)
            else:
                log_push(file, gcd.calc(), choice)

        except Exception:
            log_push(file, 'Некорректный ввод', choice)

        choice = choice_user()

    file.close()
