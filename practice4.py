# arr = ['0'] * 5
# value = 5

# for i in range(5):
#     arr[i] = value
#     value += 1

# # iterator 방식으로 순회
# # for num in arr:
# #     print(num, end=' ')

# print(*arr) # 언패킹

# iterator 방식으로 순회 하면서 모든 요소의 합계 출력
# sum() 내장함수 사용금지

# 1. 모든 요소의 합계 출력
# arr = [1, 5, 3, 4, 4, 2]
# count = 0

# for i in arr:
#     count += i
# print(count)

# # 2. 최댓값 출력
# max_val = 0
# for j in arr:
#     if max_val < arr[j]:
#         max_val = arr[j]
# print(max_val)

# def input_num():
#     a, b = map(int, input().split())
#     return a, b


# def output_num():

#     a, b = input_num()

#     for i in range(a, b+1):
#         print(i, end = ' ')

# output_num()

# a = [3, 3, 2, 6, 2]
# bucket = [0] * 7 # 인덱스를 활용(1부터 6이니까 6+1 = 7)
# for i in a:
#     bucket[i] += 1

# for i in range(1, 7):
#     print(str(i) + ':' + str(bucket[i]) + '개')

arr = ['MC','BTS','MC','BTS','BTS']


di = dict()

# for i in arr:
#     di[i] = 0

# for i in arr:
#     di[i] += 1 # key에 해당하는 value를 1씩 카운팅

# print(di)

arr = ['MC','BTS','MC','BTS','BTS']

di = dict()
for i in arr:
    di[i] = 0

for i in arr:
    di[i] += 1

# max_count = 0
# for i in di.values():
#     if max_count < i:
#         max_count = i

# list_val = list(di.values())
# index_val = list_val.index(max_count)
# list_name = list(di.keys())
# print(list_name[index_val])

# di.keys() : key, di.values() : value, di.items() : key, value 둘 다
# max_cnt = 0
# result = ''
# for key, value in di.items():
#     if value > max_cnt:
#         max_cnt = value
#         result = key # 최댓값을 가진 value로 가진 key가 result에 할당
        
# print(result)

# arr = [1,2,3,4,5]
# for i in arr:
#     if i == 3:
#         break

# for i in range(2):
#     for j in range(3):
#         print('#', end = '')
#     print()

# 2차원 리스트
T = int(input())
arr = []
for tc in range(1, T+1):
    row = list(map(int, input().split()))
    arr.append(row)
print(arr)

# 파이써닉하게 리스트컴프리헨션 써서 소스코드 작성
T = int(input())
arr = [list(map(int, input().split())) for _ in range(T)]       
print(arr)