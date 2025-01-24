# print('hello')

# # 매개변수가 없는 함수로 정의/호출
# def get_sum():
#     num1 = 5
#     num2 = 3
#     return num1 + num2
# result = get_sum()
# print(result)

# # return이 없는 함수로 정의/호출
# def get_sum1(num1, num2):
#     print(num1 + num2)

# result = get_sum1(5, 3) # 8
# print(result) # 함수 자체에 return 값이 없기 때문에 None 반환

# def fire():
#     print('Fire')
# def water():
#     print('>>>')
#     fire()
#     print('<<<')

# fire()
# water()

# def one():
#     for i in range(3):
#         two()
# def two():
#     print('HI')

# one()        

# arr = [1,2,3]
# print(len(arr))

# a = list(map(int, input().split()))

# x= 10 # global scope

# def outer_function():
#     x = 1 #outer_function 입장에서 봤을 때 local scope

#     def inner_function():
#         y = 2 # inner_function 입장에서 봤을 때 local scope
#         result = x + y # inner_function 기준에서 outer_function의 변수 x에 접근 할 수 있는 범위 # enclosed scope

#         print(result) # print 함수가 built-in scope

#     inner_function()

# outer_function()

# def abc():
#     return 1,2,3,4,5

# x = abc()
# print(x)

arr = [1, 2, 3, 4, 5]
# 문제 : 각각의 요소를 제곱해서 arr 출력
result = list(map(lambda i : i ** 2, arr))
print(result)