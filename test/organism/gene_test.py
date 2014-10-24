import unittest
import sys

from ontic import ontic_type

from existenz.organism import IntGene


class GeneTest(unittest.TestCase):
    def test_default_instance(self):
        int_gene = IntGene()
        ontic_type.perfect_object(int_gene)
        self.assertIsNotNone(int_gene)
        self.assertEqual(int_gene.mut_prob, 0.01)
        self.assertEqual(sys.maxint, int_gene.rand_max)
        self.assertEqual(-sys.maxint - 1, int_gene.rand_min)
        self.assertIsNone(int_gene.value)
