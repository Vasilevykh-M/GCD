from GCD import *
import os
import datetime

def log_push(file, content, time_):
    file.write(str(content)+" ")
    file.write(str(time_) + "\n")

if __name__ == '__main__':
    gcd = GCD(0, 0)
    choise = input("Введите 2 числа через пробел: ")
    choise = choise.split(' ')

    if not os.path.isdir("logs"):
        os.mkdir("logs")

    cur_datetime = datetime.datetime.now()
    cur_date = str(cur_datetime.date()).replace("-", "_")
    cur_time = cur_datetime.time()
    filename = r"logs/{0}_{1}_{2}_{3}_log.txt".format(cur_date, cur_time.hour, cur_time.minute, cur_time.second)
    file = open(filename, 'w')

    while choise[0]!='q':
        time_now = datetime.datetime.now().time()
        try:
            if choise[0] == "rm_logs":
                log_lst = os.listdir("logs")
                for log in log_lst[0:-1]:
                    print("logs/"+log)
                    os.remove("logs/"+log)
                choise = input("Введите 2 числа через пробел: ")
                choise = choise.split(' ')
                continue

            file.write(choise[0] + " " + choise[1] + " ")
            gcd.A = int(float(choise[0]))
            gcd.B = int(float(choise[1]))
            if gcd.A == 0 or gcd.B == 0:
                log_push(file, 'Некорректный ввод', time_now)
                print('Некорректный ввод')
                file.close()
                break

            if (gcd.Results.get((gcd.A, gcd.B))) is not None:
                log_push(file, gcd.Results.get((gcd.A, gcd.B)), time_now)
                print(gcd.Results.get((gcd.A, gcd.B)))
            elif gcd.Results.get((gcd.B, gcd.A)) is not None:
                log_push(file, gcd.Results.get((gcd.B, gcd.A)), time_now)
                print(gcd.Results.get((gcd.B, gcd.A)))
            else:
                log_push(file, gcd.calc(), time_now)
                print(gcd.calc())


        except:
            log_push(file, 'Некорректный ввод', time_now)
            print('Некорректный ввод')

        choise = input("Введите 2 числа через пробел: ")
        choise = choise.split(' ')

    file.close()