# 학생관리 프로그램
# 동명이인 없다고 가정하고 실습
# 이름, 학과, 주소, 전화번호 입력받아서 저장
# 메뉴는 등록, 수정, 삭제, 검색, 종료

# 등록할때는 이미 등록된 이름일 경우 '이미 등록된 학생입니다' 출력
# 수정은 이름으로 검색 후 없으면 '없는 학생' 출력
    # 있으면 학과, 주소, 전화번호 다시 입력받아서 저장
# 삭제는 이름으로 검색 후 없으면 '없는 학생' 출력
    # 있으면 해당 학생 데이터 삭제
# 검색은 이름으로 검색 후 없으면 '없는 학생' 출력
    # 있으면 학생의 이름, 학과, 주소, 번호 출력 
# 종료는 프로그램 종료

students = {}
while True :
    menu = input("[ (1)등록 (2)수정 (3)삭제 (4)검색 (5)종료 ] : ")
    if menu == "1" :
        name = input("이름 : ")
        dept = input("학과 : ")
        addr = input("주소 : ")
        phone = input("번호 : ")
        students[name] = {"addr" : addr, "dept" : dept, "phone" : phone}
    elif menu == "2" :
        name = input("이름 : ")
        if name in students :
            dept = input("학과 : ")
            addr = input("주소 : ")
            phone = input("번호 : ")
            students[name] = {"addr" : addr, "dept" : dept, "phone" : phone}
        else :
            print("없는 학생")
    elif menu == "3" :
        name = input("이름 : ")
        if name in students :
            students.pop(name)
            print("삭제되었습니다.")
        else :
            print("없는 학생")
    elif menu == "4" :
        name = input("이름 : ")
        if name in students :
            student = students[name]
            print(f"이름 : {name}, 학과 : {student["dept"]}, 주소 : {student["addr"]}, 번호 : {student["phone"]}")
        else :
            print("없는 학생")
    else :
        print("종료되었습니다.")
        break