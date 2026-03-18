# what is *args , **kwargs

# | Syntax     | Meaning                          |
# | ---------- | -------------------------------- |
# | `*args`    | all positional arguments (tuple) |
# | `**kwargs` | all named arguments (dict)       |


# so the wrapper func() can accept any arguement!! without issues

def test( *args, **kwargs):
    print(args)
    print(kwargs)

test(1,2,3,4, name="harshit", age=20)


# IMP
# 1. You give your function to decorator
# 2. Decorator creates a new function (wrapper)
# 3. Wrapper adds extra behavior
# 4. Original function is replaced by wrapper