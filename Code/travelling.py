TC = int(input())

for tc in range(TC):
	n,k,Q = map(int, input().split())
	N = list(map(int, input().split()))
	for q in range(Q):
		is_in = False
		L,H,X = map(int, input().split())
		sub = sorted(N[L-1:H])
		try:
			st_point = sub.index(N[X-1])
			is_in = True
		except ValueError:
			sub.append(N[X-1])
			sub.sort()
			st_point = sub.index(N[X-1])
		left_sub = []
		for i in range(st_point,0,-1):
			try:
				if sub[i] - sub[i-1] <= k:
					left_sub.append(True)
			except:
				break
		for i in range(st_point,len(sub)-1):
			try:
				if sub[i+1] - sub[i] <= k:
					left_sub.append(True)
			except:
				break
		print(len(left_sub)if not is_in else len(left_sub) +1)

