#ValueError
def enterNum():
    #print(int("abc"))# ValueError: invalid literal for int() with base 10: 'abc'
#typeerror
    print("hello" + 5) # TypeError: can only concatenate str (not "int") to str
#indexError
    my_list = [1, 2, 3]
    print(my_list[5])  # IndexError: list index out of range
enterNum()
