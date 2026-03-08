#  p1
# # b1
# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False

# num = int(input("input a number: "))

# if is_even(num):
#     print("this number is even")
# else:
#     print("this number is not even")

# # b2
# def cal_area(r):
#     return 3.14 * r * r

# radius = float(input("input radius: "))
# area = cal_area(radius)

# print("circle's area:", area)

# # b3
# def reverse_str(s):
#     return s[::-1]

# text = input("input a text: ")
# print("reversed text:", reverse_str(text))

# # b4
# def is_palindrome(s):
#     if s ==s[::-1]:
#         return True
#     else:
#         return False
    
# text = input("input a text: ")

# if is_palindrome(text):
#     print("this is a palindrome")
# else:
#     print("this is not a palindrome")

# p2
# # b1
# def factorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result = result * i
#     return result

# n = int(input("input a number: "))
# print(n, "! =", factorial(n))

# # b2
# def sort_list(lst):
#     for i in range(len(lst)):
#         for j in range(i+1, len(lst)):
#             if lst[i] > lst[j]:
#                 temp = lst[i]
#                 lst[i] = lst[j]
#                 lst[j] = temp
#     return lst

# numbers = [5, 1, 8, 92, -1, 30]

# print("original list")
# print(numbers)

# sorted_numbers = sort_list(numbers)

# print("sorted list")
# print(sorted_numbers)

# # b3
# def print_fibo(n):
#     a = 1
#     b = 1
#     for i in range(n):
#         print(a, end=" ")
#         c = a + b
#         a = b
#         b = c

# n = int(input("input a number: "))
# print("first", n, "fibonacci numbers")
# print_fibo(n)

# p3


