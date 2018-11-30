age  = int(input('введите ваш возраст '))

def doing(age):
	if age<7:
		print('ты должен ходить в садик')
	elif age<17:
		print('ты должен учиться в школе')
	elif age<23:
		print('ты должен учиться в ВУЗе')
	else:
		print('пора бы уже и работать')
	print(f'тебе {age}')
doing(age)