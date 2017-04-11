class Generator(object):

  def __init__(self, salt):
    self.salt = salt

  def generate(self, n):
    pass

  def hash_generator(self, number):
    import md5
    while True:
      yield md5.new(self.salt + str(number)).hexdigest()
      number += 1

  def get_next_hash(self):
    import re
    gh = self.hash_generator(0)
    hash = ''
    pattern = re.compile(r"(\w)\1{2,}")
    while not pattern.match(hash):
      hash = next(gh)
    return hash
