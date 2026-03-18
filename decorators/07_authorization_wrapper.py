from functools import wraps

def require_admin(func):
    @wraps(func)  #to preserve meta data
    def wrapper(user_role):
        if user_role!="admin":
            print("Access denied : Admins only!")
            return
        
        else:
            return func(user_role)   # execute the access_tea_inventory(): func
    return wrapper


@require_admin
def access_tea_inventory (role):
    print("access granted to tea inventory!")

access_tea_inventory("user")

access_tea_inventory("admin")


