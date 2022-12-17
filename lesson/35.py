print("hekko")
m = int(input())
try:
    n = 100 / m
    print(n)
except ZeroDivisionError:
    n = 0
else:
    print("gOD")
finally:
    print("fim")
print(n)

while True:
    try:
        num = int(input("введите число"))
        num = 100 / num
    except ZeroDivisionError:
        print("не 0")
    except ValueError:
        print("не ")
    print("гуд")
    break