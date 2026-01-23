# person = {
#     "name": "danhphuongskibidi",
#     "age": 36,
#     "city": "thanh hoa"

# }

# viet 3 input de update lai dictionary person tren

# person["name"] = input("enter name: ")
# person["age"] = int(input("enter age: "))
# person["city"] = input("enter city: ")

# print(person)

# list_person = [
#     {
#         "name": "Alice",
#         "age": 30,
#         "city": "New York"
#     },
#     {
#         "name": "Danh Phuong",
#         "age": 24,
#         "city": "Ha Noi"
#     }
# ]

# in ra moi ten danh phuong

# for p in list_person:
#     if p["name"] == "Danh Phuong":
#         print(p["name"])

# print(list_person[1]['name'])

# list_person = [
#     {
#         "name": "Alice",
#         "age": 30,
#         "city": "New York"
#     },
#     {
#         "name": "Danh Phuong",
#         "age": 24,
#         "city": "Ha Noi"
#     }
# ]

# Yeu cau 2:
# Tạo ra thêm 1 input cho phép người dùng chọn dictionary muốn thay đổi nằm trong List
# lua chọn chỉ có hiện ra là 1 hoặc 2
# Nếu chọn 1 thì update thằng đầu tiên
#
# Sau khi chọn xong thì hiện ra 3 input để update person tại vị trí mình chọn

# choice = int(input("choose 1 or 2: "))

# if choice == 1:
#     i = 0
# else:
#     i = 1

# list_person[i]["name"] = input("enter name: ")
# list_person[i]["age"] = int(input("enter age: "))
# list_person[i]["city"] = input("enter city: ")

# print(list_person)

# list_person = [
#     {
#         "id": 1,
#         "full_name": "Nguyen Van A",
#         "age": 25,
#         "gender": "male"
#     },
#     {
#         "id": 2,
#         "full_name": "Tran Thi B",
#         "age": 23,
#         "gender": "female"
#     },

#     {
#         "id": 3,
#         "full_name": "Le Hoang C",
#         "age": 28,
#         "gender": "male"
#     },
#     {
#         "id": 4,
#         "full_name": "Pham Ngoc D",
#         "age": 26,
#         "gender": "female"
#     },
#     {
#         "id": 5,
#         "full_name": "Vo Minh E",
#         "age": 30,
#         "gender": "male"
#     },
#     {
#         "id": 6,
#         "full_name": "Dang Thi F",
#         "age": 24,
#         "gender": "female"
#     },
#     {
#         "id": 7,
#         "full_name": "Bui Quang G",
#         "age": 27,
#         "gender": "male"
#     },
#     {
#         "id": 8,
#         "full_name": "Hoang Lan H",
#         "age": 22,
#         "gender": "female"
#     }
# ]

# Yeu cau 3:
# Tạo ra thêm 1 input cho phép người dùng chọn dictionary muốn thay đổi nằm trong List
# Cho nguoi dung chon 1 trong 8 object
# Nếu chọn 1 thì update thằng đầu tiên
#
# Sau khi chọn xong thì hiện ra 3 input để update person tại vị trí mình chọn

# choice = int(input("choose 1 to 8: "))

# i = choice - 1

# list_person[i]["full_name"] = input("enter full name: ")
# list_person[i]["age"] = int(input("enter age: "))
# list_person[i]["gender"] = input("enter gender: ")

# print(list_person)

list_person = [
    {
        "id": 1,
        "full_name": "Nguyen Van A",
        "age": 25,
        "gender": "male"
    },
    {
        "id": 2,
        "full_name": "Tran Thi B",
        "age": 23,
        "gender": "female"
    },

    {
        "id": 3,
        "full_name": "Le Hoang C",
        "age": 28,
        "gender": "male"
    },
    {
        "id": 4,
        "full_name": "Pham Ngoc D",
        "age": 26,
        "gender": "female"
    },
    {
        "id": 5,
        "full_name": "Vo Minh E",
        "age": 30,
        "gender": "male"
    },
    {
        "id": 6,
        "full_name": "Dang Thi F",
        "age": 24,
        "gender": "female"
    },
    {
        "id": 7,
        "full_name": "Bui Quang G",
        "age": 27,
        "gender": "male"
    },
    {
        "id": 8,
        "full_name": "Hoang Lan H",
        "age": 22,
        "gender": "female"
    }
]

# * [1] Add thêu person vào List_person
# Hiện ra 3 input cho phép người dùng khai bào 1 person môiw
# = [2]. In ra toàn bộ person đang có theo dạng:
# 1. person1 - agel - gender 1
# 2. person2 - age2 - gender 2
# * [3] Update lại giá trị của 1 person bất kỳ nằm trong List_person
# * - Cho phép người dùng nhập 1 id bất kỳ muốn thay đổi thông tin
# * – Hiện ra lần lượt 3 input đẻ người dùng thay đổi cho person đô
# #
# * [4] Xoa 1 person bất kỳ nằm trong List dựa theo input người dùng nhận
# # [5]. Sap xep lại List hưa theo age (Thứ tư tăng dẫn)
# * [0] Thoat chuong trinh

# *su dung cau truc while true

while True:
    print("\n1 add 2 show 3 update 4 delete 5 sort age 0 exit")
    c = input("choose: ")

    if c == "1":
        name = input("name: ")
        age = int(input("age: "))
        gender = input("gender: ")
        new_id = 1 if not list_person else max(p["id"] for p in list_person) + 1
        list_person.append({
            "id": new_id,
            "full_name": name,
            "age": age,
            "gender": gender
        })

    elif c == "2":
        for p in list_person:
            print(p["id"], p["full_name"], "-", p["age"], "-", p["gender"])

    elif c == "3":
        x = int(input("id: "))
        for p in list_person:
            if p["id"] == x:
                p["full_name"] = input("name: ")
                p["age"] = int(input("age: "))
                p["gender"] = input("gender: ")
                break
        else:
            print("id not found")

    elif c == "4":
        x = int(input("id: "))
        for p in list_person:
            if p["id"] == x:
                list_person.remove(p)
                print("deleted")
                break
        else:
            print("id not found")

    elif c == "5":
        for i in range(len(list_person)):
            for j in range(i + 1, len(list_person)):
                if list_person[i]["age"] > list_person[j]["age"]:
                    list_person[i], list_person[j] = list_person[j], list_person[i]

        print("sorted by age:")
        for p in list_person:
            print(p["id"], p["full_name"], "-", p["age"], "-", p["gender"])

    elif c == "0":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")









