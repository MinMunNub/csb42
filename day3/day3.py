# vòng lặp trong Python
# Sử dụng vòng lặp for khi biết trước số lần lặp hoặc khi duyệt qua các phần tử trong một tập hợp.
# Cú pháp:
# for biến_đếm in tập_hợp:
#     khối_lệnh

# Ví dụ sử dụng vòng lặp for để in các số từ 1 đến 5
# Chú ý: Hàm range(a, b) tạo ra một dãy số từ a đến b-1
# Ký tự [ biểu thị cho việc lớn hơn hoặc bằng, ký tự ) biểu thị cho việc nhỏ hơn.
# 1, 2, 3, 4, 5 || [1,6)
# for i in range(1, 6):  # 1, 2, 3, 4, 5 || [1,6)
#     print(i)

# ví dụ sử dụng vòng lặp for để duyệt qua các phần tử trong một danh sách (lít)
# fruits = ["apple", "banna", "cherry"]
# for fruit in fruits:
#     print(fruit)

# sử dụng vòng lặp while khi không biết trước số lần lặp và cần lặp dựa trên một điều kiện.
# cú pháp:
# while điều_kiện:
#     khối_lệnh

# sử dụng vòng lặp while để in ra các số từ 1 đến 5
# i = 1
# while i <= 5:
#     print(i)
#     i += 1
    # tăng biến để tránh vòng lặp vô hạn 

# Bài tập vòng lặp
# Bài tập 1: Sử dụng vòng lặp for để tính tổng các số từ 1 đến 100 và in kết quả.
# bài tập 2: Sử dụng vòng lặp while để in các số chẵn từ 2 đến 20.
# Bài 3: Sử dụng vòng lặp for để in tất cả các phần tử trong một danh sách các số nguyên.
# Bài 4: Sử dụng vòng lặp while để yêu cầu người dùng nhập một số dương.
# Nếu người dùng nhập số âm hoặc số 0, yêu cầu họ nhập lại.

# # b1
# a = 0
# for i in range(1, 101):
#     a += i
# print("tong tu 1 den 100 la:", a)

# # b2
# a = 2
# while a <= 20:
#     print(a)
#     a += 2

# # b3
# a = [5, 10, 15, 20, 25]
# for x in a:
#     print(x)

# # b4
# a = int(input("nhap so duong: "))
# while a <= 0:
#     a = int(input("no phai so duong: "))
# print("ban da nhap: ", a)

# Dictionary trong Python
# Dictionary (từ điển) là một cấu trúc dữ liệu trong Python dùng để lưu trữ các cặp khóa-giá trị.
# Mỗi khóa trong dictionary phải là duy nhất và được sử dụng để truy cập giá trị tương ứng.
# Cú pháp tạo một dictionary:
# my_dict = {
# "key1": "value1",
# "key2": "value2",
# "key3": "value3"
# }

# Ví dụ tạo một dictionary và truy cập các giá trị

# student = {
# "name": "Alice",
# "age": 20,
# "major": "Computer Science"
# }

# Truy cập trong dictionary
# Truy cập giá trị bằng khóa

# print("Name:", student["name"])
# print("Age:", student["age"])

# Sử dụng phương thức items() để duyệt qua cả khóa và giá trị
# for key, value in student.items():
#     print(key, ":", value)

# print("items():", student.items())

# Cập nhật giá trị trong dictionary
# student["age"] = 21
# print("Updated age:", student["age"])

# Sử dụng update() để cập nhật
# student.update({"age": 21})
# student.update({"major": "Data Science", "age": 22})
# print("Updated student dictionary:", student)

# Xóa phần tử trong dictionary
# Sử dụng del để xóa một cặp khóa-giá trị
# del student["major"]
# print("Updated student dictionary after deletion:", student)

# Sử dụng pop() để xóa và trả về giá trị của khóa đã xóa
# removed_value = student.pop("age")
# print("Removed age:", removed_value)
# print("Updated student dictionary after pop:", student)

# Bài tập 1: Tạo một dictionary để lưu trữ thông tin về một cuốn sách (tiêu đề, tác giả, năm xuất bản, số trang).

# Bài tập 2: Tạo một dictionary chứa tên các loại trái cây và giá của chúng.
# Thực hiện:
# In giá của một loại trái cây bất kỳ.
# Thêm một loại trái cây mới.
# Cập nhật giá của một loại trái cây có sẵn.

# Bài tập 3: Sử dụng vòng lặp for để in tất cả các khóa và giá trị trong dictionary đã tạo ở bài tập 1 hoặc 2.

# Bài tập 4: Viết một chương trình để đếm số lần xuất hiện của mỗi từ trong một câu nhập từ người dùng.
# Sử dụng dictionary để lưu trữ từ và số lần xuất hiện của chúng.

# b1
book = {
    "title": "van goth",
    "author": "mona lisa",
    "year": 3667,
    "pages": 41
}

print(book)

# b2
fruits = {
    "apple": 36000,
    "banana": 67000,
    "orange": 18000
}

print(fruits["banana"])      
fruits["mango"] = 61000         
fruits["apple"] = 36360         
print(fruits)

# b3
for key, value in book.items():
    print(key, ":", value)

# b4

