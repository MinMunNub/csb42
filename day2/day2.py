# 6. phep so sanh trong python >, <, >=, <=, ===, !=
# long dieu kien: &&, || => python: and, or
# ap dung dieu kien nhu nay thi gia tri tra ve la gi? => True/False


# a = 10
# b = 20

# c = a < b
# print("ket qua so sanh: "+ str(c))

# # if/else: cau dieu kien
# if a < b:
#     print("A < B")
# elif a == b:
#     print("A = B")
# # else: truong hop con lai khi ma ko co cai if nao dung
# else:
#     print("B > A")

# in ra ten va giai cua ban
# huy = nhat
# minh huy = nhi
# tung anh = khuyen khich


# ten = input("Nhap ten cua ban: ")

# if ten == "huy":
#     print("Giai: nhat")
# elif ten == "minh huy":
#     print("Giai: nhi")
# elif ten == "tung anh":
#     print("Giai: khuyen khich")
# else:
#     print("Khong co ten nay trong danh sach")

# nhap diem
# diem = float(input("Nhap diem cua ban: "))

# if diem < 0 or diem > 10:
#     print("-1")   
# elif diem >= 9:
#     print("A+")
# elif diem >= 8:
#     print("A")
# elif diem >= 7:
#     print("B")
# elif diem >= 6:
#     print("C")
# elif diem >= 5:
#     print("D")
# else:
#     print("E")

   

# a = int(input("Nhap so a: "))
# b = int(input("Nhap so b: "))
# c = int(input("Nhap so c: "))
# d = int(input("Nhap so d: "))

# ds = [a, b, c, d]
# ds.sort()

# print(ds[1])



# a = float(input("Nhap so a: "))
# b = float(input("Nhap so b: "))
# c = float(input("Nhap so c: "))

# if a == 0:
#     print("No solution")
# else:
#     d = b*b - 4*a*c
#     if d < 0:
#         print("No solution")
#     else:
#         x1 = (-b - d**0.5) / (2*a)
#         x2 = (-b + d**0.5) / (2*a)
#         if x1 > x2:
#             x1, x2 = x2, x1
#         print(f"{x1:.2f} {x2:.2f}")



# bai 1
# a = int(input("input number: "))

# if a % 2 == 0:
#     print(a, "is even")
# else:
#     print(a, "is odd")



# bai 2
# a = float(input("input number: "))

# if a == int(a):
#     print(a, "is an integer")
# else:
#     print(a, "is not an integer")



# bai 3
# a = input("input character: ")

# if '0' <= a <= '9':
#     print(""+ a +"  is a digit")
# else:
#     print(""+ a +"  is not a digit")



# bai 4
# a = int(input("input number: "))

# if a % 3 == 0 and a % 5 == 0:
#     print(a, "is divisible by 3 and 5")
# elif a % 3 == 0:
#     print(a, "is divisible by 3")
# elif a % 5 == 0:
#     print(a, "is divisible by 5")
# else:
#     print(a, "is not divisible by 3 or 5")



# bai 5
# print("welcome to the ultimate sercurity system")

# user = input("username: ")
# pw = input("password: ")

# if user == "skibidi" and pw == "6736":
#     print("you are logged in, admin")
# else:
#     print("wrong username or password")



# bai 6
# a = float(input("input length 1: "))
# b = float(input("input length 2: "))
# c = float(input("input length 3: "))

# if a + b > c and a + c > b and b + c > a:
#     print("the 3 line segments can form a triangle")
# else:
#     print("the 3 line segments cannot form a triangle")



# bai 7
# a = float(input("input length 1: "))
# b = float(input("input length 2: "))
# c = float(input("input length 3: "))

# if a + b <= c or a + c <= b or b + c <= a:
#     print("the 3 line segments cannot form a triangle")
# elif a == b == c:
#     print("the 3 line segments can form an equilateral triangle")
# elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
#     print("the 3 line segments can form a right triangle")
# else:
#     print("the 3 line segments can form a triangle")























