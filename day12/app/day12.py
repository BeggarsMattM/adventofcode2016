from app.assembunny import Assembunny

input = """cpy 1 a
cpy 1 b
cpy 26 d
jnz c 2
jnz 1 5
cpy 7 c
inc d
dec c
jnz c -2
cpy a c
inc a
dec b
jnz b -2
cpy c b
dec d
jnz d -6
cpy 19 c
cpy 14 d
inc a
dec d
jnz d -2
dec c
jnz c -5""".split("\n")

def toint(x):
  if x.lstrip("-").isdigit():
    return int(x)
  else:
    return x

input = map(lambda x: x.split(" "), input)
input = map(lambda x: map(toint, x), input)
input = map(tuple, input)

assembunny = Assembunny(dict(a=0, b=0, c=0, d=0))

assembunny.execute(input)

print assembunny.registers['a']
