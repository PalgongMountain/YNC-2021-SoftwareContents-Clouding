"""
원의 반지름을 입력하여 원의 넓이를 계산하는 프로그램
(단, 사용자가 음수를 입력하면 잘못된 값임을 알려준다.)

학번 : 2105080
이름 : 임지홍
"""
import math,sys

x = eval(input("원의 반지름을 입력하세요 : "))

pi = 3.14

if type(x) == type(0.1):
    sys.exit("실수는 입력할 수 없습니다.")
    
if x < 0 :
    print("잘못된 값입니다.")
else :
    print(f"원의 면적은 {pi*math.pow(x, 2)}입니다.")
