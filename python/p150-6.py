"""
1에서 3 사이의 정수를 입력받아 컴퓨터와 가위바위보 게임을 하는 프로그램

학번 : 2105080
이름 : 임지홍
"""
import sys,random

user = eval(input("선택하세요(1 : 가위, 2 : 바위, 3 : 보) "))

isuserwin = False
iscpuwin = False
isdraw = False

if type(user) == type(0.1):
    sys.exit("실수는 입력할 수 없습니다.")
    
if(user <= 0 or user >= 4) :
    sys.exit("수를 잘못 입력했습니다. 1에서 3 사이의 수를 입력해주세요")
    
cpu = random.randint(1, 3)

if user == cpu:
    isdraw = True
elif user == 1 :
    if cpu == 2 :
        iscpuwin = True
    elif cpu == 3 :
        isuserwin = True
elif user == 2 :
    if cpu == 3 :
        iscpuwin = True
    elif cpu == 1 :
        isuserwin = True
elif user == 3 :
    if cpu == 1 :
        iscpuwin = True
    elif cpu == 2 :
        isuserwin = True

print(f"컴퓨터의 선택(1 : 가위, 2 : 바위, 3 : 보) {cpu}")

if iscpuwin :
    print("컴퓨터가 이겼음")
elif isuserwin :
    print("사용자가 이겼음")
elif isdraw :
    print("비겼음")
    
        



    

    

