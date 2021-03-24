# -*- coding: utf-8 -*-
"""
4자리 정수를 입력받아 자리수의 합을 구하는 프로그램
ex) 1234 = 1 + 2 + 3 + 4 = 10
"""

number = int(input("정수="))

v1000 = number // 1000
r1000 = number % 1000

v100 = r1000 // 100
r100 = r1000 % 100

v10 = r100 // 10
r10 = r100 % 10

result = v1000 + v100 + v10 + r10

# first = number // 1000
# second = (number % 1000) // 100
# thrid = (number % 100) // 10
# fourth = number % 10

# result = first + second + thrid + fourth

print(f"당신이 입력한 수는 {number}입니다.\n각 자리수로 나누어 천의 자리는 {v1000}이고, 백의 자리는 {v100}, 십의 자리는 {v10}, 일의 자리는 {r10}입니다.\n따라서 각 자리수의 합은 {result}입니다.")
