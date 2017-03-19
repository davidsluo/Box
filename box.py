#!/usr/bin/env python
import sys
from pprint import pprint

if len(sys.argv) < 2:
    print('Usage: ' + sys.argv[0] + ' <word>')
    exit(1)

word = ' '.join(sys.argv[1:])
if len(word) % 2 != 1 or len(word) < 5:
    print('Word must have an odd number of characters and be at least 5 characters long.')
    exit(1)

front_face = [[] for i in word]
for i in range(len(word)):
    if i == 0:
        front_face[i] = list(word)
    elif i == len(word) - 1:
        front_face[i] = list(word[::-1])
    else:
        front_face[i] = list(word[i] + (' ' * (len(word) - 2)) + word[-i-1])

back_face = [i[::-1] for i in front_face]

size = int(len(word) * 1.5)

# Resize both for superimposing
for i in range(int(len(word) / 2)):
    front_face.insert(0, list(' ' * len(word)))
    back_face.append(list(' ' * len(word)))

for line in front_face:
    line.extend(list(' ' * int(len(word) / 2)))
for line in back_face:
    for i in range(int(len(word) / 2)):
        line.insert(0, ' ')

superimposed = [['' for x in range(size)] for y in range(size)]

for i in range(size):
    for j in range(size):
        front = front_face[i][j]
        back = back_face[i][j]

        superimposed[i][j] = \
                (front if front is not ' ' else None) or \
                (back if back is not ' ' else None) or ' '

for i,j,k,l in zip(
        range(1, int(size / 3)), # 1, 2, 3
        range(int(size / 3) - 1, 0, -1), # 3, 2, 1
        range(int(size * 2 / 3) + 1, size - 1), # 9, 10, 11
        range(size - 2, int(size * 2 / 3), -1) # 11, 10, 9
        ):
    superimposed[i][j] = '/'
    superimposed[i][l] = '/'
    superimposed[k][j] = '/'
    superimposed[k][l] = '/'

for i in superimposed:
    print(' '.join(i))
