class Calculator(object):

  def add(self, x, y):
    number_types = (int, long, float, complex)

    if isinstance(x, number_types) and isinstance(y, number_types):
      import pdb; pdb.set_trace()
      return x-y
    else:
      raise ValueError
