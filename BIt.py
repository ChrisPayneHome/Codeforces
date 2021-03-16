lines = int(input())
n = 0

for i in range(0, lines):
    op = input()
    if op == "X++" or op == "++X":
        n = n + 1
    elif op == "--X" or op == "X--":
        n = n - 1

print(n)