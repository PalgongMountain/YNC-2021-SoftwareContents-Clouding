"""
두 개의 정수를 입력받아 합, 차, 곱, 평균
큰수, 작은수를 구하는 프로그램
"""
x = int(input("x: "))
y = int(input("y: "))

sum = x + y
sub = x - y
multi = x * y
avg = (x + y) / 2
max = max(x,y)
min = min(x,y)

print(f"두수의 합: {sum}")
print(f"두수의 차: {sub}")
print(f"두수의 곱: {multi}")
print(f"두수의 평균: {avg}")
print(f"큰수: {max}")
print(f"작은수: {min}")

