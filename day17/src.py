import hashlib

def md5_hash_of(code):
    m = hashlib.md5()
    m.update(code)
    return m.hexdigest()

def up(hash, pos):
    [_, y] = pos
    return hash[0] in 'bcdef' and y > 0

def down(hash, pos):
    [_, y] = pos
    return hash[1] in 'bcdef' and y < 3

def left(hash, pos):
    [x, _] = pos
    return hash[2] in 'bcdef' and x > 0

def right(hash, pos):
    [x, _] = pos
    return hash[3] in 'bcdef' and x < 3

def possible_moves(code, state):
    moves = []
    [path, pos] = state
    [x, y] = pos
    hash = md5_hash_of(code + path)

    if up(hash, pos):    moves.append([path + 'U', [x, y - 1]])
    if down(hash, pos):  moves.append([path + 'D', [x, y + 1]])
    if left(hash, pos):  moves.append([path + 'L', [x - 1, y]])
    if right(hash, pos): moves.append([path + 'R', [x + 1, y]])
    return moves

def new_possible_moves(code, states):
    new_moves = []
    for state in states:
        new_moves.append(possible_moves(code, state))
    return [item for sublist in new_moves for item in sublist]

def vault_accessed(state):
    [path, pos] = state
    if pos == [3, 3]: return path
    return None

def shortest_path(passcode):
    moves = [['', [0, 0]]]
    while not any([vault_accessed(state) for state in moves]):
        moves = new_possible_moves(passcode, moves)
    for state in moves:
        if vault_accessed(state) is not None: return vault_accessed(state)

passcode = 'hijkl'
md5 = md5_hash_of(passcode)
pos = [0, 0]
assert md5.startswith('ced9')
assert not up(md5, pos)
assert not left(md5, pos)
assert not right(md5, pos)
assert down(md5, pos)
assert possible_moves(passcode, ['', [0, 0]]) == [['D', [0, 1]]]
assert new_possible_moves(passcode, [['', [0, 0]]]) == [['D', [0, 1]]]
after_one_step = new_possible_moves(passcode, [['', [0, 0]]])
assert new_possible_moves(passcode, after_one_step) == [['DU', [0, 0]], ['DR', [1, 1]]]

passcode = 'ihgpwlah'
assert shortest_path(passcode) == 'DDRRRD'
passcode = 'kglvqrro'
assert shortest_path(passcode) == 'DDUDRLRRUDRD'
passcode= 'ulqzkmiv'
assert shortest_path(passcode) == 'DRURDRUDDLLDLUURRDULRLDUUDDDRR'

passcode = 'qljzarfv'
print shortest_path(passcode)
