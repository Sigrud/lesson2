classes=[{'school_class': '4a', 'scores': [3,4,4,5,2]},
	{'school_class': '4b', 'scores': [5,4,5,5,2]},
	{'school_class': '4c', 'scores': [3,4,1,3,4]}]


sum=0  
for cl in classes:
	sum1=0
	for a in cl['scores']:
		sum1+=a
		
		c=sum1/len(cl['scores'])
		
	print (f'средняя оценка по классу {cl} = {c}')
	sum+=c
print (f'средняя оценка по школе {sum}')