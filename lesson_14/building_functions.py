def add_2_nums(a, b):
    return a + b


# multiple arguments passed as tuple

def add_all(*args):
    total = 0
    for num in args:
        total += num
    return total


def add_nums(a, b, c):
    return a + b + c

add_nums(*(1, 2, 3)) # passing a tuple as a series of argument to a function


def double(num):
    return num * num


# default parameters

def double_by(num, by=10):
    return num * by


def name(first, last):
    print '%s %s', (first, last)


# passing dictionary as arguments

def shopping_list(**items):
    print items

shopping_list(lipstick=40, shoes=20, hair=45, wristwatch=90)


