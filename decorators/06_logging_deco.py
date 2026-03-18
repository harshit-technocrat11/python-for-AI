from functools import wraps

def logactivity(func):  #1. Decorator function receives another function
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"calling : {func.__name__}")
        result = func(*args, **kwargs)
        print(f"✅finished: {func.__name__}")
        return result
    
    return wrapper


@logactivity
def brew_chai(type,milk="no"):
    print(f"Brewing {type} chai , milk: {milk}")    
brew_chai("Masala!","yes")

@logactivity
def brew_coffee(type):
    print(f"brewing {type} coffee")
brew_coffee("black")

# logactivity → setup
# wrapper → actual execution
