t = int(input())

for _ in range(t):
	s = input()
	n1, op, n2 = int(s[0]), s[1], int(s[2])
	if op == '>':
		if n1 > n2:
			print(s)
		elif n1 < n2:
			print(n1,'<',n2,sep='')
		else:
			print(n1,'=',n2,sep='')
	elif op == '<':
		if n1 < n2:
			print(s)
		elif n1 > n2:
			print(n1,'>',n2,sep='')
		else:
			print(n1,'=',n2,sep='')
	elif op == '=':
		if n1 == n2:
			print(s)
		elif n1 < n2:
			print(n1,'<',n2,sep='')
		else:
			print(n1,'>',n2,sep='')
