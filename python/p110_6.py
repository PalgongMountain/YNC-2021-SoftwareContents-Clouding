"""
음식 비용을 입력하면 팁을 포함한 전체 금액을 계산하는 프로그램
학번 : 2105080
이름 : 임지홍
"""

food_cost = int(input("음식 비용: "))
tip_str = input("팁 비율: ")

tip = int(tip_str[0:2])

total = food_cost + food_cost * (tip/100)

print(f"food = {food_cost}, tip = {tip}")
print(f"총액: {total} 달러")
