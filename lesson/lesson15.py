"""методы списков """
list1 = [1, 2, 3, 4, 5, 6, ["hi", True], "you"]
print(len(list1))
list1[1] == "gigi"
list1[2:4] = [10, 3, 51]
print(list1[1:5]) #срез
list1.append(10) #добовляет элемент в конце спика
list1.extend([5, 7]) # соединяте 2 списка
list1.insert(5, "gif") #вставляет элесент на определённую позицию
list1.remove(1)# Удоляет первый наденый элемент в списке если он его не находит то ошибка
el = list1.pop(1) #удаляет эдемент по индексу  и возврощяет его
list1.index(10) # возврощяет расположени я первого найденого элемента и сожно указать стартовую позицию и конечную тоесть диапозон
co =list1.count(6) #возврощяет количество элементов со значением
#list1.sort() это сортировка
list1.reverse() # переворачивает список
list1.copy() # копирует
list1.clear() # очищяет список
print(el, co )