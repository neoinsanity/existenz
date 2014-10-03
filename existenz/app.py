#!/usr/bin/env python
import argparse
import sys

from world import World


class App(object):
    def __init__(self, rotate=3, size=10):
        self.rotate = rotate

        # create the world
        self.world = World(size)

    def run(self):
        self.world.rotate(self.rotate)


if __name__ == '__main__':
    # Get the args.
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--rotate',
                        default=3,
                        help='Number of days to run.')
    parser.add_argument('-s', '--size',
                        default=10,
                        help='Size of world.')
    args = parser.parse_args()

    # run the app
    app = App(rotate=args.rotate, size=args.size)
    app.run()
