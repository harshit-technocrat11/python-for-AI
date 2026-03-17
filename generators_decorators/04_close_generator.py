def local_chai():
    yield "masala chai"
    yield "ginger chai"

def imported_chai():
    yield "matcha"
    yield "Oolong"

def full_menu():
    yield from local_chai()
    yield from imported_chai()

# for chai in full_menu():
#     print(chai)

def chai_stall():
    try:
        while True:
            order = yield "waiting for chai order"
    except:
        print("stall ( tea generator closed ) closed , No more chai!")


stall = chai_stall()
print(next(stall))

# clean up  of memory!!, need to close
stall.close()


def my_gen():
    try:
        yield 1
        yield 2
    
    except GeneratorExit:
        print("generator closedd")

g= my_gen()
print(next(g))
g.close()
# print(next(g))  already closed!!




# concepts
# yield
# next(gen)
# yield from another_gen

# close() - cleanup


# ⚡ Why close() matters

# Useful when:

# stopping infinite generators

# cleaning resources

# breaking streaming loops