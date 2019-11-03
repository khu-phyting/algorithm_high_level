# 9*9 행렬에 81개의 자연수가 주어질 때,
# 이들 중 최댓값을 찾고 그 최댓값이 몇 행 몇열에 위치한 수인지 구하는 프로그램
import numpy as np
import random as rd
list = []
array= np.empty((9,9))
for i in range(1,82):
    number = rd.randint(1,100)
    list.append(number)
c = 0
an=0
bn=0
for a in range(9):
    for b in range(9):
        array[a][b] = list[c]
        c= c+1
        if array[a][b] == max(list):
            an=a+1
            bn=b+1
print(array)
print(max(list))
print(an)
print(bn)

