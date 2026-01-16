# function trong python: dung de thuc thi mot khoi cau lenh nao do
# tai su dung lai o nhieu ;;;;;;;;;;;/cho
# cach viet: def ten_ham():

# void function: in ra gi do hoac thay doi mot dieu gi do
# a = 10
# def do_something():
#     global a
#     a = 100
#     print("hom nay troi ha noi kha ret")

# do_something()

# print(a)

# return: tra ve mot gia tri nao do duoc viet trong ham

# def count_plus():
#     return 10 + 10

# print(count_plus())

# params: tham so cua ham, co the co nhieu hon 1 tham so
# def f(x = 2, y = 1):
#     return x ** 2 + 2 * x + 3 + y * 2

# print(f())

# bài tập: tạo 1 function có 3 tham số lần lượt là số thứ 1 số thứ 2 và phép tính
# khi gọi hàm thì kết quả phép tính sẽ được thực thi dựa theo những tham số mà người dùng khai báo

# def calc(a, b, op):
#     if op == "+":
#         return a + b
#     if op == "-":
#         return a - b
#     if op == "*":
#         return a * b
#     if op == "/":
#         return a / b

# print(calc(3, 6, "+"))
# print(calc(4, 1, "-"))
# print(calc(6, 1, "*"))
# print(calc(6, 7, "/"))

# Tao 1 chương trình quản lý 1 mảng món ăn
# Tạo ra 4 function để xử lý các chức năng: Create, update, delete, read

# Creat: dùng để thêm mới 1 giá trị vào mảng
# VD: def create(newValue)

# Update: Thay thế 1 món ăn nào đó nằm trong mảng
# VD: def update(position, newValue)

# Delete: Xoá 1 phần thử bất kỳ nằm trong mảng
# VD: def delete(position, clear=False)

# Read: Đọc full dữ liệu nằm trong mảng và in ra theo dạng:
# VD: def read():
# 1. món thứ 1
# 2. món thứ 2 
# 3. ...

# foods = ["taco", "fries", "burger", "pizza"]

# def create(newValue):
#     foods.append(newValue)

# def update(position, newValue):
#     foods[position] = newValue

# def delete(position, clear=False):
#     if clear == True:
#         foods.clear()
#     else:
#         foods.pop(position)

# def read():
#     for i in range(len(foods)):
#         print(str(i + 1) + ". " + foods[i])

# def sort_by_length():
#     foods.sort(key=len)

# read()

# x = input("add food: ")
# create(x)
# read()

# p = int(input("update position: "))
# v = input("new food: ")
# update(p - 1, v)
# read()

# d = int(input("delete position: "))
# delete(d - 1)
# read()

# sort_by_length()
# print("sorted by length: ")
# read()


# lập function sắp xếp các món ăn trong mảng dựa theo độ dài của từ ví dụ:
# 1. bun
# 2. nem chua
# 3. pepperoni pizza

# bai1
# def is_int(num):
#     return num == int(num)

# num = float(input("input number: "))

# if is_int(num):
#     print(f"{int(num)} is an integer")
# else:
#     print(f"{num} is not an integer")

# bai2
# def is_prime(n):
#     if n <= 1:
#         return False

#     for i in range(2, n):
#         if n % i == 0:
#             return False

#     return True


# num = int(input("input number: "))

# if is_prime(num):
#     print(f"{num} is a prime")
# else:
#     print(f"{num} is not a prime")

# bai3
# def is_prime(n):
#     if n <= 1:
#         return False

#     for i in range(2, n):
#         if n % i == 0:
#             return False

#     return True


# n = int(input("input number: "))

# count = 0
# num = 2

# print(f"first {n} prime(s):", end=" ")

# while count < n:
#     if is_prime(num):
#         print(num, end=" ")
#         count += 1
#     num += 1

# bai4
# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result = result * i
#     return result


# n = int(input("input number: "))

# total = 0
# for i in range(1, n + 1):
#     total = total + factorial(i) // i

# print("result:", total)

# bai5
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


n = int(input("Input number: "))

total = 0
for i in range(1, n + 1):
    total = total + factorial(i) // i

print("Result:", total)

