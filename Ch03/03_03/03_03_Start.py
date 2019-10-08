# Files and File Writing

# Open a file
my_file = open('scores.txt', 'w')

# w --> write
# r --> read
# r+ --> read and write
# a --> append
# Show attributes and properties of that file
print('Name ' + my_file.name)
print('Mode ' + my_file.mode)

# Write to a file
my_file.write('GBJ : 100\nKHD : 99\nBBB: 89')
my_file.close()

# Read the file
my_file2 = open('scores.txt', 'r')
print(my_file2.read(10))
print(my_file2.read(10))