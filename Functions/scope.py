#built-in scope

#global scope
p=2
print(p)

#local scope
def find():
    x=4
    print(x)
find()

#enclosing scope
def find():
    x=4
    print(x)
    def inner():
        print(x)

    inner()
find()
x=9
def find():
    x=4
    
    def inner():
        nonlocal x
        x=3
        print(f"inner{x}")
    inner()
    print(f"outer{x}")
    
find()
print(f"global{x}")