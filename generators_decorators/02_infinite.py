# infinite generator

# used for streams / real time systems 

def infinite_chai():
    count = 1

    while True:
        yield f"refill #{count}"
        count+=1

refill = infinite_chai()
user2 =  infinite_chai()

# _ underscore is a valid variable

for _ in range(6):
    print(next(refill))

for _ in range(8):
    print(next( user2))