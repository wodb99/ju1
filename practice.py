a = [1,2,3]
a.append(4)

# 알파벳인지 아닌지 확인(대문자인지 소문자인지)
# 1. 메서드
# 2. 유니코드(아스키코드)
# A 유니코드 : 65, a 유니코드 : 97
# 대문자에 32를 더하면 소문자로 변경가능

# chr1 = 'B'
# chr2 = 'b'

# print(chr(ord(chr1) + 32))
# print(ord(chr2))

# a = 'hello'
# print(a.find('b'))
# print(a.index('b')) # ValueError

# try:
#     print(a.index('b'))
# except:
#     print('찾지 못했습니다.')

# if 'b' in a:
#     print(a.index('b'))
# else:
#     print('찾지 못했습니다.')

# arr = ['a','b','c']
# # 문자열로 출력할 때 두 가지 방법
# # 1. join메서드
# # 2. 언패킹 연산자

# print(' '.join(arr))
# print(*arr)

# append와 extend의 차이 ?
# append는 요소(항목)를 추가할 때
# extend는 iterable 추가할 때
# a = [1, 2, 3]
# 4를 추가할거야 : append
# [4,5,6] 추가할거야 : extend 

# pop() : 마지막 요소 제거하고 반환
# append, pop 알고리즘에서 중요
# stack : 후입선출
# pop(0) -> queue : 선입선출

# arr = [4, 1, 3, 2]
# arr.sort() # 오름차순
# print(arr) 
# arr.sort(reverse=True) # 내림차순
# print(arr)

# #sort와 sorted의 차이 ? (중요)
# #원본을 유지하고 싶은 경우 sorted 즉, 차이점은 반환값이 있는지 없는지

# arr = [4, 1, 3, 2]
# arr2 = sorted(arr)
# print(arr2)

# 얕은복사 : 복사본이 변경되면 원본이 변경
# 깊은복사 : 복사본이 변경되어도 원본이 변경되지 않는다

# 얕은복사
arr1 = [1, 2, 3, [4,5,6]]
arr2 = arr1[:] # 리스트의 1차원 요소만 복사
              # 리스트 안의 리스트 ([4, 5])는 참조(reference)만 복사됨
arr3 = arr1.copy()

arr2[0] = 7
print(arr1) # 원본 변경X
print(arr2) 

arr2[3][0] = 8
print(arr1)  # 원본 변경됨, 중첩된 경우 신경쓰기
print(arr2)