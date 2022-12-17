#bool
'''этот тим данных имееет 2 значения (True, Float ) они логические '''
test = True
ru  = False
print(type(test))
print(type(ru))
#str() int() float() -преводят значения  к типу данных
x = 5.3
print(x, type(x))
x = int(x) # преводим число к типу данных  int  округляет до 5
print(x, type(x))
y = 1
print(y, type(y))
y = bool(y) # оно переводит так что меньше или рано нулю то false что больше или рано единице то True
print(y, type(y))
