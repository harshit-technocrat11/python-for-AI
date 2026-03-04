def chai_customer():
    print("welcome! what chai would you like ?")
    order = yield
    while True:

        print(f"preparing : {order}")
        order = yield

stall =  chai_customer()
next(stall)

stall.send