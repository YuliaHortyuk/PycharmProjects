from time import sleep
class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        i = 0
        while i < 30:
            if i in range(0, 30, 3):
                print('red')
                sleep(7)
                i += 1
            elif i in range(1, 30, 3):
                print('yellow')
                sleep(2)
                i += 1
            elif i in range(2, 30, 3):
                print('green')
                sleep(5)
                i += 1

TrafficLight = TrafficLight()
TrafficLight.running()
