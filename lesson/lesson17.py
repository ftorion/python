"""кортеж - тот же список но не изменяймый """
"""+ если нужно получить защещённый список """
"""способы создания """
t1  = (1, 2, 3)
t2 = 1, 2, 3
t1 = tuple((1, 2, 3,))
t1 = ()
t1 = (1,)
t1 = tuple("hello")
t4 =list("hello")
print(t1.__sizeof__())
print(t4.__sizeof__())
print(t1, t2, type(t1))
print(t1[2])
del  t1, t2, t4
"""операции над кортежами """
t1 = tuple("hello")
t2 = tuple(" world")
t3 = t1 + t2
print(t3, type(t3), len(t3),t3.count("l"), t3.index("w"), t3.__sizeof__())
if "l" in t3:
    print(t3.index("l"))
else:
    pass

for i in t3:
    if i == " ":
        continue
    print(i, end=" ")
else:
    print(len(t3), t3.__sizeof__(), id(t3))
del  t1, t2, t3

t1 = ([1, 2, 3], [4, 0, 3], ["hello", "world"])
print(t1, t1.__sizeof__(), id(t1))
t1[2][0] = "hi"
print(t1, t1.__sizeof__(), id(t1))
t1[2].append("wori")
print(t1, t1.__sizeof__(), id(t1))
del t1
"""распаковка кортежа"""
t1 = (1, 2, 3)
x, y, z = t1
print(x, y, z)

"""home work"""
words = ["мадам", "топот", "test", "madam", "word"]
rez = []
for i in words:
    wol = list(i)
    wol.reverse()
    wol2 = list(i)
    if wol == wol2:
        rez.append(i)
    else:
        pass
else:
    print(rez)
del rez, x, y, z, t1

my_str = ["Око за око", "А роза упала на лапу азора", "Около Миши молоко"]
p = []
for word in my_str:
    w = word.replace(" ", "").lower()
    if w == w[::-1]:
        p.append(word)

print(p)
'''дополнительно '''
dots = list(range(1, 9))
dots2 = list("hello")
print(dots)
s = "-".join(map(str, dots))
s2 = "-".join(dots2)
print(s2)
print(s)
