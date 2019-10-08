# Command Line Arguments
import sys

# Print Arguments
print('Number of arguments: ', len(sys.argv), ' arguments.')
print('Arguments:', sys.argv)

# Remove Arguments
sys.argv.remove(sys.argv[0])

# Sum up the Arguments
arguments = sys.argv
sum = 0
for arg in arguments:
    try:
        number = int(arg)
        sum += number
    except:
        print('bad input')
print(sum)