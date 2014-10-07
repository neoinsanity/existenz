import unittest

from existenz.globe import Globe


class GlobeTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_default_globe(self):
        globe = Globe()
        self.assertIsNotNone(globe)
        self.assertEqual(5, globe.size)
        self.assertEqual(25, len(globe.locations))

        location_0_0 = globe.get_location(0, 0)
        self.assertIsNotNone(location_0_0)
        self.assertEqual(0, location_0_0.x)
        self.assertEqual(0, location_0_0.y)
        self.assertEqual((0, 0), location_0_0.coordinate)

        location_4_4 = globe.get_location(4, 4)
        self.assertIsNotNone(location_4_4)
        self.assertEqual(4, location_4_4.x)
        self.assertEqual(4, location_4_4.y)
        self.assertEqual((4, 4), location_4_4.coordinate)

    def test_10_globe(self):
        globe = Globe(size=10)
        self.assertIsNotNone(globe)
        self.assertEqual(10, globe.size)
        self.assertEqual(100, len(globe.locations))

        location_0_0 = globe.get_location(0, 0)
        self.assertIsNotNone(location_0_0)
        self.assertEqual(0, location_0_0.x)
        self.assertEqual(0, location_0_0.y)
        self.assertEqual((0, 0), location_0_0.coordinate)

        location_9_9 = globe.get_location(9, 9)
        self.assertIsNotNone(location_9_9)
        self.assertEqual(9, location_9_9.x)
        self.assertEqual(9, location_9_9.y)
        self.assertEqual((9, 9), location_9_9.coordinate)

    def test_100_globe(self):
        globe = Globe(size=100)
        self.assertIsNotNone(globe)
        self.assertEqual(100, globe.size)
        self.assertEqual(10000, len(globe.locations))

        location_0_0 = globe.get_location(0, 0)
        self.assertIsNotNone(location_0_0)
        self.assertEqual(0, location_0_0.x)
        self.assertEqual(0, location_0_0.y)
        self.assertEqual((0, 0), location_0_0.coordinate)

        location_99_99 = globe.get_location(99, 99)
        self.assertIsNotNone(location_99_99)
        self.assertEqual(99, location_99_99.x)
        self.assertEqual(99, location_99_99.y)
        self.assertEqual((99, 99), location_99_99.coordinate)

    def test_out_of_bound_location_index(self):
        globe = Globe()
        self.assertIsNotNone(globe)
        self.assertEqual(5, globe.size)
        self.assertEqual(25, len(globe.locations))

        self.assertRaisesRegexp(
            IndexError, r'No coordinate \(0, 5\)', globe.get_location, 0, 5)

        self.assertRaisesRegexp(
            IndexError, r'No coordinate \(5, 0\)', globe.get_location, 5, 0)

        self.assertRaisesRegexp(
            IndexError, r'No coordinate \(6, 6\)', globe.get_location, 6, 6)

        self.assertRaisesRegexp(
            IndexError, r'No coordinate \(-1, -1\)', globe.get_location, -1, -1)

    def test_globe_get_neighbors(self):
        globe = Globe()

        neighbors = globe.get_neighbors(0, 0)
        neighbors = globe.get_neighbors(0, 0)
        neighbors = globe.get_neighbors(0, 0)
        expected_neighbors = [
            (4, 4), (4, 0), (4, 1),
            (0, 4), (0, 1),
            (1, 4), (1, 0), (1, 1)]
        neighbors_coordinates = [(l.x, l.y) for l in neighbors]
        self.assertListEqual(expected_neighbors, neighbors_coordinates)

        neighbors = globe.get_neighbors(4, 4)
        expected_neighbors = [
            (3, 3), (3, 4), (3, 0),
            (4, 3), (4, 0),
            (0, 3), (0, 4), (0, 0)]
        neighbors_coordinates = [(l.x, l.y) for l in neighbors]
        self.assertListEqual(expected_neighbors, neighbors_coordinates)

        neighbors = globe.get_neighbors(2, 3)
        expected_neighbors = [
            (1, 2), (1, 3), (1, 4),
            (2, 2), (2, 4),
            (3, 2), (3, 3), (3, 4)]
        neighbors_coordinates = [(l.x, l.y) for l in neighbors]
        self.assertListEqual(expected_neighbors, neighbors_coordinates)
