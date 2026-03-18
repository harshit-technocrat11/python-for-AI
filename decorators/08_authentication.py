def require_auth(func):
    
    def wrapper(user, *args, **kwargs):
        if not user.get("is_authenticated"):
            print(f"access denied!! to {user['name']}")
            return
        else:
            print("access granted !!")
            return func(user, *args, **kwargs)
        
    return wrapper

@require_auth
def view_dashboard(user):
    # execute , this func, only after passing auth
    print(f"welcome !,  {user['name']} to dashboard!")

user1 = {"name":"harshit", "is_authenticated":True}
user2 = {"name":"aryan", "is_authenticated":False}

view_dashboard(user=user1)
view_dashboard(user=user2)