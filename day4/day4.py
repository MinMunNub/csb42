# listUser = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
# len(list): In ra số lượng phần tử có trong list 
# Các phần tử nằm trong list sẽ bắt đầu từ số 0
# Note: 0 <= index < len(list)
# Truy cập vào các phần tử bất kỳ trong list: Tên_list[index]
# Thêm 1 phần tử mới vào trong list: tên_list.append(newValue)

# print("So luong phan tu: ", len(listUser))
# print(listUser)
# print(listUser[0])
# print(listUser[len(listUser) - 1])

# # thêm:
# listUser.append("Danh Phuong")
# print(listUser)

# listUser.remove("Charlie")

# listUser.pop()
# print(listUser)

# tao mot input, nguoi dung nhap so 1 2 3 4 va lam theo

# 1.nhap de them thong tin vao trong list
# 2.xos 1 gia tri ma nguoi dung nhap
# 3.print ra 1 gia tri ma nguoi dung nhap
# 4.in ra toan bo list

# listUser = ["Alice", "Bob", "Charlie", "Kirk", "Ethan"]


# choice = input("nhap so 1 2 3 hoac 4: ")

# if choice == "1":
#     name = input("Nhap ten can them: ")
#     listUser.append(name)
#     print(listUser)

# elif choice == "2":
#     name = input("Nhap ten can xoa: ")
#     if name in listUser:
#         listUser.remove(name)
#         print(listUser)

# elif choice == "3":
#     name = input("nhap ten can in: ")
#     if name in listUser:
#         print(name)

# elif choice == "4":
#     s = ""
#     for i in range(0, 5):
#         s = s + str(i)
#         if i < 4:
#             s = s + " - "
#         print(s)



# s = ""
# s = s + "0" + "-"
# s = s + "1" + "="
# s = s + "2" + "-"
# s = s + "3" + "-"
# s = s + "4" + "-"

# 1 + 2 + 3 + 4 + 5 + ... + n = tong

s = ""
for i in range(1, 11):
        s = s + str(i)
        if i < 10:
            s = s + " + "
            tong = sum(range(1, 11))
        print(s, "= ", tong)









