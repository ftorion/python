def hello():
    return "hello"

def super_hi(func):
    print("hello12")
    print(func())

print(hello())
print((super_hi(hello)))

def helo():
    return "hello hi "

test = helo
print(test())

def dec(func):
    def func_v():
        print("code before")
        func()
        print("code")
    return func_v
@dec
def f():
    print("hello 1010")
print(f())


def make(fn):
    def wrapped():
        title = fn()
        title = title.capitalize()
        title = title.replace(",", "")
        return title
    return wrapped
@make
def gi():
    return "Hello, world"
print(gi())