t = int(input())
results = []
for test in range(t):
	n = int(input())
	if n < 8:
		results.append("NO")
	else:
		nums = list(map(int, input().split()))
		pos_list = []
		neg_list = []
		minn = min(nums)
		maxx = max(nums)
		if minn < 0:
			minn = 0 - minn
			for i in range(minn + 1):
				neg_list.append(0)
		
		if maxx >= 0:
			for i in range(maxx + 1):
				pos_list.append(0)
		
		for i in nums:
			if i >= 0:
				pos_list[i] += 1
			else:
				i = 0 - i
				neg_list[i] += 1
		max1 = 0
		max2 = 0
		min1 = 0
		min2 = 0
		both_max_found = False
		both_min_found = False
		max1_found = False
		min1_found = False
		for i in reversed(range(len(pos_list))):
			if pos_list[i] >= 4 and not max1_found:
				max1 = i
				max2 = i
				pos_list[i] -= 4
				both_max_found = True
				break
			elif pos_list[i] >= 2 and not max1_found:
				max1 = i
				pos_list[i] -= 2
				max1_found = True
			elif pos_list[i] >= 2:
				max2 = i
				pos_list[i] -= 2
				both_max_found = True
				break
		
		if not both_max_found:
			for i in range(len(neg_list)):
				if neg_list[i] >= 4 and not max1_found:
					max1 = i
					max2 = i
					neg_list[-i] -= 4
					both_max_found = True
					break
				elif neg_list[i] >= 2 and not max1_found:
					max1 = i
					neg_list[-i] -= 2
					max1_found = True
				elif neg_list[i] >= 2:
					max2 = i
					neg_list[i] -= 2
					both_max_found = True
					break

		for i in reversed(range(len(neg_list))):
			if neg_list[i] >= 4 and not min1_found:
				min1 = i
				min2 = i
				neg_list[i] -= 4
				both_min_found = True
				break
			elif neg_list[i] >= 2 and not min1_found:
				min1 = i
				neg_list[i] -= 2
				min1_found = True
			elif neg_list[i] >= 2:
				min2 = i
				neg_list[i] -= 2
				both_min_found = True
				break
		
		if not both_min_found:
			for i in range(len(pos_list)):
				if pos_list[i] >= 4 and not min1_found:
					min1 = i
					min2 = i
					pos_list[i] -= 4
					both_min_found = True
					break
				elif pos_list[i] >= 2 and not min1_found:
					min1 = i
					pos_list[i] -= 2
					min1_found = True
				elif pos_list[i] >= 2:
					min2 = i
					pos_list[i] -= 2
					both_min_found = True
					break
		
		if both_max_found and both_min_found:
			results.append("YES")
			if (max2 - min2) * (max1 - min1) > (max2 - min1) * (max1 - min2):
				results.append(str(min1)+' ' + str(min2)+' ' + str(min1)+' ' + str(max2)+' ' +str(max1)+' ' +str(min2)+' '+str(max1)+' ' + str(max2))
			else:
				results.append(str(min1)+' ' + str(min2)+' ' + str(min1)+' ' + str(max1)+' ' +str(max2)+' ' +str(min2)+' '+str(max2)+' ' + str(max1))
		else:
			results.append("NO")
		

for res in results:
	print(res)
		
		