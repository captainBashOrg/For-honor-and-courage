from time import sleep
#from datetime import datetime
from threading import Thread

print("За честь и отвагу!")


class Knight(Thread):

    def __init__(self, name, power):
        self.kname = name
        self.power = power
        super().__init__()

    def run(self):
        print(f'Донесение от {self.kname}, на нас напали!')
        enemies = 100
        days = 0
        while enemies > 0:
            sleep(1) # поправить на 1
            days += 1
            enemies -= self.power
            if enemies < 0:
                enemies = 0
            print(f'{self.kname} сражается {days} день(дня)..., осталось {enemies} воинов противника.')
        print(f'{self.kname} одержал победу спустя {days} дней(дня)!')


# Создание класса
knight1 = Knight('Sir Lancelot', 10)
knight2 = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
# Запуск потоков
knight1.start()
knight2.start()
#остановка потоков
knight1.join()
knight2.join()
# Вывод строки об окончании сражения
print('Все битвы завершены! Враг разгромлен!')
