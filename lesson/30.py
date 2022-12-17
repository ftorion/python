"""модули"""
import os
import config
#import random as r #назначений псевдонима
from random import randint as r #частичное импортирование
from random import shuffle
#from random inport * ипорт всех методов

print(config.rand(10, 20))
print(__name__)
print(os.getcwd())# получить текущую рабочую деректорию
print(r(1, 100))
l = [i for i in range(1, 10)]
shuffle(l)
print(l)
f = config.rand(10, 20)
print(f)
