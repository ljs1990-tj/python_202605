from student import Student
student_dict = {}



def student_add() : 
    stu_no = input("학번 : ")
    name = input("이름 : ")
    dept = input("학과 : ")
    s = Student(stu_no, name, dept)
    student_dict[stu_no] = s
    # print(student_dict)
    # 학번, 이름, 학과를 입력받아서 
    # student_dict에 저장
    # 저장 방법은 {"학번" : Student객체}
    
def student_grade_update() :
    stu_no = input("학번 입력 : ")
    if stu_no in student_dict :
        s = student_dict[stu_no]
        grade = int(input("학년 입력 : "))
        s.set_stu_grade(grade)
    else :
        print("해당 학번 없음")
# 3
def student_search() :
    stu_no = input("학번 입력 : ")
    if stu_no in student_dict :
        s = student_dict[stu_no]
        print(f"학번 : {stu_no}, 이름 : {s.get_stu_name()}", end=", ")
        print(f"학과 : {s.get_stu_dept()}, 학년 : {s.get_stu_grade()}")
    else :
        print("해당 학번 없음")
    # 학번 입력받아서 있으면
    # 학번, 이름, 학과, 학년 출력
    # 학번 없으면 '없는 학생' 출력 후 메뉴로
    # 필요에 따라 Student 클래스 수정해도 됨

while True :
    menu = input("[ (1) 학생추가 (2) 학년 수정 (3) 학생 검색 ... (5) 종료 ] : ")
    if menu == "1" :
        student_add()
    elif menu == "2" :
        student_grade_update()
    elif menu == "3" :
        student_search()
    elif menu == "4" :
        pass
    else :
        break

# hong = Student("1234", "홍길동", "컴퓨터")
# print(hong.get_stu_grade())

# test = []
# test.append(hong)
# print(test)

