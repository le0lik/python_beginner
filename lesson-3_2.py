def print_personal_info(name, sname, year, city, email, phone):
    """
    Выводит персональные данные

    :param name: string
    :param sname: string
    :param year: string
    :param city: string
    :param email: string
    :param phone: string
    """
    print(f"Имя: {name}; Фамилия: {sname}; Год рождения: {year}; "
          f"Город проживания: {city}; Email: {email}; Телефон: {phone}")


print_personal_info(name="Вася", sname="Пупкин", email="vpupkin@mail.ru", \
                    phone="8-800-1234567", city="Дудинка", year="1980")
