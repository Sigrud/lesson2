

str1 =input('введите первую строку ')
str2 =input('введите вторую строку ')
# str1="2"
# str2="8"

def strings(str1,str2):
	if type(str1 and str2)==str:
		
		if str1==str2:			
			return (1)

		elif len(str1)>len(str2):
			return(2)
		elif str2=='learn':
			return (3)

		return(0)
print(strings(str1,str2))




# if type(str1 and str2)==str:
# 	# print(strings(str1,str2))
# 	print('0')