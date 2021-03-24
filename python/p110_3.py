"""
삼각형의 두 변의 길이를 받아
나머지 변의 최대 길이를 구하는 프로그
"""

first_length = int(input("삼각형의 첫 번째 변의 길이: "))
second_length = int(input("삼각형의 두 번째 변의 길이: "))
max_length = (first_length + second_length) - 1

print(f"삼각형의 나머지 변의 최대 길이 = {max_length}")