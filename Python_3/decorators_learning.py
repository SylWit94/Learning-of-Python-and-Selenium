# How the wrapper works

import datetime


def simple_current_time_wrapper(function):
    def wrapper():
        print(datetime.datetime.now())
        function()

    return wrapper


def print_hello_how_to_test():
    print('Hello! How to test?')


wrapper_print_hello_how_to_test = simple_current_time_wrapper(print_hello_how_to_test)
wrapper_print_hello_how_to_test()


# How the wrapper works - my example

def simple_wrapper(function):
    def inner_function():
        print('Value of inner function')
        function()

    return inner_function


def another_function():
    print('Value of another function')


wrapper_another_function = simple_wrapper(another_function)
wrapper_another_function()


# How the @ wrapper works

import datetime


def simple_current_time_wrapper(function):
    def wrapper():
        print('\n')
        print(datetime.datetime.now())
        function()

    return wrapper


@simple_current_time_wrapper
def hello_how_to_test():
    print('Hello! How to test?')


@simple_current_time_wrapper
def bye_bye():
    print('Bye bye!')


@simple_current_time_wrapper
def hello_decorators():
    print('Hello decorators!')


hello_how_to_test()
bye_bye()
hello_decorators()


# Exercise with decorator

import datetime


def decorator_with_date(function):
    def inner_function():
        print(datetime.datetime.now())
        function()
        print(datetime.datetime.now())

    return inner_function


def print_greetings():
    workers = ['Eve', 'Bob', 'Jess', 'Pat', 'Andrea', 'Gary']
    for worker in workers:
        print(f'Hello {worker}!')


variable_print_greetings = decorator_with_date(print_greetings)
variable_print_greetings()


# Exercise with @ decorator

import datetime


def decorator_with_date(function):
    def inner_function():
        print(datetime.datetime.now())
        function()
        print(datetime.datetime.now())

    return inner_function


@decorator_with_date
def print_greetings():
    workers = ['Eve', 'Bob', 'Jess', 'Pat', 'Andrea', 'Gary']
    for worker in workers:
        print(f'Hello {worker}!')


print_greetings()


# Decorator with parameter

import datetime


def simple_current_time_wrapper(function):
    def wrapper(name):
        print(datetime.datetime.now())
        function(name)

    return wrapper


@simple_current_time_wrapper
def print_greetings(name):
    print(f'Hello {name}!')


print_greetings('Jack')

# more code...

print_greetings('Tom')


# Decorator @ with parameter

import datetime


def simple_current_time_wrapper(function):
    def wrapper(name):
        print(datetime.datetime.now())
        function(name)

    return wrapper


def print_greetings(name):
    print(f'Hello {name}!')


wrapper_print_greetings = simple_current_time_wrapper(print_greetings)
wrapper_print_greetings('Bob')

# more code...

wrapper_print_greetings = simple_current_time_wrapper(print_greetings)
wrapper_print_greetings('Tom')


# Exercise with @ decorator and parameters

def simple_wrapper(function):
    def wrapper(value_1, value_2):
        print(f'value_1: {value_1}, value_2: {value_2}')
        function(value_1, value_2)

    return wrapper


@simple_wrapper
def print_sum(value_1, value_2):
    print(value_1 + value_2)


print_sum(2, 5)


# Exercise with decorator and parameters

def simple_wrapper(function):
    def wrapper(value_1, value_2):
        print(f'value_1: {value_1}, value_2: {value_2}')
        function(value_1, value_2)

    return wrapper


def print_sum(value_1, value_2):
    print(value_1 + value_2)


wrapper_print_sum = simple_wrapper(print_sum)
wrapper_print_sum(value_1=2, value_2=5)


# Decorators that return a result

import datetime


def simple_current_time_wrapper(function):
    def wrapper(name):
        print(datetime.datetime.now())
        return function(name)

    return wrapper


@simple_current_time_wrapper
def print_greetings(name):
    return f'Hello {name}!'


print(print_greetings('Jack'))

# more code...

print(print_greetings('Tom'))


# Decorators that return a result - exercise

def simple_wrapper(function):
    def wrapper(value_1, value_2):
        print(f'value_1: {value_1}, value_2: {value_2}')
        return function(value_1, value_2)

    return wrapper


@simple_wrapper
def get_sum(value_1, value_2):
    return value_1 + value_2


result = get_sum(2, 5)
print(f'Sum: {result}')

# Construction *args (any number of parameters)

import datetime


def simple_current_time_wrapper(function):
    def wrapper(*args):
        print(datetime.datetime.now())
        function(*args)

    return wrapper


@simple_current_time_wrapper
def print_sum(value_1, value_2):
    print(f'Sum of {value_1} and {value_2} is {value_1 + value_2}')


print_sum(2, 3)


# Wrapper with date

import datetime
import time


def current_date_wrapper(function):
    def wrapper(value_1, value_2):
        print(f'Start: {datetime.datetime.now()}')
        result = function(value_1, value_2)
        print(f'End: {datetime.datetime.now()}')
        return result

    return wrapper


@current_date_wrapper
def get_sum(value_1, value_2):
    time.sleep(2)
    return value_1 + value_2


@current_date_wrapper
def get_multiplication(value_1, value_2):
    time.sleep(2)
    return value_1 * value_2


value_1 = 2
value_2 = 3

print(f'Sum of {value_1} and {value_2} =')
print(get_sum(value_1, value_2))

print(f'Multiplication of {value_1} and {value_2} =')
print(get_multiplication(value_1, value_2))