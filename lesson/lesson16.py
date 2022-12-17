"""ИЗМЕНЯЙМЫЕ И НЕ ИЗМЕНЯЙМЫЕ ОБЕКТЫ """
x = 10
print(x, id(x))
x = 20
print(x, id(x))

y ="hi"
print(y, id(y))
y += " you"
print(y, id(y))

li = [1, 2, 3, 4]
print(li, id(li))
li.append(5)
print(li, id(li))
i = 10
j = i
print(i, id(i))
print(j, id(j))
i = 13
print(i, id(i))
print(j, id(j))

l1 = [1, 2, 3]
l2 = l1.copy()
print(l1, id(l1))
print(l2, id(l2))
l1.append((3))
print(l1, id(l1))
print(l2, id(l2))


x = 40
print(x)
del x
