import openpyxl
wBook = openpyxl.load_workbook('mydata.xlsx')
sheet = wBook.active
n = int(input('How many records you want to insert: '))
for i in range(n):
	name = input(f'{i+1}. Enter name: ')
	age = input(f'{i+1}. Enter age: ')
	enroll = input(f'{i+1}. Enter Enrollment number: ')
	data = [name, age, enroll]
	sheet.append(data)
	wBook.save('mydata.xlsx')
print('All records inserted successfully !')
