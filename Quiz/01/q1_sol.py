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
print('The difference between last and first values is:')
diff = values[-1] - values[0]
print('  ',diff)

print('Here are the values represented as horizontal bars:')
# INSERT CODE HERE
# create matrix filled by 0
matrix = []
for i in range(len(values)):
    matrix.append([0 for i in range(max(values))])

# set '1' according to values
for n in range(len(values)):
    for i in range(values[n]):
        matrix[n][i] = 1
    print('    ','* ' * values[n])

print('Here are the values represented as vertical bars, '
      'with a surrounding frame:'
     )
# INSERT CODE HERE
print('  ','-' * (length * 2 + 3))
for i in range(-1, -len(matrix[0]) - 1, -1):
    line = ''
    for j in range(len(matrix)):
        if matrix[j][i] == 1:
            line = line + "* "
        else:
            line = line + "  "

    line = "| " + line + "|"
    print('  ',line)
print('  ','-' * (length * 2 + 3))
