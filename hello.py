""" Simple Example """


def add(x, y):
    """Return sum of x and y"""
    return x + y

# def create function that subtracts two integers

def subtract(x, y):
    """Return difference of x and y"""
    return x - y

RESULT = add(1, 2)
print("This is the sum: 1, 2, %s" % RESULT)

RESULT = subtract(10,2)
print("This is the difference: 10, 2, %s" % RESULT)
