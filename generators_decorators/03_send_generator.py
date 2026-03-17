# send to generators

def chai_customer():
    print("welcome! what chai would you like ?")
    order = yield
    
    while True:
        print(f"preparing : {order}")
        order = yield  


# stall =  chai_customer()
# next(stall) #start the generator

# next(chai_customer)
# chai_customer.send("Masala chai")

# if chai_customer() not stored inside, stall variable then 
# error 
#   
#     next(chai_customer)
#     ~~~~^^^^^^^^^^^^^^^
# TypeError: 'function' object is not an iterator


# -----create an instance of the func()

stall = chai_customer()

next(stall)

stall.send("cold coffee")
stall.send("masala chai")