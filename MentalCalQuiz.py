#초 1~2를 위한 두자릿수 암산 훈련

import random
import time
import datetime
import os


#문제를 출제하는 함수
def make_quiz():
    operand1 = random.randint(1, 24)	#1부터 24사이의 임의의 정수 선택
    operand2 = random.randint(1, 24)	#1부터 24사이의 임의의 정수 선택
    operator = random.randint(1, 2)		#덧셈, 뺄셈을 랜덤으로 선택

    x=str(operand1)     #eval함수를 사용하기 위해 str으로 변환
    y=str(operand2)     #eval함수를 사용하기 위해 str으로 변환

    if operator == 1:   #operator가 1이면, 덧셈
       q = x + ' + ' + y
    if operator == 2 and operand1 > operand2:   #operator가 2고, operand1 > operand2면, operand1 - operand2
       q = x + ' - ' + y
    if operator == 2 and operand1 < operand2:   #operator가 2고, operand1 < operand1면, operand2 - operand1
       q = y + ' - ' + x
    if operator == 2 and operand1 == operand2:  #operator가 2고, operand1 = operand1면, operand1 + operand2
       q = x + ' + ' + y
        
    return q


#정답/오답 횟수를 저장한 변수를 초기화
correct = 0  #정답개수
wrong = 0   #오답개수
sum_time = 0    #풀이시간

for i in range(1,21):   #스무 문제 출제
    quiz = make_quiz()  #문제 출제
    print(quiz)			#문제 출력
    start = time.time() #시작 시각 저장
    user = int(input("= ")) #사용자에게 답 입력받고 정수로 변환
    end = time.time()   #마침 시각 저장
    answer = round(eval(quiz), 2) #정답 계산

    print("문제 #", i, "을 푸는데 걸린 시간 :", round(end-start, 2), "초") #각 문제 푸는데 걸린 시간
    sum_time = sum_time + end - start #전체 시간 계산
    
    if (user == answer):    #정답 확인
        print("정답!")
        correct = correct+1 #정답개수 저장
    else:
        print("오답!",">> 정답:",answer)
        wrong = wrong+1     #오답개수 저장


print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
print("정답 :", correct, "/ 오답 :", wrong)
print("모든 문제를 푸는데 걸린 시간 :", round(sum_time,2), "초")

if(wrong == 0):     #100점일 때,
	print("훌륭해요!") 
if(wrong <= i*0.1): #90점일 때,
    print("잘했어요!")
if(wrong <= i*0.2): #80점일 때,
    print("더 열심히 해봐요!")
if(wrong > i*0.2): #80점일 때,
    print("화이팅! 포기하지 마세요!")
    
os.system('pause')