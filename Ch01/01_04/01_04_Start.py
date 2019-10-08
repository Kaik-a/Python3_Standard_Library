# Range -> range instance that holds all nums counting by one between 0 and first input
# List -> lists numbers from the inputted tuple
numbered_contestants = range(30)
print(list(numbered_contestants))

for c in list(numbered_contestants):
    print("Contestans " + str(c) + " is here")

lucky_winners = range(7, 30, 5)
print(list(lucky_winners))