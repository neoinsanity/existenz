from location import Location


class Globe(object):
    def __init__(self, size=5):
        self._size = size
        self._total_locations = size * size

        self._locations = []
        for x in range(0, self._size):
            for y in range(0, self._size):
                location = Location(x, y)
                self._locations.append(location)

    @property
    def locations(self):
        return self._locations

    @property
    def size(self):
        return self._size

    def get_location(self, x, y):
        """

        :param x:
        :param y:
        :return:
        :rtype: Location
        """
        index = (x * self._size) + y
        x_out_of_bound = x < 0 or x >= self._size
        y_out_of_bound = y < 0 or y >= self._size
        if index > self._total_locations or x_out_of_bound or y_out_of_bound:
            raise IndexError('No coordinate (%s, %s)' % (x, y))
        return self._locations[index]

    def get_neighbors(self, x, y):
        """

        :param x:
        :param y:
        :return:
        :rtype: list
        """
        n = list(self.locations[index] for index in self._neighbors(x,y))

        return n

    def _neighbors(self, x, y):
        indexes = list()
        for a in [-1, 0, 1]:
            for b in [-1, 0, 1]:
                x_ordinate = (x + a) % self.size
                y_ordiante = (y + b) % self.size
                index = (self.size * x_ordinate) + y_ordiante
                indexes.append(index)
        return indexes
