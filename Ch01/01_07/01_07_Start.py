# Least to Greatest
point_in_a_game = [0, -10, 15, -2, 1, 12]
sorted_game = sorted(point_in_a_game)
print(sorted_game)

# Alphabetically
children = ['sue', 'jerry', 'linda']
print(sorted(children))
print(sorted(['Sue', 'jerry', 'linda']))

# Key Parameters
print(sorted('My favorite child is linda'.split(), key=str.upper))
print(sorted(point_in_a_game, reverse = True))

leader_board = {231: 'CKL', 123: 'ABC', 432: 'JKC'}
print(sorted(leader_board, reverse= True))
print(leader_board.get(432))

students = [('alice', 'B', 13), ('eliza', 'A', 16), ('tae', 'C', 15)]
print(sorted(students, key=lambda student:student[0]))
print(sorted(students, key=lambda student:student[1]))
print(sorted(students, key=lambda student:student[2]))