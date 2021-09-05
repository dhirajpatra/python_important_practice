"""
Decorators allow you to make simple modifications to callable objects like
functions, methods, or classes.
"""
def multiply(multiplier):
    def multiply_generator(old_function):
        def new_function(*args, **kwds):
            return multiplier * old_function(*args, **kwds)

        return new_function

    # it returns the new generator
    return multiply_generator


# Usage: multiply is not a generator, but multiply(3) is
@multiply(3)
def return_num(num):
    return num


# Now return_num is decorated and reassigned into itself should return 15
return_num(5)


def temperature(t):
    def celsius2fahrenheit(x):
        return 9 * x / 5 + 32

    result = "It's " + str(celsius2fahrenheit(t)) + " degrees!"
    return result


print(temperature(20))


# repeat one function twice
def repeater(old_func):
    def new_func(*args, **kwargs):
        print('first')
        old_func(*args, **kwargs)
        print('second')
        old_func(*args, **kwargs)

    # we have to return the new_function,
    # or it wouldn't reassign it to the value
    print('return')
    return new_func


@repeater
def multy(num1, num2):
    print(num1 * num2)


multy(4, 2)


def polynomial_creator(a, b, c):
    def polynomial(x):
        return a * x ** 2 + b * x + c

    return polynomial


p1 = polynomial_creator(2, 3, -1)
p2 = polynomial_creator(-1, 2, 1)

for x in range(-2, 2, 1):
    print(x, p1(x), p2(x))


def my_decorator(func):
    def wrapper():
        print("something is happeing before calling the function")
        func()
        print("something is happeing after calling the function")
    return wrapper


@my_decorator
def good_test():
    print("very good")


good_test()

# decorator function to convert to lowercase
def lowercase_decorator(function):
    def wrapper():
        # it getst what calling function returned
        func = function()
        string_lowercase = func.lower()
        return string_lowercase
    return wrapper

# decorator function to split words
def splitter_decorator(function):
   def wrapper():
       func = function()
       string_split = func.split()
       return string_split
   return wrapper

@splitter_decorator # this is executed next
@lowercase_decorator # this is executed first
def hello():
   return 'Hello World'

print(hello())   # output => [ 'hello' , 'world' ]
