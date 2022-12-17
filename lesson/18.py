"""множестов"""
s = {"appple", "orange", "apple", "pear", "banana"}
s2 = set("hello")
s3 = {i for i in range(1, 11)}
s4 = {8, 3, 21, 3}
print(type(s), s.__sizeof__())
print(s, s2, s3, s4)
nums = [1, 2, 3, 3, 3, 4, 5, 6, 1, 2]
nums2 = list(set(nums))
print(nums2)
a = set("abracadabra")
b = set("alacazam")

print(a, b, sep="\n")
c = a-b #вычитания
c1 = a | b #обединения
c2 = a & b #пересечения
c3 = a ^ b # буквы попадут только если они не содержутся в обоих множествах
print(c, c1, c2, c3, sep="\n")

"""методы"""
"""
set.copy() возврощяет копию множества
set.add() добовляет элемент в множество 
set.remove() удоляет первый найденный элемент с ошибкой 
set.discard() удоляет элемент без ошибки
set.pop() возврощяет и удоляет первый элемент множества 
set.clear() - очистка множества 
"""
g = frozenset("hi") #нельзя добавить во множество и изменить
