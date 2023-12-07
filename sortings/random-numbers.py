import random

# Generate and print 20 random integers
random_numbers_20 = [random.randint(1, 20) for _ in range(20)]
print(" ".join(map(str, random_numbers_20)))
