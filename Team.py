ln = int(input())
n = 0

for i in range(0, ln):
    prblm = int(str(input()).replace(" ", ""))
    if prblm >= 101 or prblm == 11:
        n = n+1
    else:
        pass

print(n)