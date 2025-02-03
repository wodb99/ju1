# get
person = {
    'name' : 'sangho',
    'age' : 20,
    'interest' : {'hoby' : 'coomputer', 'invest' : 'bitcoin'}
}

# computer 출력
# print(person['interest']['hoby'])
# # request.get, 딕셔너리의 get 메서드는 다르다
# print(person.get('interest').get('hoby'))

# #print(person.get('height')) # None
# print(person.get('height', 185)) # 185
# print(person)

# # get 메서드와 setdefault 메서드 차이 ?
# # key가 없을 경우 원본 딕셔너리에 추가하는지 안하는지 차이
# print(person.setdefault('height', 185))
# print(person)

# keys, values, items -> for문과 함께 사용
# print(person.keys())
# for key in person.keys():
#     print(key)

# # 리스트의 pop 메서드와 딕셔너리 pop 메서드의 차이 ?
# # 리스트는 인덱스 기준, 딕셔너리는 key 기준
# print(person.pop('age'))
# print(person)

# # 해시테이블

# # update : 자주 사용하지는 않음
# # person['height'] = 185

# other_person = {'height' : 185}
# person.update(other_person)
# print(person)

# 리스트 element 추가 메서드 : append
# 세트 element 추가 메서드 : add

# pop : 임의의 항목 제거, discard : 특정 항목 제거
# 임의의 항목 == 무작위 는 다른말
# 임의의 항목 -> 해시테이블의 순서를 기준으로 

# sequence 타입(list, tuple, string)에는 인덱스가 존재
# set와 dictionary에는 해시테이블이 존재
# 두 차이를 비교했을 때 해시테이블 개념 왜 알아야 ?
# 특징 2가지
# 1. set와 dictionary는 리스트에 비해 성능이 매우 빠르다(검색, 삽입, 삭제)
# 예) set와 dictionary : O(1)
# 예) list : O(n)
# 리스트에서 검색 : 특정값을 찾기 위해서 전체 element 순회
# 리스트에서 삽입 : 중간에 삽입, 뒤로 한 칸씩 밀려남
# 2. set와 dictionary는 중복 허용하지 않음 

# 해시테이블의 해시값
# 1. 정수 : 일정
# 2. 문자 : 난수화
lst = [1, 2, 3, 4, 5]
print(lst[3])
lst.insert(3,6)
print(lst)
