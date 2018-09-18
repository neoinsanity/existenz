"""A representation of the World."""
import json
import logging
import random
import uuid
from sys import stdout

from ontic.ontic_type import perfect_object

from existenz.entity import Entity
from existenz.location import Location
from existenz.util_decorator import memoize


def attempt_planting(location):
    if random.randint(0, 1):
        entity = Entity(id=str(uuid.uuid4()), type='plant')
        location.add_entity(entity)
        return entity
    else:
        return None


class World(object):
    """Representation of the world for denizens to live and die."""

    def __init__(self, log=logging.getLogger(), seed=0, size=15):
        self.log = log
        self._seed = seed
        self._size = size
        self._day = 0
        self._total_locations = size * size
        self._entities = list()
        self._entity_location_map = dict()

        self._locations = self._generate_initial_locations()

        # seed the current world
        for location in self.locations:
            planted = attempt_planting(location)
            if planted:
                self._entities.append(planted)
                self._entity_location_map[planted.id] = location

        self.dump_world()

    @property
    def locations(self):
        """A list of the locations in a given globe."""
        return self._locations

    @property
    def size(self):
        """The size of the world length.

        The total number of locations is equivalent to size * size.
        """
        return self._size

    def rotate(self, days=1):
        """Cycle through a given number of days in the world.

        :param days: The number of days the world should life-cycle it denizens.
        :type days: int
        """
        # todo(raul) add the code to iterate that gives each entity a turn
        for iteration in range(0, days):
            self._purculate_populations()
            self._day += 1

        self.dump_world()

    def get_location(self, x_coord, y_coord):
        """Retrieve a given location from given coordinates.

        :param x_coord: The abscissa of the coordinate.
        :type x_coord: int
        :param y_coord: The ordinate of the coordinate.
        :type y_coord: int
        :return: The location for the given coordinates.
        :rtype: existenz.location.Location
        """
        index = (x_coord * self._size) + y_coord
        x_out_of_bound = x_coord < 0 or x_coord >= self._size
        y_out_of_bound = y_coord < 0 or y_coord >= self._size
        if index > self._total_locations or x_out_of_bound or y_out_of_bound:
            raise IndexError('No coordinate (%s, %s)' % (x_coord, y_coord))
        return self._locations[index]

    @memoize
    def get_neighbors(self, x_coord, y_coord):
        """Retrieve the locations adjacent to the given coordinates.

        :param x_coord: The abscissa of the coordinates.
        :type x_coord: int
        :param y_coord: The ordinate of the coordinates.
        :type y_coord: int
        :return: A list of neighbors locations.
        :rtype: list(existenz.location.Location)
        """
        return list(self.locations[index] for index in
                    self._neighbors(x_coord, y_coord))

    def dump_world(self):
        """Method that will dump the state of the current world to stdio."""
        stdout.write('-- day: ' + str(self._day) + '\n')
        for x_coord in range(0, self.size):
            for y_coord in range(0, self.size):
                index = (self.size * x_coord) + y_coord
                loc = self._locations[index]
                self.log.debug(json.dumps(loc))

    def _generate_initial_locations(self):

        locations = []
        for x_coord in range(0, self._size):
            for y_coord in range(0, self._size):
                location = Location(id=(self.size * x_coord) + y_coord,
                                    x=x_coord,
                                    y=y_coord,
                                    type_count=dict(),
                                    entities=dict())
                perfect_object(location)
                locations.append(location)

        return locations

    def _neighbors(self, x_coord, y_coord):
        """Calculates the neighbors to a given coordinate.

        :param x_coord: The abscissa of the target coordinate.
        :type x_coord: int
        :param y_coord: The ordinate of the target coordinate.
        :type y_coord: int
        :return: list
        """
        indexes = list()
        for x_inc in [-1, 0, 1]:
            for y_inc in [-1, 0, 1]:
                if x_inc == 0 and y_inc == 0:
                    # Skip the central location.
                    continue
                x_ordinate = (x_coord + x_inc) % self.size
                y_ordiante = (y_coord + y_inc) % self.size
                index = (self.size * x_ordinate) + y_ordiante
                indexes.append(index)
        return indexes

    def _purculate_populations(self):
        entity_catch_list = list()

        while self._entities:
            entity = self._entities.pop(
                random.randrange(len(self._entities)))
            entity_catch_list.append(entity)
            entity.life_cycle(self, self._entity_location_map[entity.id])

        self._entities = entity_catch_list
