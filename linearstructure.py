'''
n개로 이루어진 정수 집합에서 원하는 수의 위치를 찾는 문제
(단, 입력되는 집합은 오름차순으로 정렬되어 있으며, 같은 수는 없음)

입력:
정수 n 입력 후, n개의 정수를 입력한 후 찾고자 하는 수를 입력하면
그 수의 위치를 찾아주는 프로그램
'''

n = int(input("정수 n 입력 "))
li = []
for i in range(0, n):
    li.append(input("원소 입력, 줄로 구분 "))
print(li)

item = input("찾고자 하는 원소 ")

Position = 0
found = False
counter = 0

while Position < len(li) and not found:
    counter = counter + 1
    if li[Position] == item:
        found = True
    Position = Position + 1

print(counter)
