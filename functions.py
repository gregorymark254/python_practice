def hello_world():
    print("Hello, World!")


hello_world()


def sum(num1=0, num2=0):
    if (type(num1) is not int or type(num2) is not int):
        return 0
    return num1+num2


total = sum(7, 2)
print(total)


def mulitple_items(*args):
    print(args)
    print(type(args))


mulitple_items("Dave", "John", "Sara")


def mult_name_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


mult_name_items(first="Dave", last="John")
