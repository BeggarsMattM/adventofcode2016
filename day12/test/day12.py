import unittest
from app.assembunny import Assembunny

class TddAdventOfCode2016(unittest.TestCase):

  def setUp(self):
    self.assembunny = Assembunny()

  def test_assembunny_copies_x_into_y(self):
    instruction = ('cpy', 41, 'a')
    self.assembunny.process(instruction)
    self.assertEqual(self.assembunny.a, 41)

  def test_assembunny_increments_value_of_register(self):
    instruction = ('inc', 'a')
    self.assembunny.process(instruction)
    self.assertEqual(self.assembunny.a, 1)

  def test_assembunny_decrements_value_of_register(self):
    instruction = ('dec', 'a')
    self.assembunny.process(instruction)
    self.assertEqual(self.assembunny.a, -1)

  def test_assembunny_handles_group_of_instructions(self):
    code = [('cpy', 41, 'a'), ('inc', 'a'), ('inc', 'a'),
            ('dec', 'a'), ('jnz', 'a', 2), ('dec', 'a')]
    self.assembunny.execute(code)
    self.assertEqual(self.assembunny.a, 42)

  def test_assembunny_copies_values_between_registers(self):
    code = [('cpy', 41, 'a'), ('cpy', 'a', 'b'), ('inc', 'b')]
    self.assembunny.execute(code)
    self.assertEqual(self.assembunny.a, 41)
    self.assertEqual(self.assembunny.b, 42)

  def test_assembunny_can_jnz_based_on_value_or_register(self):
    instruction = ('jnz', 1, 2)
    self.assembunny.process(instruction)
    self.assertEqual(self.assembunny.a, 0)

# class TddInPythonExample(unittest.TestCase):
#
#   def setUp(self):
#     self.calc = Calculator()
#
#   def test_calculator_add_method_returns_correct_result(self):
#     result = self.calc.add(2,2)
#     self.assertEqual(4, result)
#
#   def test_calculator_returns_error_message_if_both_args_not_numbers(self):
#     self.assertRaises(ValueError, self.calc.add, 'two', 'three')
#
#   if __name__ == '__main__':
#     unittest.main()
