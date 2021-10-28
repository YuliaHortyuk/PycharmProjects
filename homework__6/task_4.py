class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} начала движение')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn_right(self):
        print(f'{self.name} повернула направо')

    def turn_left(self):
        print(f' {self.name} повернула налево')

    def show_speed(self):
        return self.speed

    def full_info(self):
        return f'{self.speed} {self.color} {self.name} {self.is_police}'

    def police(self):
        if self.is_police:
            print(f'{self.name} полицейская машина ')
        else:
            print(f' {self.name} не полицейская машина ')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(self, speed, color, name)
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name}  привысила скорость на   {(int(self.speed) - 60)}')
        else:
            print(self.speed)


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(self, speed, color, name)
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(self, speed, color, name)
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        if self.speed > 40:
            return f'{self.name}  привысила скорость на   {(int(self.speed) - 40)}'
        else:
            return self.speed


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(self, speed, color, name)
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


car_1 = SportCar(150, 'красный', 'Ауди спорт', False)
car_2 = WorkCar(70, 'белый', 'Фольксваген', False)
car_3 = TownCar(65, 'синий', 'Джип', False)
car_4 = PoliceCar(50, 'черный', 'Рено', True)

print(car_1.full_info())
print(car_1.show_speed())
print(car_1.go())
print(car_1.police())
print(car_2.full_info())
print(car_2.show_speed())
print(car_2.stop())
print(car_2.police())
print(car_3.full_info())
print(car_3.show_speed())
print(car_3.turn_right())
print(car_4.full_info())
print(car_4.turn_left())
print(car_4.police())
