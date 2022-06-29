# 1~24의 정수 2개를 임의로 선택 후 덧셈
# 1~24의 정수 중 1개 1~10의 정수 중 1개를 임의로 선택 후 큰 수에서 작은 수 뺄셈

import random
import datetime
import time

starttime=time.time() #시작한 시각 저장
count=0

while count<20:
    
    x=random.randint(1,24)
    y=random.randint(1,24)
    f=x+y    
    print("( 문제 #",count+1,") ",x,"+",y,'=')
    answer = int(input())
    
    if(answer==f):
        print("<O>")        
    else:
        print("<X>")      
    count=count+1

endtime=time.time() #마친 시간 저장
print("시작한 시각:",starttime)
print("마친 시각:",endtime)
print("걸린 시간:",endtime-starttime)