# 로또 생성 프로그램

import random

cnt = int(input("로또를 몇 세트 자동생성 할까요? "))

for i in range(1, cnt+1) :
    numbers = []
    while len(numbers) < 6 :
        rotto = random.randint(1, 45)
        if rotto not in numbers :
            numbers.append(rotto)
    
    numbers.sort()
    
    print(f"{i}번째 세트", end=" ")        
    for z in numbers :
        print(f"%2d" % z, end=" ")
    print()
