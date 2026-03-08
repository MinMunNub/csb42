# file = "day12.txt"

# while True:
#     print("1 them")
#     print("2 doc")
#     print("3 sua")
#     print("4 xoa")
#     print("5 dem so luong chu cai")
#     print("6 nhap n dong")
#     print("0 thoat")

#     c = input("choice: ")

#     if c == "1":
#         t = input("text: ")
#         open(file, "a").write(t + "\n")

#     elif c == "2":
#         lines = open(file).readlines()
#         for i in range(len(lines)):
#             print(i, lines[i].strip())

#     elif c == "3":
#         lines = open(file).readlines()
#         for i in range(len(lines)):
#             print(i, lines[i].strip())

#         index = int(input("nhap index muon sua: "))

#         if 0 <= index < len(lines):
#             new_text = input("nhap gia tri moi")
#             lines[index] = new_text + "\n"
#             open(file, "w").writelines(lines)
#             print("sua thanh cong")
#         else:
#             print("index ko hop le")

#     elif c == "4":
#         lines = open(file).readlines()
#         for i in range(len(lines)):
#             print(i, lines[i].strip())

#         i = int(input("index: "))
#         lines.pop(i)
#         open(file, "w").writelines(lines)

#     elif c == "5":
#         text = open(file).read()
#         dem = 0
#         for ch in text:
#             if ch.isalpha():
#                 dem += 1
#         print("Tong so luong chu cai:", dem)

#     elif c == "6":
#         n = int(input("Nhap so dong muon ghi: "))
#         f = open(file, "a")
#         for i in range(n):
#             t = input("Nhap dong thu " + str(i+1) + ": ")
#             f.write(t + "\n")
#         f.close()

#     elif c == "0":
#         break

# yc3
file = "person.txt"

n = int(input("nhap so nguoi: "))

f = open(file, "a")

for i in range(n):
    print("nguoi thu", i + 1)

    name = input("nhap ten: ")
    age = input("nhap tuoi: ")
    address = input("nhap dia chi: ")
    point = input("nhap diem: ")

    f.write(name + " - " + age + " - " + address + " - " + point + "\n")

f.close()

print("da luu thanh cong!")

lines = open(file).readlines()

for i in range(len(lines)):
    print(i, lines[i].strip())

i = int(input("nhap index muon sua: "))

name = input("nhap ten moi: ")
age = input("nhap tuoi moi: ")
address = input("nhap dia chi moi: ")
point = input("nhap diem moi: ")

lines[i] = name + " - " + age + " - " + address + " - " + point + "\n"

open(file, "w").writelines(lines)

print("da cap nhat!")