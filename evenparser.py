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
			genre_cnt += 1
		d[front] = str(genre_d[after])
		if len(ob) > 2:
			second = ob[2].rstrip('\n')
			if second not in genre_d:
				genre_d[second] = genre_cnt
				genre_cnt += 1
			d[front] += ' '
			d[front] += str(genre_d[second])
for k, v in genre_d.items():
	print k, v

name = dict()
gcount = dict()
with open("mxm_dataset_train.txt", "r") as dataset:
	cnt = 0
	m = dict()
	for line in dataset:
		if line[0] == '#' or line[0] == '%':
			continue
		tokens = line.split(',')
		if tokens[0] not in d:
			continue
		f = tokens[0]
		genre_indices = d[f].split(' ')
		for i in range(len(genre_indices)):
			genre_idx = int(genre_indices[i])
			if genre_idx == 3 or genre_idx == 6 or genre_idx == 11:
				continue
			if genre_idx not in gcount:
				gcount[genre_idx] = 0
			if gcount[genre_idx] > 1000:
				continue
			gcount[genre_idx] += 1 
			haha = [0] * 5001
			m[cnt] = haha
			name[cnt] = tokens[0]
			filename = tokens[0]
			m[cnt][0] = d[filename]
			for token in tokens:
				keyval = token.split(':')
				if len(keyval) < 2:
					continue
				key = int(keyval[0])
				val = int(keyval[1])
				if key > 5000:
					print "error detected on line", cnt, "with key", key
					continue
				m[cnt][key] = val
			cnt += 1
			if cnt % 1000 == 0:
				print cnt
	f = open('uniform_data.csv', 'wb')
	f2 = open('name_mapping.txt','wb')
	writer = csv.writer(f)
	for key,value in m.items():
		f2.write(str(key) + ',' + name[key] + '\n')
		writer.writerow([val for val in value])
		
		
		
	print "total count", cnt
for k, v in gcount.items():
	print k, v
		
		
