import random

again = True

while again:
    print(random.randint(1,6))
    next_turn = input("Want to trun again. (y/n): ")
    if next_turn.lower() == 'y':
        continue
    else:
        break