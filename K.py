from math import gcd as mgcd

n, a, b = map(int, input().split())

v1 = [0] * n
v2 = [0] * n

g = {}
def gcd(a, b):
	if a > b:
		a, b = b, a
	tmp = g.get((a,b), None)
	if tmp is None:
		tmp = mgcd(a, b)
		g[(a,b)] = tmp
	return tmp


for j in range(n):
	v1[j] = 1 + gcd(j+1, b)
	if j > 0:
		v1[j] += v1[j-1]

for i in range(1, n):
	for j in range(n):
		curr = gcd(i+1, a) + gcd(j+1, b)
		if j == 0:
			v2[j] = v1[j] + curr
		else:
			v2[j] = min(v1[j], v2[j-1]) + curr
	v1, v2 = v2, v1

print(v1[-1])



# dp = [[0] * n for _ in range(n)]

# for i in range(1, n+1):
# 	for j in range(1, n+1):
# 		dp[i-1][j-1] = gcd(i, a) + gcd(j, b)

# for i in range(1, n):
# 	dp[0][i] = dp[0][i] + dp[0][i-1]
# for i in range(1, n):
# 	dp[i][0] = dp[i][0] + dp[i-1][0]

# for i in range(1, n):
# 	for j in range(1, n):
# 		dp[i][j] += min(dp[i-1][j], dp[i][j-1])

# print(dp[-1][-1])
