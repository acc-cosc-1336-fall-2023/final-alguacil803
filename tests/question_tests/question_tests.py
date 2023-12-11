#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_b.question_b import get_most_likely_ancestor_consensus

class Test_Config(unittest.TestCase):

    def test_question_b(self):
        positions = get_most_likely_ancestor_consensus("GATATATGCATATACTT", "ATAT")
        x = positions[0]
        y = positions[1]
        z = positions[2]
        self.assertEqual(x, 2)
        self.assertEqual(y, 4)
        self.assertEqual(z, 10)

