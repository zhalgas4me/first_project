correct_password = "0000"
popytka = 3
chet = 0

while chet < popytka:
    pass_ = input("Введите пароль чтобы открыть ноутбук: ")

    if pass_ == correct_password:
        print("Ноутбук открыт")
        break
    else:
        print("Неверный пароль")
        chet += 1

if chet == popytka:
    print("3 попытки прошли. Доступ закрыт.")



name = input("Напишите свое имя: ")
print("Имя студента" + " " + name)
age = input("Напишите возраст: ")
print("Студент" + " " + name + " " + age + " " + "лет")

if int(age) <= 18:
    print("Вам нет 18+ лет, пожалуйста, подождите 18+ летия")
    quit()
    
else:
    print("Welcome to my club")
    
time = input("Какое время вы можете прийти (пн,ср,пт): ")
pon = "пн"
sr = "ср"
pch = "пт"
if time == pon:
    print("В понедельник урок с 10:00")
elif time == sr:
    print("В среду с 12:00")
elif time == pch:
    print("Урок с 14:30")
else:
    print("В другое время мы не работаем")
print("welcom to my курс ")

while True:
    correct_pass = input("Придумайте пароль: ")
    login = input("Придумайте логин: ")

    pass_in_while = input("Введите пароль: ")
    login_while = input("Введите логин: ")

    if pass_in_while == correct_pass and login_while == login:
        print("ДОСТУП ОТКРЫТ")
        break
    else:
        print("Логин или пароль не верные")

print("переходите по ссылке и смотрите первый урок www.zhalgas.kz/lesson")
