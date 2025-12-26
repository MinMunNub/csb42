# listUser = ["Alice", "Bob", "Charlie", "Kirk", "Ethan"]
# del listUser[0]
# print(listUser)

# text = "reference site about lorem ipsum"
# len(tên_chuỗi) => in ra số lượng ký tự trong 1 chuỗi
# truy cập vào các vị trí nằm trong 1 chuỗi: tên_chuỗi[index]
# note: 0 <= index < len(tên_chuỗi)
# cắt chuỗi: tên_chuỗi[start: end] => lấy trong khoảng bắt đầu và kết thúc
# start <= text < end
# trỏ vào phần tử cuối cùng nằm trong 1 chuỗi: tên_chuỗi[len(tên_chuỗi) - 1]
# print("length: " + str(len(text)))
# giá trị của length sẽ luôn lớn hơn ký tự cuối cùng của chuỗi 1 đơn vị
# print(text[9])

# bài 1 cho phép nhập 2 input start và end
# => in ra chuỗi trong khoảng start và end

# bài 2 cho phép người dùng thêm 1 ký tự vào trong chuỗi
# có 2 input
# -1: hiện ra vị trí muốn thêm
# -2: nhạp ký tự muốn thêm 

# bai1
# text = ["Alice", "Bob", "Charlie", "Kirk", "Ethan"]

# start = int(input("nhap start: "))
# end = int(input("nhap end: "))

# print(text[start:end])

# bai2
# text = ["Alice", "Bob", "Charlie", "Kirk", "Ethan"]

# pos = int(input("nhap vi tri muon them: "))
# char = input("nhap ky tu muon them: ")

# text.insert(pos, char)
# print(text)

# Bài 3: check xem ký tự đó có tồn tại trong text không
# Input: nhập 1 ký tự bất kỳ
# Ouput: in ra "Có" nếu tồn tại và in ra "KHÔNG" nếu không tồn tại

# text = "reference site about lorem ipsum"

# Bài 4: Tìm kiếm số lần xuất hiện của 1 ký tự nằm trong chuỗi t
# Input: nhập 1 ký tự bất kỳ
# Output: Đếm số lần xuất hiện cua ký tự đó

# text = "reference site about lorem ipsum"

# # bai3
# text = "reference site about lorem ipsum"

# char = input("nhap 1 ky tu: ")

# if char in text:
#     print("co")
# else:
#     print("danh phuong skibidi")

# bai4
# text = "reference site about lorem ipsum"

# char = input("nhap 1 ky tu: ")

# count = 0

# for c in text:
#     if c == char:
#         count = count + 1

# print("so lan xuat hien:", count)

# bai1
# n = int(input("input number: "))

# for i in range(1, n + 1):
#     print("#" * i)

# bai2
# num = float(input("input a positive number: "))

# while num <= 0:
#     num = float(input("input a positive number: "))

# print("thank you.")

# bai3
# n = int(input("input number: "))

# if n < 0:
#     print("invalid")
# else:
#     result = 1
#     for i in range(1, n + 1):
#         result = result * i
#     print(str(n) + "! = " + str(result))

# bai4
# num = input("input number: ")

# total = 0

# for c in num:
#     total = total + int(c)

# print("Sum of digits of " + num + " = " + str(total))

# bai5
# count = 0
# num = 1000

# print("numbers with sum of digits = 9:")

# while count < 10:
#     s = 0
#     for c in str(num):
#         s = s + int(c)

#     if s == 9:
#         print(num, end=" ")
#         count = count + 1

#     num = num + 1

# bai6
# import turtle

# n = int(input("input number of edges: "))

# angle = 360 / n

# for i in range(n):
#     turtle.forward(100)
#     turtle.left(angle)

# turtle.done()

# bai7
import turtle

r = 10

for i in range(30):
    turtle.circle(r, 180)
    r = r + 5

turtle.done()

