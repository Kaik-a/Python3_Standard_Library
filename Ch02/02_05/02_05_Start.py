# Itertools
import itertools

# Infinite Counting
for x in itertools.count(50, 5):
    print(x)
    if x == 80:
        break

x = 0
# Infinite Cycling
for c in itertools.cycle('RACECAR'):
    print(c)
    x += 1
    if x == 50:
        break

# Infinite Repeating
for r in itertools.repeat(True):
    print(r)
    x += 1
    if x == 100:
        break