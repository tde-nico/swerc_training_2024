n = int(input())

tot = 0
for _ in range(n):
	event, people = input().split(' ')
	people = int(people)

	if event == 'B':
		if tot < people:
			print('YES')
		else:
			print('NO')
		tot = max(0, tot - people)
	else: # 'P'
		tot += people
