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

student_list = []
while True :
    menu = input("[ (1)등록 (2)수정 (3)삭제 (4)검색 (5)종료 ] : ")
    if menu == "1" :
        name = input("이름 : ")
        flg = False
        for i in range(len(student_list)) :
            stu = student_list[i]        
            if stu["name"] == name :
                print("이미 존재하는 학생입니다.")
                flg = True
                break
        if flg == True:
            continue
        dept = input("학과 : ")
        addr = input("주소 : ")
        phone = input("번호 : ")
        student_list.append({"name" : name, "dept" : dept, "addr" : addr, "phone" : phone})
    elif menu == "2" :
        name = input("이름 : ")
        for i in range(len(student_list)) :
            stu = student_list[i]
            flg = False
            if stu["name"] == name :
                dept = input("학과 : ")
                addr = input("주소 : ")
                phone = input("번호 : ")
                student_list[i] = {"name" : name, "dept" : dept, "addr" : addr, "phone" : phone}
                flg = True
                break
        if flg == False : 
            print("없는 학생")
    elif menu == "3" :
        name = input("이름 : ")
        for i in range(len(student_list)) :
            stu = student_list[i]
            if stu["name"] == name :
                student_list.pop(i)
                flg = True
                break
        if flg == False : 
            print("없는 학생")
    elif menu == "4" :
        name = input("이름 : ")
        for i in range(len(student_list)) :
            stu = student_list[i]
            flg = False
            if stu["name"] == name :
                print(f"이름 : {name}, 학과 : {stu["dept"]}, 주소 : {stu["addr"]}, 번호 : {stu["phone"]}")
                flg = True
                break
        if flg == False : 
            print("없는 학생")
    else :
        print("종료되었습니다.")
        break