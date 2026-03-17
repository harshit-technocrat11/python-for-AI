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