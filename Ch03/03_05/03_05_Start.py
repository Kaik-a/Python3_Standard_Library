# Iterative Files
myFile = open("scores.txt", "r")

# Read one line at a time
print(myFile.readline())
print(myFile.readline())

# Iterate through each line of a file
for line in myFile:
    new_high_scorer = line.replace('BBB', 'PDJ')

myFile.close()