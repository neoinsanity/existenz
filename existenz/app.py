#!/usr/bin/env python

import sys

from world import World


class App(object):

    def __init__(self, size = 10):
        # create the world
        self.world = World(size)

    @property
    def current_state(self):
        return self.world.globe

    def step(self, days = 1):
        self.world.rotate(days)


if __name__ == '__main__':
    argv = sys.argv
    app = App(argv=argv)

    app.step()

    # print the results out
    print app.current_state
