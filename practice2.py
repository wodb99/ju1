# a = 10 #할당
# print(id(a))
# a = 50 #재할당
# print(id(a))

# #할당과 재할당에서 메모리 주소는 다르다.

# arr = [1,5,4,7]
# a = arr[len(arr)-1]
# a = arr[-1]

# arr1 = [1,5,2,7,3,6]
# print(arr1[0], arr1[-1])
# print(arr1[::2])
# print(arr1[3:])

# a, b = 1, 2
# c, d = (1, 2)

# print(type(a))
# print(type(d))


# a = 1,2,3
# a = 1,2,3
# print(type(a))
# print(a)

# my_dict_3 = {}
# my_dict_3 = dict() # a = set()

# my_dict_3['apple'] = 12
# my_dict_3['list']= [1,2,3]

# print(my_dict_3)

# d = dict()
# d['HI'] = [1,2,3,"KFC1"]
# d['OH'] = [1,5,{"HO":14, "MY":119, "qq":'KFC2'}]
# d[-153] = [(1,2,(5,6,"KFC3"))]

# print(d['HI'][3])
# print(d['OH'][2]['qq'])
# print(d[-153][0][2][2])

# a = ''
# b = None

# print(type(a))
# print(type(b))

# a = 10
# b = 5

# # print(a >= b) #항상 부등호 먼저

# a = [1,2,3]  # 두 개는 다른 객체 > 메모리 주소가 다르기 때문에
# b = [1,2,3]

# print(id(a)) 
# print(id(b))
# #다른 객체이기 때문에 False
# print(a is b)

# b = a
# print(id(a)) 
# print(id(b))
# #같은 객체이기 때문에 True
# print(a is b)

a = (1, )
print(type(a))

