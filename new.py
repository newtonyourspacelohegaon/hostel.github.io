
t = int(input())
for i in range(t):
    n = int(input())
    money = list(map(int,input().split()))
    money.sort()
    totalmoeny = 0
    for j in money:
        totalmoeny += j
    halfmo = (totalmoeny/n)/2
    halfper = (n//2)
    a = ((money[halfper]*n*2)-totalmoeny)+1
    if a < 18:print(-1)
    else: print(a)