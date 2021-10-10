name = input('Введите ваше имя ')
age = int(input('Введите ваш возраст '))
period = int(input('Введите период '))
future_age = str(age + period)
print (name + ', через ' + str(period) +' лет вам будет ' + future_age + ' лет ')
if int(future_age) % 5 == 0:
    print('У вас будет юбилей!')