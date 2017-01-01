class Assembunny(object):

  def __init__(self, registers):
    self.registers = registers

  def execute(self, code):
    pos = 0
    while pos < len(code):
      pos += self.process(code[pos])

  def process(self, line):
    instruction, x, y = line[0], line[1], line[-1]

    if   instruction == 'cpy': return self.copy(x, y)
    elif instruction == 'inc': return self.inc(x)
    elif instruction == 'dec': return self.dec(x)
    elif instruction == 'jnz': return self.jnz(x, y)

  def val(self, x):
    return self.registers[x] if x in self.registers else x

  def copy(self, val, register):
    self.registers[register] = self.val(val)
    return 1

  def inc(self, register):
    self.registers[register] += 1
    return 1

  def dec(self, register):
    self.registers[register] -= 1
    return 1

  def jnz(self, val, jump):
    return 1 if self.val(val) == 0 else jump
