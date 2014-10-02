import json


class Location(object):
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._plant = 0

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def coordinate(self):
        return self.x, self.y

    @property
    def plant(self):
        return self._plant

    @plant.setter
    def plant(self, plant):
        self._plant = plant

    def __repr__(self):
        return json.dumps({'x': self.x, 'y': self.y, 'plant': self.plant})

    def __str__(self):
        return self.__repr__()
