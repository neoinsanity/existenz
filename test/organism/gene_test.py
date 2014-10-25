import unittest
import sys

from ontic import ontic_type

from existenz.organism import CharGene, IntGene


class GeneTest(unittest.TestCase):
    def test_default_char_gene(self):
        char_gene = CharGene()
        self.assertIsNotNone(char_gene)
        ontic_type.perfect_object(char_gene)
        self.assertEqual(0.01, char_gene.mut_prob)
        self.assertEqual('\xff', char_gene.rand_max)
        self.assertEqual('\x00', char_gene.rand_min)
        self.assertEqual(None, char_gene.value)
        ontic_type.validate_object(char_gene)

    def test_default_int_gene(self):
        int_gene = IntGene()
        self.assertIsNotNone(int_gene)
        ontic_type.perfect_object(int_gene)
        self.assertEqual(0.01, int_gene.mut_prob)
        self.assertEqual(sys.maxint, int_gene.rand_max)
        self.assertEqual(-sys.maxint - 1, int_gene.rand_min)
        self.assertIsNone(int_gene.value)
        ontic_type.validate_object(int_gene)
