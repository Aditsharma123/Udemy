name_string = input("Give me everybody's names, separated by a comma and space: ")
names = name_string.split()

import random

print(random.choice(names))
