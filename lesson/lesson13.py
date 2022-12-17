"""циклы"""
"""for - цикл со счётчиком"""
"""while цикл выполняется  пока условие верно"""
sts = 5
while sts:
    print(sts, end ="|")
    sts -= 1
s = " hello world"
for i in s:
    if i == " ":
        continue
    print(F"'{i}'", end = " ")

print() # сделанно что бы разделить
for i in "HoHOHO HO":
    if i == " ":
        break # выход из цикла
    print(i, end= " ")
else:
    print("100%") # отробатывает в конце ЗАВЕРШЕНИЯ цикла





#Home Work
year = 1900
while year <= 2022:
    print(year)
    year += 1