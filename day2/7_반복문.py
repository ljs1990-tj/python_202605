# 입력한 숫자의 구구단을 출력
# ex) 3입력 시 3단 출력
# dan = int(input("단을 입력해주셈 : "))

# for a in range(1, 10) : 
#     print(f"{dan} * {a} = {dan*a}")
    
# 2~9단까지 모두 출력

for x in range(2, 10) :
    print("="*6, f"{x}단", "="*6)
    for y in range(1, 10) :
        print(f"{x} * {y} = {x*y}")