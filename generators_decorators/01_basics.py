# generator - function

def serve_chai():
    yield "Cup 1: Masala chai"
    yield "Cup 2: Ginger chai"
    yield "Cup 3: Elaichi chai"
    yield "Cup 4: Lemon chai"

# we have used - -yield

stall = serve_chai()

for cup in stall:
    print(cup)

def get_chai_list():
    return [ "cup 1","cup 2","cup 3" ]

# generator func

def get_chai_gen():
    yield "cup 1"
    yield "cup 2"
    yield "cup 3"

chai = get_chai_gen();
print(chai)  # refernece stored <generator object get_chai_gen at 0x000001E732D15B10>

# to actually print the values we need Loop / next 
print(next(chai))  #cup 1
print(next(chai))  #cup 2

# next() - pointer moves
print(chai)