answers={'Как дела':'Хорошо','Чем занимаешься':'Программирую',
	'Какой сегодня день?':'Хороший','Давно я сижу?':'Очень)'}

def ask_user():
	while True:
		try:
			print('программа : есть вопросы? \n')
			a=input('пользователь: ')		
			if a in answers:
				print(f'программа: {answers[a]}')
				break
			if a=='Пока':
				print('Пока')
				break
		except (KeyboardInterrupt):
			print('принудительный выход из программы')
			break

ask_user()