import unittest
from app.generator import Generator

class Day14(unittest.TestCase):

  def setUp(self):
    self.generator = Generator('abc')

  def test_index_produces_triple:
    triple = self.generator.next_triple(0)
    assert triple[0] == 18

  def test_known_salt(self):
    salts = self.generator.generate(64)
    assert salts[-1][0] == 22728
