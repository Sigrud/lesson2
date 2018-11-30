one=input('введите первый агрумент: \n')
two= input('введите второй аргумент: \n')

def get_sum(num_one,num_two):
	try:
		return(int(num_one)+int(num_two))
	except (TypeError,ValueError):
		print('введено неверное значение или тип агрументов')
		
print(get_sum(one,two))