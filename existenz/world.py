import random
from sys import stdout

from globe import Globe

class World(object):
    def __init__(self, size=10):
        self._size = size
        self._day = 0

        # create the two globes for current and future world states
        self._current_globe = Globe(self._size)
        self._future_globe = Globe(self._size)

        # seed the current world
        random.seed(1)  #todo: raul - replace this will random configuration
        for location in self.globe:
            location.plant = random.randint(0, 1)

        self.dump_world()

    @property
    def globe(self):
        return self._current_globe.locations

    @property
    def size(self):
        return self._size

    def rotate(self, days=1):
        #todo: raul - add the life rules resolution
        self._day

    def dump_world(self):
        stdout.write('-- day: ' + str(self._day) + '\n')
        for x in range(0, self.size):
            for y in range(0, self.size):
                index = (self.size * x) + y
                loc = self._current_globe.locations[index]
                stdout.write(str(loc))
            stdout.write('\n')
