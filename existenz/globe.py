from location import Location


class Globe(object):
    def __init__(self, size=10):
        self._size = size

        self._locations = []
        self._map = {}
        for x in range(0, self._size):
            for y in range(0, self._size):
                location = Location(x,y)
                self._locations.append(location)
                self._map[(x, y)] = location

    @property
    def coordinates(self):
        return self._map.keys()

    @property
    def locations(self):
        return self._locations

    @property
    def size(self):
        return self._size

    def get_location(self, x, y):
        return self._map[(x, y)]
