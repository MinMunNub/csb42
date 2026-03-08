# while true lam input de nguoi dung nhap vao de them sua xoa file
# 1. them
# 2. sua
# 3. xoa
# 4. doc
# 5. dong

# def create():
#     new_name = input("Enter person name")
#     new_age = input("Enter person age")
#     new_gender = input("Enter person gender")
    
#     current_id = list_person[len(list_person) - 1]["id"]
#     new_id = current_id + 1

#     new_person = {
#         "id": new_id,
#         "full_name": new_name,
#         "age": new_age,
#         "gender": new_gender
#     }

#     list_person.append(new_person)

# while True:
#     print("--------------")
#     print("[1]. Add thêm dong vào file")
#     print("[2]. In ra toàn bộ file")
#     print("[3]. Update lại dong của 1 gia bất kỳ nằm theo trong file")
#     print("[4]. Xoá 1 dong bất kỳ nằm trong list dựa theo input người dùng nhập")
#     print("[0]. Exit")
#     choice = input("Enter choice: ")
    
#     if choice == "1":

#         def create():
#             text = input("nhap dong moi: ")

#             f = open("day11.txt", "a")
#             f.write(text + "\n")
#             f.close()

#     elif choice == "2":
#         print("Bạn vừa thực thi lựa chọn 2")

#     elif choice == "3":
#         print("Bạn vừa thực thi lựa chọn 3")
#     elif choice == "4":
#         print("Bạn vừa thực thi lựa chọn 4")
#         file = open('day11.txt', 'r')
#         lines = file.readlines()
#         for line in lines:
#             print(line)
#         file.close()

#     elif choice == "0":
#         print("Cam on ban da nhap lua chonnnnn !!!!")
#         break

file = "day11.txt"

while True:
    print("1 them")
    print("2 doc")
    print("3 sua")
    print("4 xoa")
    print("5 in ra tong so luong chu cai")
    print("0 thoat")

    c = input("choice: ")

    if c == "1":
        t = input("text: ")
        open(file, "a").write(t + "\n")

    elif c == "2":
        lines = open(file).readlines()
        for i in range(len(lines)):
            print(i, lines[i].strip())

    elif c == "3":
        lines = open(file).readlines()
        for i in range(len(lines)):
            print(i, lines[i].strip())
        i = int(input("index: "))
        t = input("new text: ")
        lines[i] = t + "\n"
        open(file, "w").writelines(lines)

    elif c == "4":
        lines = open(file).readlines()
        for i in range(len(lines)):
            print(i, lines[i].strip())
        i = int(input("index: "))
        lines.pop(i)
        open(file, "w").writelines(lines)

    elif c == "5":
        import re

        with open('day11.txt', 'w') as file:
            file.write('day11.txt')

        def extract_and_sum(file_name):
            with open(file_name, 'r') as file:
                content = file.read()

                numbers = re.findall(r'\d+', content)

            return sum(map(int, numbers))

    result = extract_and_sum("day11.txt")
    print("The sum of numbers in the file is:", result)





    