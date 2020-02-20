# Written by *** and Eric Martin for COMP9021
#
# Generates a random list of integers between 1 and 6
# whose length is chosen by the user, displays the list,
# outputs the difference between last and first values,
# then displays the values as horizontal bars of stars,
# then displays the values as vertical bars of stars
# surrounded by a frame.


from random import seed, randrange
import sys

from itertools import zip_longest

try:
    for_seed, length = (int(x) for x in input('Enter two integers, the second '
                                              'one being strictly positive: '
                                              ).split()
                        )
    if length <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
values = [randrange(1, 7) for _ in range(length)]
print('Here are the generated values:', values)
# INSERT CODE HERE

# print difference
print(f"\nThe difference between last and first values is:\n   {values[-1] - values[0]}\n")

print('Here are the values represented as horizontal bars:')
# INSERT CODE HERE

#
print()
print("\n".join(["     " + "  ".join(["*" for _ in range(item)]) + ' ' for item in values]))
print()

print('Here are the values represented as vertical bars, '
      'with a surrounding frame:'
      )
# INSERT CODE HERE
print()
print('  ', '-' * (length * 3 + 2))
lines = [["*" for _ in range(item)] for item in values]
for line in reversed(["  ".join(item) for item in zip_longest(*lines, fillvalue=" ")]):
    print("   | " + line + " |")
print('  ', '-' * (length * 3 + 2))
print()
