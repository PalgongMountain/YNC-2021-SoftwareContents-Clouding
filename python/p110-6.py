"""
음식 비용을 입력하면 팁을 포함한 전체 금액을 계산하는 프로그램
학번 : 2105080
이름 : 임지홍
"""

food_cost = int(input("음식 비용을 입력하세요 : "))
tip = int(input("팁의 비율을 입력하세요(%): "))

total = food_cost + food_cost * tip / 100 

print(f"음식 비용 = {food_cost}\n팁 = {tip}%")
print(f"총액: {total} 달러")
