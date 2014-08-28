import unittest

from existenz.app import App


class ExistenzCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_simple_existenz(self):
        app = App()
        self.assertIsNotNone(app)

        app.step()
        print str(app.current_state)
