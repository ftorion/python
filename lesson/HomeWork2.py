"""задача 1"""
arr = [1, 2, 3]
for i in range(0, len(arr)):
    arr[i] *= 2
else:
    print(arr)
    del arr

"""задани 2"""
arr = [1, 2, 3]
rez = 0
for i in range(0, len(arr)):
    rez += arr[i] ** 2
else:
    print(rez)
    del arr, rez

"""задание 3"""
print("ведите время сколько катался (в часах)")
i = int(input())
print(i//2)
del i

"""задание 4 """
strr = "Hello World"
if " " in strr:
    strr = strr.upper()
else:
    strr = strr.lower()
print(strr)
del strr