# Random Module
import random

# Random Numbers
print(random.random())
decider = random.randrange(2)
if decider == 0:
    print('HEADS')
else:
    print('TAILS')

print(random.randrange(1, 7))  # Dice roll

# Random Choices
lottery_winngers = random.sample(range(100), 5)
print(lottery_winngers)

possible_pets = ['dog', 'cat', 'fish']
print(random.choice(possible_pets))

cards = ['Jack', 'Queen', 'King', 'Ace']
random.shuffle(cards)
print(cards)