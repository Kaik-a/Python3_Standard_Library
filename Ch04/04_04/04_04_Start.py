# Create a Timer with the Time module
import time

run = input('start ? >')

seconds = 0

if run == 'yes':
    while seconds != 10:
        print('>', seconds)
        time.sleep(1)
        seconds += 1
    print('>', seconds)