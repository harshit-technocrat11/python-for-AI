# Decorator =  wrap extra behaviour around a function without changing its code 

# take a func() -> wrap it with extra behaviour -> return a new function  

def my_decorator(func):
    def wrapper():
        print("1 before func runs")
        func()
        print("3 after func runs")    
    
    return wrapper

@my_decorator
def greet():
    print("2 Hello from decorator class from chaicode")

greet()
print(greet.__name__)

# basic example
def add( a, b):
    return a+b

# def wrapper(func):  #takes func as an argument ( like a value )
#     print("before")
#     result = func(2,3)
#     print("after")
#     return result

# wrapper(add)

# ex-2

def wrapper(func):
    def inner():
    
        print("before")
        func()
        print("after")
    return inner;

def say_hi():
    print("hi")


newfunc = wrapper(say_hi)
newfunc()

# You took a function → wrapped it → returned a new function

# now using it wrapper as a decorator

@wrapper
def say_hi():
    print("hi there!!")
say_hi()