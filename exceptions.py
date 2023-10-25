class JustnotError(Exception):
    pass


x = 2

try:
    raise JustnotError("This isnt cool")
    # raise Exception("IM a custom exception")
    # print(x/1)
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed.")
except NameError:
    print('Nameerror means something is probably undefined.')
except ZeroDivisionError:
    print("You can't divide by zero!")
except Exception as error:
    print(error)
else:
    print('No errors, all good!')
finally:
    print('This will always run no matter what happens above.')
