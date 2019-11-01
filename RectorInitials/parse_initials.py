def rector_init(surname, name, patronymic):
    new_line = name[0].upper() + '. ' + patronymic[0].upper()+'. ' + surname[0].upper() + surname[1:] # Соединяет имя, фамилию, отчество через точки. Вход string выход string.
    return new_line # Выводит результат объединения. Тип - string

