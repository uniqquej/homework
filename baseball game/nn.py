import random

numbers = set()

while len(numbers) < 5:
    numbers.add(random.randint(0,9))
print(numbers)

num_list = list(numbers)
print(num_list)
random.shuffle(num_list)
print(num_list)
