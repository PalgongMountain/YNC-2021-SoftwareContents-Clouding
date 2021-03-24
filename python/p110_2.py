"""
닭, 돼지, 소의 다리 갯수를 구하는 프로그램
"""

chicken = int(input("닭이 몇마리 인가요? : "))
pig = int(input("돼지가 몇마리 인가요? : "))
cow = int(input("소가 몇마리 인가요? : "))

total_leg = chicken * 2 + pig * 4 + cow * 4

print(f"닭은 {chicken}마리이고 돼지는 {pig}마리이고 소는 {cow}마리 일 때 전체 다리갯수는 {total_leg}입니다.")
