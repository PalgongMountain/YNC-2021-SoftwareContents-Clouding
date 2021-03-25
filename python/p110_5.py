"""
화씨 온도를 읽어서 섭씨 온도로 변환하는 프로그램
학번 : 2105080
이름 : 임지홍

fahren = 화씨
celsius = 섭씨
"""

fahren = int(input("화씨 온도를 입력하시오: "))
celsius = (fahren - 32.0) * 5/9

print(f"화씨 {fahren}도는 섭씨 {round(celsius,2)}도에 해당합니다.")
