import unittest
import sys

from ontic import ontic_type

from existenz.organism import CharGene, IntGene
from existenz.organism.gene import BaseGene


class GeneTest(unittest.TestCase):
    def test_base_gene(self):
        base_gene = BaseGene()
        self.assertIsNotNone(base_gene)
        self.assertEqual(0.01, base_gene.mut_prob)

        self.assertRaisesRegexp(NotImplementedError,
                                'Must be implemented by subclasses.',
                                base_gene.mutate)

        self.assertRaisesRegexp(NotImplementedError,
                                'Must be implemented by subclasses.',
                                base_gene.random_value)

    def test_default_char_gene(self):
        char_gene = CharGene()
        self.assertIsNotNone(char_gene)
        self.assertEqual(0.01, char_gene.mut_prob)
        self.assertEqual('\xff', char_gene.rand_max)
        self.assertEqual('\x00', char_gene.rand_min)
        self.assertEqual(None, char_gene.value)
        ontic_type.validate_object(char_gene)

    def test_char_gene_random_value(self):
        char_gene = CharGene(rand_min='a', rand_max='z')
        expected_range = map(chr, range(97, 123))
        init_val = char_gene.random_value()
        caught_change = False
        for _ in range(0, 5000):
            ret = char_gene.random_value()
            self.assertIsInstance(ret, str)
            self.assertIn(ret, expected_range)
            caught_change = init_val != ret or caught_change

        self.assertTrue(caught_change,
                        'No random change in value detected')

    def test_char_gene_mutation(self):
        char_gene = CharGene(rand_min='a', rand_max='z')
        init_val = char_gene.value = str('r')
        caught_change = False
        for _ in range(0, 200):
            char_gene.mutate()
            caught_change = init_val != char_gene.value or caught_change

        self.assertTrue(caught_change,
                        'No mutation in value detected')

    def test_default_int_gene(self):
        int_gene = IntGene()
        self.assertIsNotNone(int_gene)
        self.assertEqual(0.01, int_gene.mut_prob)
        self.assertEqual(sys.maxint, int_gene.rand_max)
        self.assertEqual(-sys.maxint - 1, int_gene.rand_min)
        self.assertIsNone(int_gene.value)
        ontic_type.validate_object(int_gene)

    def test_int_gene_random_value(self):
        int_gene = IntGene(rand_min=0, rand_max=250)
        expected_range = [x for x in range(0, 251)]
        init_val = int_gene.random_value()
        caught_change = False
        for _ in range(0, 250):
            ret = int_gene.random_value()
            self.assertIsInstance(ret, int)
            self.assertIn(ret, expected_range)
            caught_change = init_val != ret or caught_change

        self.assertTrue(caught_change,
                        'No random change in value detected')

    def test_int_gene_mutation(self):
        int_gene = IntGene(rand_min=0, rand_max=250)
        init_val = int_gene.value = 1
        caught_change = False
        for _ in range(0, 200):
            int_gene.mutate()
            caught_change = init_val != int_gene.value or caught_change

        self.assertTrue(caught_change,
                        'No mutation in value detected')

    def test_normalize(self):
        int_gene = IntGene(rand_min=0, rand_max=9, value=2)
        int_gene._normalize_value()
        self.assertEqual(2, int_gene.value)
        int_gene.value = 10
        int_gene._normalize_value()
        self.assertEqual(0, int_gene.value)
        int_gene.value = 11
        int_gene._normalize_value()
        self.assertEqual(1, int_gene.value)
        int_gene.value = 20
        int_gene._normalize_value()
        self.assertEqual(0, int_gene.value)
        int_gene.value = 0
        int_gene._normalize_value()
        self.assertEqual(0, int_gene.value)
        int_gene.value = 9
        int_gene._normalize_value()
        self.assertEqual(9, int_gene.value)

        int_gene = IntGene(rand_min=-3, rand_max=9, value=0)
        int_gene._normalize_value()
        self.assertEqual(0, int_gene.value)
        int_gene.value = -3
        int_gene._normalize_value()
        self.assertEqual(-3, int_gene.value)
        int_gene.value = 9
        int_gene._normalize_value()
        self.assertEqual(9, int_gene.value)
        int_gene.value = 10
        int_gene._normalize_value()
        self.assertEqual(-3, int_gene.value)
        int_gene.value = 11
        int_gene._normalize_value()
        self.assertEqual(-2, int_gene.value)
        int_gene.value = 20
        int_gene._normalize_value()
        self.assertEqual(7, int_gene.value)

        int_gene = IntGene(rand_min=3, rand_max=7, value=2)
        int_gene._normalize_value()
        self.assertEqual(7, int_gene.value)
        int_gene.value = 20
        int_gene._normalize_value()
        self.assertEqual(5, int_gene.value)
        int_gene.value = 3
        int_gene._normalize_value()
        self.assertEqual(3, int_gene.value)
        int_gene.value = 0
        int_gene._normalize_value()
        self.assertEqual(5, int_gene.value)
        int_gene.value = -7
        int_gene._normalize_value()
        self.assertEqual(3, int_gene.value)
        int_gene.value = -20
        int_gene._normalize_value()
        self.assertEqual(5, int_gene.value)

        int_gene = IntGene(rand_min=-13, rand_max=-5, value=6)
        int_gene._normalize_value()
        self.assertEqual(-12, int_gene.value)
        int_gene.value = 20
        int_gene._normalize_value()
        self.assertEqual(-7, int_gene.value)
        int_gene.value = 8
        int_gene._normalize_value()
        self.assertEqual(-10, int_gene.value)
        int_gene.value = 0
        int_gene._normalize_value()
        self.assertEqual(-9, int_gene.value)
        int_gene.value = -5
        int_gene._normalize_value()
        self.assertEqual(-5, int_gene.value)
        int_gene.value = -19
        int_gene._normalize_value()
        self.assertEqual(-10, int_gene.value)
