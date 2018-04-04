import time

import numpy as np


def core_move(a, b):
    return tuple(np.asarray(a)[np.asarray(b)])


solved = tuple(range(21))
moves = [
    (2, 0, 3, 1, 6, 7, 8, 9, 10, 11, 4, 5, 12, 13, 14, 15, 16, 17, 18, 19, 20),
    (0, 1, 17, 11, 12, 4, 2, 7, 8, 9, 10, 18, 13, 5, 3, 15, 16, 19, 14, 6, 20),
    (0, 5, 2, 13, 4, 19, 14, 6, 3, 9, 10, 11, 12, 20, 15, 7, 1, 17, 18, 16, 8),
    (1, 3, 0, 2, 10, 11, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19, 20),
    (0, 1, 6, 14, 5, 13, 19, 7, 8, 9, 10, 3, 4, 12, 18, 15, 16, 2, 11, 17, 20),
    (0, 16, 2, 8, 4, 1, 7, 15, 20, 9, 10, 11, 12, 3, 6, 14, 19, 17, 18, 5, 13),
]

inv = {a: b for a in moves for b in moves if core_move(a, b) == solved}

start = time.clock()
distance = {solved: 0}
for i in range(15):
    todo = [k for k, v in distance.items() if v == i]
    print('%d pocket cubes with a solution of %d moves' % (len(todo), i))
    for cube in todo:
        for move in moves:
            moved = core_move(cube, move)
            distance.setdefault(moved, i + 1)

print('it took %.2f seconds to finish' % (time.clock() - start))
