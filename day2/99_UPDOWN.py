import random

random_number = random.randint(1, 100)
cnt = 0
print("=== Up & Down 게임을 시작합니다! ===")
print("1부터 100 사이의 숫자를 맞춰보세요.")

while True:
    num = int(input("숫자를 입력하세요: "))
    
    if num < 1 or num > 100:
        print("1에서 100 사이의 숫자만 입력해주세요!")
        continue
    
    cnt += 1
    if num < random_number:
        print("▲ UP!")
    elif num > random_number:
        print("▼ DOWN!")
    else:
        print(f"{cnt}번 만에 정답!")
        break
