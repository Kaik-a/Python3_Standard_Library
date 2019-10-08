# Calculating Length

# len() --> returns length
first_name = 'Taylor'
print(len(first_name))
last_name = 'Swift'
print(len(last_name))
last_name.__len__()

ages = [1, 11, 43, 12, 10]
print(len(ages))
i = 0
for i in range(0, len(ages)):
    print(ages[i])

print(len(['Bob', 'Mary', 'sam']))

candy_collection = {'bob': 10, 'mary': 7, 'sam': 18}

print(len(candy_collection))