#include <bits/stdc++.h>

typedef unsigned long long u64;

std::map<std::pair<u64, u64>, u64> g;

inline u64 gcd(u64 a, u64 b) {
	if (a > b)
		std::swap(a, b);
	auto it = g.find(std::make_pair(a, b));
	if (it == g.end()) {
		u64 n = std::gcd(a, b);
		g[std::make_pair(a, b)] = n;
		return n;
	}
	return it->second;
}

int main() {
	u64 n, a, b;
	scanf("%llu %llu %llu\n", &n, &a, &b);

	u64 i, j, curr;
	u64 *tmp;
	u64 *v1 = (u64 *)malloc(sizeof(u64) * n);
	u64 *v2 = (u64 *)malloc(sizeof(u64) * n);

	for (j = 0; j < n; ++j) {
		v1[j] = 1 + gcd(j+1, b);
		if (j > 0)
			v1[j] += v1[j-1];
	}

	for (i = 1; i < n; ++i) {
		for (j = 0; j < n; ++j) {
			curr = gcd(i+1, a) + gcd(j+1, b);
			if (j == 0)
				v2[j] = v1[j] + curr;
			else
				v2[j] = std::min(v1[j], v2[j-1]) + curr;
		}
		tmp = v1;
		v1 = v2;
		v2 = tmp;
	}

	printf("%llu\n", v1[n-1]);
	return (0);
}
