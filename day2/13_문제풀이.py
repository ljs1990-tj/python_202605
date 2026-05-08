
user = {}
while True :
    menu = input("[ (1) 친구 등록 (2) 검색 (그 외) 종료 ] : ")
    if menu == "1" :
        name = input("이름 : ")
        phone = input("번호 : ")
        user[name] = phone
    elif menu == "2" :
        name = input("이름 : ")
        if name in user :
            print(f"{name}의 번호는 {user[name]} 입니다.")
        else :
            print("해당 이름 없음")
    else :
        print("종료되었습니다.")
        break
    
# {"철수" : "1234", "영희" : "2323", ...}

# [
#   {name : "철수", addr : "인천", phone : "1234"}, 
#   {name : "영희", addr : "서울", phone : "2323"}
#]

# {
#   "철수" : {name : "철수", addr : "인천", phone : "1234"}, 
#   "영희" : {name : "영희", addr : "서울", phone : "2323"}
#}