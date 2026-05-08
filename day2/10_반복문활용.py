# end보다 start숫자가 더 크면 '시작 숫자가 더 큽니다.' 출력 후
# 두 숫자를 다시 입력 받을 수 있도록
while True :
    start = int(input("시작 숫자 : "))
    end = int(input("끝 숫자 : "))
    if end < start :
        print("시작 숫자가 더 큽니다. 다시 입력하쇼")
        continue
    sum = 0
    for a in range(start, end+1) :
        sum += a
    print(f"합 : {sum}")
    break