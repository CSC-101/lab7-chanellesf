import sys
from types import NoneType

import convert

# Converts each command-line argument in sys.argv into a float
total = 0.0

for i in range(1, len(sys.argv)):
    if (type(convert.str_to_float(sys.argv[i])) != NoneType):
        total = total + convert.str_to_float(sys.argv[i])


if __name__ == '__main__':
    print(sys.argv)
    print("The sum is: ", total)
