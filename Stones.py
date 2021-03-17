n = int(input())
stones = input()
ans = 0

for i in range(1, n):
    if stones[i-1] == stones[i]:
        ans = ans + 1
    else:
        pass
    
print(ans)