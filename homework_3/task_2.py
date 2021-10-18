def person_info(name, surname, birth, city, e_mail, phone):
    print(f'{name} {surname} {birth} {city} {e_mail} {phone}')


n = input('Введите имя ')
s = input('Введите фамилию ')
b = input('Введите дату рождения ')
c = input('Введите город ')
m = input('Введите e_mail ')
p = input('Введите номер телефона ')
person_info(name=n, surname=s, birth=b, city=c, e_mail=m, phone=p)
