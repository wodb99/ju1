# class SetMenu: # 클래스 정의
#     def __init__(self): # 생성자
#         self.sanghi = 4500 # 필드
#         self.bigmac = 4200

#     def eat(self): # 메서드
#         print('햄버거 주문하기')
#         print(f'{self.sanghi + self.bigmac}원 입니다.')

# mc = SetMenu()
# mc.eat()

# class Zergling:
#     def __init__(self):
#         self.hp = 20
#         self.mana = 50

#     def run(self):
#         print('뛴다')
#         self.hp -= 1
#         self.mana += 1

#     def show_stats(self):
#         print(f'HP : {self.hp}')
#         print(f'MANA : {self.mana}')


# z1 = Zergling() # 인스턴스 생성
# z2 = Zergling()

# z1.run()
# z1.show_stats()

# for i in range(5):
#     z2.run()
# z2.show_stats()

# a = 3 # 3은 객체, a는 변수, 할당
# b = [1, 4, 2, 5, 4] # []는 객체, b는 변수, 할당
# c = SetMenu() #객체(SetMenu라는 인스턴스 하나), SetMenu()는 객체, c는 변수, 할당
# a = 15 # 15는 객체, a는 변수, 재할당(할당)
# b[3] = 2 # b[3]은 인덱싱 element(요소), 할당x, 2는 객체x(리스트 안에 값을 할당하는 것이므로 독립적인 개체는 아님)
#                                                     할당의 개념에서 객체가 아닌 것..?
# a = SetMenu() # SetMenu()는 객체, a는 변수, 재할당(할당)
# # 변수의 개수 : 3개
# # 객체의 개수 : 4개
# # 할당 횟수 : 5번

a = 3
b = 3 # 객체는 하나..?

class GameMachine:
    def __init__(self): # 필수는 아니다..?
        self.coin = 0

    def input_coin(self,coin_num):
        # 코인은 5개까지만, 10 초과할 수 없음
        if coin_num > 5:
            return
        
        if self.coin + coin_num > 10:
            return
        
        self.coin += coin_num

    def play_game(self):
        if self.coin < 1:
            print('코인을 넣어주세요')
            return
        
        self.coin -= 1
        print('게임 재밌다')

    def show_status(self):
        print(f'남아있는 코인은 {self.coin} 입니다.')

gm = GameMachine()
gm.input_coin(2)
gm.show_status()
gm.play_game()
gm.show_status()

class Student:
    # 클래스 변수
    total_students = 0
    # 생성자 함수
    def __init__(self, name, grade):
        # 왼쪽 name : 인스턴스 변수, 오른쪽 name : parameter
        self.name = name
        self.grade = grade
        Student.total_students += 1
    