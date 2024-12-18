import string

# Функция вывода исключений в терминал для пользователя
def Warning(parametr):
    if parametr == 'name':
        print("Некорректное имя.", "Это поле обязательное.", "Имя должно содержать только латинские буквы, цифры и пробелы, первая буква – заглавная",  "Повторите ввод", sep = '\n')
    elif parametr == 'surname':
        print("Некорректная фамилия.", "Это поле обязательное.", "Фамилия должна содержать только латинские буквы, цифры и пробелы, первая буква – заглавная", "Повторите ввод", sep='\n')
    elif parametr == 'phone':
        print("Некорректный номер телефона", "Это поле обязательное.", "Номер должен содержать 11 цифр.", "Повторите ввод", sep='\n')
    elif parametr == 'date':
        print("Некорректная дата рождения.", "Формат полный - ДД.ММ.ГГГГ.", "Повторите ввод.", sep="\n")

# Функция, которая обрабатывает пользовательский ввод имени/фамилии и возвращает его, если оно корректно.
# Эта функция будет ждать ввода до тех пор, пока пользователь не введет корректное имя/фамилию (состоящее только из букв)
# parametr - параметр для функции, который определяет, функция принимает имя или фамилию. 
# Функция масштабирована до ввода имени и фамилии для избежания дублирования кода
def set_name(parametr):
    
    # переменная-флаг для контроля того, правильно ли ввел имя пользователь
    correct_name = False
    # информация для пользователя 
    print(f"Введите {parametr}. Это поле обязательное.")

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

# Функция ввода номера телефона пользователем. Работает по тому же принципу, что и set_name(parametr)
def set_phone():

    # Переменная, которая контролирует корректность введенного номера
    correct_phone = False
    # Информация для пользователя
    print("Введите номер телефона. Это поле обязательное.")

    # Блок ввода и обработки данных
    while (not correct_phone):

        phone = input()

        # Проверка на длину введенных данных
        if (len(phone) == 0) or (len(phone) < 11) or (len(phone) > 12) or (len(phone) == 12 and phone[0] != '+'):
            Warning('phone')
            continue
        
        # Автозамена 8 на +7
        if (phone[0] == '+'):
            if (phone[1] == '7'):
                phone = '8' + phone[2:]
            else:
                # если после + идет не 7, то номер некорректен
                print("После '+' должна идти цифра 7")
                Warning('phone')
                continue
        
        # проверка на то, что номер состоит только из цифр
        if (phone.isdigit()):
            correct_phone = True
        else:
            Warning('phone')
            continue

    return phone

# Функция ввода даты рождения. 
def set_date():

    # переменная контроля корректности введенной даты
    correct_date = False
    # информация для пользователя
    print("Введите дату рождения. Формат ДД.ММ.ГГГГ. Это поле необязательное, его можно не заполнять")

    #блок ввода и обработки данных
    while (not correct_date):

        date = input()

        # Если поле пусто, то принимаем ввод, так как оно опциональное
        if (len(date) == 0):
            return date
        
        # Проверка на правильные разделители и формат в целом
        if date[2] != '.' or date[5] != '.':
            Warning('date')
            continue

        # Сплитим по "." для удобной проверки формата ввода
        temp_date = date.split(".")

        # Проверяем на то, что год состоит из 4 символов
        if len(temp_date[2]) != 4:
            Warning('date')
            continue

        # Проверка на тип данных
        for x in temp_date:
            if (not x.isdigit()):
                Warning('date')
                break
        else:
            # Проверка на корректность даты
            
            day = int(temp_date[0])
            month = int(temp_date[1])
            year = int(temp_date[2])

            
            if (1 <= month <= 12):
                # Проверяем день, если в месяце 31 день
                if (month in [1, 3, 5, 7, 8, 10, 12]):
                    if day > 31 or day == 0:
                        Warning('date')
                        continue
                    else:
                        correct_date = True
                # Проверяем день, если в месяце 30 дней
                elif (month in [4, 6, 9, 11]):
                    if (day > 30 or day == 0):
                        Warning('date')
                        continue
                    else:
                        correct_date = True

                # Проверка на високосный год и количество дней в феврале
                elif (month == 2):
                    if (year % 4 == 0 or year % 400 == 0):
                        if (day > 29):
                            Warning('date')
                            continue
                        else:
                            correct_date = True
                    else:
                        if (day > 28):
                            Warning('date')
                            continue
                        else:
                            correct_date = True
            else:
                Warning('date')
                continue
            

    
    # Склеивание даты обратно в строку
    out_date = temp_date[0] + '.' + temp_date[1] + '.' + temp_date[2]

    return out_date       

date = set_date()
print(date)
