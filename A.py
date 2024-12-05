n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

s = [(a[i]/b[i], i) for i in range(n)]
s.sort()

c = [0] * n

for _, i in s:
	ai, bi = a[i], b[i]
	tmp = ai // bi
	if tmp > k:
		tmp = k
	k -= tmp
	c[i] = tmp

if k == 0:
	print(' '.join(map(str, c)))
else:
	print(' '.join('0' * n))
