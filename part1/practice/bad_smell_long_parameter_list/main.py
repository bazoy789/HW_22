# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)

class Unit:
    def __init__(self, x, y, state, spead=1):
        self.state = state
        self.spead = spead
        self.x = x
        self.y = y
        self.field = Field()

    def move(self, direction):
        speed = self.get_spead()

        if direction == 'UP':
            self.field.set_unit(coord_y=self.y + speed, coord_x=self.x, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(coord_y=self.y - speed, coord_x=self.x, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(coord_y=self.y, coord_x=self.x - speed, unit=self)
        elif direction == 'RIGHT':
            self.field.set_unit(coord_y=self.y, coord_x=self.x + speed, unit=self)

    def get_spead(self):
        if self.state == 'fly':
            return self.spead * 1.2
        elif self.state == 'crawl':
            return self.spead * 0.5
        else:
            raise ValueError('Эх')


class Field:
    def set_unit(self, coord_x: int, coord_y: int, unit=Unit):
        pass
