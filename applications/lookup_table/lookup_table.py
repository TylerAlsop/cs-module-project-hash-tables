# Your code here
### Need to import "math" and "random" python libriaries
import math, random

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    # U.
        # Given two inputs: x and y
        # Need to produce the same output as slowfun_too_slow()
        # slowfun_too_slow() takes the inputs and uses them for math.pow(x, y), saving them to a variable "v"
            # It then takes that variable and alters it using a new math function.
            # It repeats this two more times
            # It returns that variable "v"
    # P.
        # Create a lookup_table
    lookup_table = { math.pow(x, y) }

        # Push the result of the first math function into the lookup_table

        # Access that item and perform the next math function on it and resaves it.
        # Repeat until all math functions are done.
    for i in lookup_table:
        math.factorial(i)
        i //= (x + y)
        i %= 982451653
        # Return the lookup table.
        return i



# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
