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
    elif parametr == 'command':
        print("Такой команды не существует. Попробуйте еще раз.")
    elif parametr == 'unique':
        print("Запись с таким уникальный идентификатором (Имя+Фамилия) существует. Попробуйте еще раз")

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
        
        # Проверка на то, является ли первый символ цифрой
        if name[0].isdigit():
            Warning(f"{parametr}")
            continue

        # Автозамена первой буквы имени/фамилии на заглавную
        if name[0] in string.ascii_lowercase:
            name = name[0].upper() + name[1:]

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

# Функция для вывода списка возможных комманд пользователю
def list_commands():
    print("------------------------------------------------------------")
    print("Для того, чтобы выполнить команду, введите ее номер в консоль")
    print("1. Добавить новую запись в справочник")
    print("2. Найти запись в справочнике")
    print("3. Посмотреть все записи справочника")
    print("4. Удалить запись")
    print("5. Изменить запись")
    print("6. Посмотреть возраст человека")
    print("7. Завершить работу")
    print("------------------------------------------------------------")

# Объявление констант, хранящих коды команд для удобства и читаемости кода
ADD = 1
FIND = 2
PRINT_ALL = 3
DELETE = 4
REDACT = 5
CALCULATE_AGE = 6
QUIT = 7

def add_record(file):

    isAdded = False

    while(not isAdded):

        # ввод данных 
        name = set_name('name')
        surname = set_name('surname')

        isFailedLoop = False

       
        # ставим указатель в файле в начало файла
        file.seek(0)
         # проверка на существование записи в файле
        for exist_records in file:
            file_record = exist_records.split(' ')
            if (file_record[0] == name and file_record[1] == surname):
                Warning('unique')
                isFailedLoop = True
                break
        else:
            isAdded = True
           
        if (isFailedLoop):
            continue

        phone = set_phone()
        date = set_date()

    record = name + " " + surname + " " + phone + " " + date + '\n'
    # добавляем запись в буфер
    file.write(record)
    # выкидываем запись из буфера в файл на диск
    file.flush()

def print_records(file):
    print("------------------------------------------------------------")
    print("Справочник")
    print("Имя", "Фамилия", "Номер телефона", "Дата рождения")
    
    # ставим указатель в начало файла
    file.seek(0)

    for records in file:
        print(records, end="")

# константа, содержащая пустую строку
nullString = ''

# функция поиска записи по уникальному идентификатору
def uniqueKey_search(key, file):

    # ставим указатель на начало файла
    file.seek(0)

    # выполняем линейных поиск по файлу, сравнивая значения уникального идентификатора
    for record in file:
        splRecord = record.split(' ')
        if (key[0] == splRecord[0] and key[1] == splRecord[1]):
            return record

    # если запись не найдена, функция возвращает пустую строку (она будет обработана)
    return nullString

def search_interface(file):

    # локальные константы для удобства и читабельности кода
    UNIQUE_SEARCH = 1
    QUIT_SEARCH = 2

    
    
    isWorkSearch = True

    while(isWorkSearch):
        # информация для пользователя
        print("1. Поиск по уникальному идентификатору (Имя + Фамилия)")
        print("2. Возврат в главное меню")

        # обработка команды
        command_code = int(input())
        if (command_code > 2 or command_code < 0):
            print("Команда не найдена, попробуй еще раз!")
            continue

        if (command_code == UNIQUE_SEARCH):
            
            # ввода уникального ключа
            name = set_name('name')
            surname = set_name('surname')
            
            # структура для удобства передачи
            key = [name, surname]

            search_result = uniqueKey_search(key, file) 

            if (search_result == nullString):
                print("Запись не найдена!")
            else:
                print(search_result)
        elif (command_code == QUIT_SEARCH):
            break

# Главная функция программы, которая обрабатывает события (команды пользователя)
def event_loop():
    isWork = True
    
    # открытие файла, в котором будет храниться справочник
    file = open("handbook.txt", 'a+')

    # цикл обработки команд 
    while (isWork):
        # вывод доступных команд пользователю
        list_commands()
        
        # обработка введенного значения
        command_code = int(input())
        if (command_code <= 0 or command_code > 7):
            Warning('command')
            continue

        # поиск и выполнение команды, которую выбрал пользователь

        if (command_code == ADD):
            add_record(file)
        elif (command_code == FIND):
            search_interface(file)
        elif (command_code == PRINT_ALL):
            print_records(file)
        elif (command_code == DELETE):
            ...
        elif (command_code == REDACT):
            ...
        elif (command_code == CALCULATE_AGE):
            ...
        elif (command_code == QUIT):
            break
    
    # закрытие файла с справочником
    file.close()


event_loop()