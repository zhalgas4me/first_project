# my project
import os
import time

def login():
    os.system("cls")
    correct_password = "0000"
    chet = 0

    while chet < 3:
        pass_ = input("Введите пароль чтобы открыть ноутбук: ")

        if pass_ == correct_password:
            os.system("cls")
            print("Ноутбук открыт")
            time.sleep(2)
            check_age()
        else:
            os.system("cls")
            print(f"Неверный пароль. Осталось попыток: {2 - chet}.")
            chet += 1
            time.sleep(2)

    if chet == 3:
        print("3 попытки прошли. Доступ закрыт.")
        time.sleep(2)
        quit()

def check_age():
    os.system("cls")
    name = input("Напишите свое имя: ")
    print("Имя студента" + " " + name)

    time.sleep(2)

    while True:
        age_input = input("Напишите возраст: ")
        try:
            age = int(age_input)
            break  # Exit the loop if age is valid
        except ValueError:
            print('Недопустимое значение.')
            time.sleep(2)
            os.system("cls")

    print("Студент" + " " + name + " " + str(age) + " " + "лет")

    time.sleep(2)

    if age < 18:
        os.system("cls")
        print("Вам нет 18+ лет, пожалуйста, подождите 18+ летия")
        time.sleep(2)
        check_age()
        
    else:
        os.system("cls")
        print("Welcome to my club")
        time.sleep(2)
        main()

def create_pwd():
    os.system("cls")

    while True:
        correct_pass = input("Придумайте пароль: ")
        login = input("Придумайте логин: ")

        pass_in_while = input("Введите пароль: ")
        login_while = input("Введите логин: ")

        if pass_in_while == correct_pass and login_while == login:
            print("ДОСТУП ОТКРЫТ")
            time.sleep(2)
            prm_end()
        else:
            print("Логин или пароль не верные")
        
        prm_end()
    
def prm_end():
    print("переходите по ссылке и смотрите первый урок www.zhalgas.kz/lesson")
    quit()

def main():
    os.system("cls")
    spec_time = input("Какое время вы можете прийти (пн,ср,пт): ")

    pn = "пн"
    sr = "ср"
    pt = "пт"

    if spec_time == pn:
        print("В понедельник урок с 10:00")
    elif spec_time == sr:
        print("В среду с 12:00")
    elif spec_time == pt:
        print("Урок с 14:30")
    else:
        print("В другое время мы не работаем")

    time.sleep(5)

    print("welcome to my курс ")

    time.sleep(2)
    create_pwd()

login()
