"""функции"""
def hello(line= int(),arr =list()):
    for i in arr:
         print(f"hi {i}")
    else:
        return f"количество переменных в массиве {line}"
i = ["jon", "MAx", "Rich"]
print(hello(len(i), i))

del i

def pri(text= str() , d = False):
    for i in text:
        if " " in i:
            print("пробелы есть ")
    if not " " in text:
        print("пробелов нет")
    if d == True:
        print(id(text))
    print(text)

print(pri("hiii man"))
print(pri("hdhdhdh", True))

def main(a, b):
    return a + b
print()

"""Home Work"""
def odd_map(arr=list()):
    j = arr.index("odd")
    print(j)
    if "odd" in arr and j in arr:
        print("True")
    else:
        print("False")
odd_map(["ho", "ho", 5,"odd",3, " fa"])
odd_map(["ho", "ho", 5,"odd", " fa"])

def find_sup(n=int()):
    rez = 0
    for i in range(1, n+1):
        if i % 3 == 0 or i % 5 == 0:
            rez += i
    return  rez
print(find_sup(10))

def name(arr=list()):
    arr_rez = []
    for i in arr:
        if len(i) == 4:
            arr_rez.append(i)
    return arr_rez
print(name(["hiro", "kirop", "hopuse", "kike" ]))




