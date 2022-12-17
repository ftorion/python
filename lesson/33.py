f = open("test.txt", mode="a", encoding="utf-8") #открытие файла
f.write("новая строка\n")
lin = ["Новая строка 1", "Новая строка 2"]
for i in lin:
    f.write(i + "\n")
f.writelines(f"{i}\n"for i in lin)
f.close() # закрфтия файла
f = open("test.txt", mode="r", encoding='utf-8')
for line in f:
    print(line, end="\n")
f.close()