# a = int(input())
# b = int(input())
# c = int(input())
# if a > b and a > c:
#     print("A cao nhất")
# elif b > a and b > c:
#     print("B cao nhất")
# elif c > a and c > b:
#     print("C cao nhất")
# elif a == b and a > c:
#     print("A và B đều cao hơn C")
# elif b == c and b > a:
#     print("B và C đều cao hơn A")
# elif c == a and c > b:
#     print("C và A đều cao hơn B")
# else:
#     print("A bằng B bằng C")

# a = int(input())
# b = int(input())

# if a < b:
#     c = a
# else:
#     c = b

# for i in range(c, 0, -1):
#     if a % i == 0 and b % i == 0:
#         print(i)
#         break

n = int(input("Độ dài của danh sách: "))
A = []
for i in range(n):
    number = int(input("Khởi tạo các phần tử: "))
    A.append(number)

B = []
for i in range(len(A)):
    if A[i] % 2 == 0:
        B.append(A[i])

for i in range(len(B)):
    print(B[i])