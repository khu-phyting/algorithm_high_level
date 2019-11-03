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
