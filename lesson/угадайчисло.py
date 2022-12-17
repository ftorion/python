import random

num = random.randint(1, 100)
pop = 1
print('угодай число')
while True:
    print(f"попытка {pop}")
    rez = int(input())
    pop += 1
    if rez == num:
        print(f"поздровляю вы угодали число {num}, количество попыток {pop}")
        break
    elif rez < num:
        print("больше")
    else:
        print('меньше')
input()