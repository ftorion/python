"""оператор if ветления"""
"""оператор работает с BOOL(True, False)"""
"""операторы сравнения 
== равно 
!= не равно 
<> равны ли оба операторва 
> больше < меньше 
>= больше или равно <= меньше или равно 
тождейственных равенств нет 
"""
#пример логических вырожений
print(3 > 4)
# выведет False

#if если
#elif  если не  if то elif
#else если не if  и не elif (выполняет если не одно условия не истино )
x = int(input()) # ввод числа с клавиотуры
if x == 0:
    print(x == 0)
elif x > -1:
    print(f"{x} больше -1")
else:
    print(x)

#пример 2
light = str(input("red, yellow, green "))
light1 = light.lower() #переводим все символы в нижний регистр
if light1 == "red":
    print("stop")
elif light1 == "yellow":
    print("wait")
elif light1 == "green":
    print("go")
else:
    print("what?")

#пример 3
age = int(input("сколько вам лет"))
if age >= 16:
    print("добро пожаловать")
else:
    print(f"вам {age}, вам не хватает {16-age}")

"""логические операторы
and  и 
or или 
not не (пример) 
x = True 
print(not(x)) False 
"""

time = 11
if time < 12 or time > 13:
    print("open")
else:
    print("close")

day = "st"
if (time < 12 or time > 13) and  day != "su":
    print("open")
else:
    print(close)


y = 1
if not y:
    print("ok")
else:
    print("no")
"""тернарный оператор некое подобие наэто """
res = "ok" if y else "no"
print(res)
