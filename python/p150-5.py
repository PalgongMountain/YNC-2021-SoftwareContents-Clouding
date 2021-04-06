"""
3개의 정수를 입력받아 가장 작은 값을 결정하는 프로그램

학번 : 2105080
이름 : 임지홍
"""
import sys

try :
    print("(정수를 입력할 때, \"x,y,z\"형식으로 입력해주세요)")
    x, y, z = eval(input("3개의 정수를 입력하세요 : "))
except :
    sys.exit("입력 형식이 잘못됐습니다. 각 정수를 ','기호로 구분해주세요.")

if type(x) == type(0.1) or type(y) == type(0.1) or type(z) == type(0.1):
    sys.exit("실수는 입력할 수 없습니다.")
    
if x < y :
    min = x
else :
    min = y

if min > z :
    min = z

print(f"제일 작은 정수는 {min}입니다.")