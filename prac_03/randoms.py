import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# The smallest is 5 and the largest is 19.

# What did you see on line 2?
# The smallest is 3 and the largest is 9. It will not produce 4,
# because the range is 2.

# What did you see on line 3?
# The smallest is 2.5 and the largest is 5.5

print(random.randint(1, 100))
