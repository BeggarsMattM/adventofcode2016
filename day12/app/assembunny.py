class Assembunny(object):

  def __init__(self):
    self.a = self.b = self.d = self.pos = 0
    self.c = 1

  def execute(self, code):
    while self.pos < len(code):
      self.process(code[self.pos])

  def process(self, line):
    instruction = line[0]

    if instruction == 'cpy':
      self.copy(line[1], line[2])
    elif instruction == 'inc':
      self.inc(line[1])
    elif instruction == 'dec':
      self.dec(line[1])
    elif instruction == 'jnz':
      self.jnz(line[1], line[2])

  def copy(self, newval, register):
    if type(newval) == int:
      setattr(self, register, newval)
    else:
      setattr(self, register, getattr(self, newval))
    self.pos = self.pos + 1

  def inc(self, register):
    oldval = getattr(self, register)
    setattr(self, register, oldval + 1)
    self.pos = self.pos + 1

  def dec(self, register):
    oldval = getattr(self, register)
    setattr(self, register, oldval - 1)
    self.pos = self.pos + 1

  def jnz(self, val, jump):
    if type(val) != int: val = getattr(self, val)
    if val == 0:
      self.pos = self.pos + 1
    else:
      self.pos = self.pos + jump
