"""списки/ масивы """
list1 = [1, 2, 3, "hello", ["hi", 10], "wori", True]
list2 = list("hello") # передоётся только последовательность
list3 = [i*2 for i in "hello world" if i not in [" ", "h"]] #запомнить а то гг
print(type(list1))
print(list1, list2, list3,  sep = "\n")