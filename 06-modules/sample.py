# import my_math

# print(my_math.add(1,2))

# from my_package.math import my_math
# from my_package.statistics import tools

# print(my_math.add(1,2))
# print(tools.mod(10,2))



# grade = int(input())
# if grade >= 90:
#     print('A학점')
# elif grade >= 80:
#     print('B학점')
# elif grade >= 70:
#     print('C학점')   
# else:
#     print('D학점')

year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 400) == 0:
    print('윤년입니다.')
else:
    print('윤년이 아닙니다.')