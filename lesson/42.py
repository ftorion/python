"""LAMBDA"""
def get_sum(sum):
    return sum **2

print(get_sum(2))

hi = lambda num: num **2
print(hi(5))

print((lambda num: num ** 2)(7))

l = [1, 2, 3, 4]
def get_doble(l):
    return list(map(lambda num: num * 2, l))

print(get_doble(l))