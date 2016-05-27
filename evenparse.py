import numpy as np
import csv
d  = dict()

genre_cnt = 0

genre_d = dict()
with open('genre.cls') as f:
	genre = f.readlines()
	for l in genre:
		if l[0] == '#':
			continue
		ob = l.split('\t')
		front = ob[0]
		after = ob[1].rstrip('\n')
		
		if after not in genre_d:
			genre_d[after] = genre_cnt
			print genre_cnt, after
			genre_cnt += 1
		d[front] = genre_d[after]
