import string

# Функция, которая обрабатывает пользовательский ввод имени и возвращает его, если оно корректно.
# Эта функция будет ждать ввода до тех пор, пока пользователь не введет корректно имя (состоящее только из букв)

# Функция вывода исключений в терминал для пользователя
def Warning(parametr):
    if parametr == 'name':
        print("Некорректное имя.", "Имя должно содержать только латинские буквы, цифры и пробелы, первая буква – заглавная",  "Повторите ввод", sep = '\n')
    elif parametr == 'surname':
        print("Некорректная фамилия.", "Фамилия должна содержать только латинские буквы, цифры и пробелы, первая буква – заглавная", "Повторите ввод", sep='\n')

def get_name(parametr):
    
    # переменная-флаг для контроля того, правильно ли ввел имя пользователь
    correct_name = False
    # информация для пользователя 
    print(f"Введите {parametr}")

    # цикл, который позволяет принимать ввод, пока пользователь не введет корректные данные
    while (not correct_name):
        
        name = input()

        # Проверка на пустоту строки
        if len(name) == 0:
            Warning(f"{parametr}")
            continue

        # Проверка первой буквы в имени
        if name[0] in string.ascii_lowercase or name[0].isdigit():
            Warning(f"{name}")
            continue

        # Проверка всего слова на корректность 
        for x in name:
            if x not in string.ascii_letters and not x.isdigit():
                Warning(f"{parametr}")
                break
        else:
            correct_name = True

    return name



