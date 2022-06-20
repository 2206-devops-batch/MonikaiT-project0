import unittest
class Testtotal_expenses(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('y'.upper(), 'Y')
        self.assertEqual('n'.upper(), 'N')
        self.assertEqual('x'.upper(), 'X')
