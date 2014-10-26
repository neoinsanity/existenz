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

    def test_default_int_gene(self):
        int_gene = IntGene()
        self.assertIsNotNone(int_gene)
        self.assertEqual(0.01, int_gene.mut_prob)
        self.assertEqual(sys.maxint, int_gene.rand_max)
        self.assertEqual(-sys.maxint - 1, int_gene.rand_min)
        self.assertIsNone(int_gene.value)
        ontic_type.validate_object(int_gene)

        int_gene.random_value()

    def test_normalize(self):
        int_gene = IntGene(rand_min=0, rand_max=9, value=2)
        int_gene._normalize_value()
        self.assertEqual(2, int_gene.value)
        int_gene.value = 10
        int_gene._normalize_value()
        self.assertEqual(0, int_gene.value )
        int_gene.value = 11
        int_gene._normalize_value()
        self.assertEqual(1, int_gene.value )
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
