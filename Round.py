a = input().replace(" ", ",").split(",")
b = input().replace(" ", ",").split(",")
ans = 0

if int(b[0]) == 0:
	pass
else:
	ans = ans+1
	for i  in range(1, len(b)):
		if int(b[i]) != 0 and int(b[i]) >= int(b[int(a[1]) - 1]):
			ans = ans+1
		else:
			pass

print(ans)