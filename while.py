
b=['Вася','Маша','Петя','Валера','Саша','Даша']
while True:

	a=b.pop(-1)
	if a=='Валера':
		print('Валера нашелся')
		break
	else:
		print(f'Нашелся не Валера, а {a}')

# ---------------------------

answers={'Как дела':'Хорошо','Чем занимаешься':'Программирую',
	'Какой сегодня день?':'Хороший','Давно я сижу?':'Очень)'}

# def get_answer(question,answer):
# 	return (answers.get(question))

def ask_user():
	while True:
		print('программа : есть вопросы? \n')
		a=input('пользователь: ')

		# answer=get_answer(a,answers)
		# print(answer)
		
		if a in answers:
			print(f'программа: {answers[a]}')
			break
		if a=='Пока':
			print('Пока')
			break

if __name__== "__main__":
	ask_user()
