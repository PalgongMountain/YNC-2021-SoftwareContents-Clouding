"""
시간과 분을 입력받아 초로 변환하는 프로그램
"""

hour = int(input("시간을 입력하세요: "))
min = int(input("분을 입력하세요: "))

sec = hour * 3600 + min * 60

print(f"{hour} 시간 {min} 분은 {sec} 초입니다.")