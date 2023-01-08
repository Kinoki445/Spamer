#Кликер 
from time import sleep   
import keyboard as key
import pyautogui as auto
import random, string

def random445(amount, file, s):
	value = 1
	while value <= amount:
		code = ('').join(random.choices(string.ascii_letters + string.digits, k=s)) # k = числу символов
		f = open(file, "a+", encoding= 'UTF-8')
		f.write(f'{code}\n')
		f.close()
		value += 1

def spam2(pings,file):											# Функция для того чтобы весь текст в файле text.txt отправлялся автоматически
    sleep(pings)											    
    text = open(file, encoding = 'UTF-8')
    for line in text:
        auto.typewrite(line)									# Автоввод текста
        auto.press('enter')										# Автопрожатие кнопки enter для отправки
        sleep(pings)
    auto.typewrite('/clear 20 ')								# Автоматически вводит /clear для того чтобы удалять все сообщения которые отправились (локальная тема для дискорда)
    auto.press('enter')											# Автопрожатие кнопки enter для отправки

def spam(pings,word):               							# Функция для спама текстом который вводит пользователь.
    sleep(pings)					
    auto.typewrite(word)										# Автоввод текста
    auto.press('enter')											# Автопрожатие кнопки enter для отправки

def clicker(pings):												# Функция для кликов мышки
	sleep(pings)		
	auto.tripleClick()											# Делает автотрипил клик

def funcspam2(trigger,run,ping,word):
		while trigger:
			while run:
				if key.is_pressed ( start_key ):				# Кнопка для запуска кликера
					print ('Кликер запущен')
					while run:
						spam(ping,word)
						if key.is_pressed ( pause_key ):		# Кнопка для остановки кликера
							print('Кликер остановлен')
							run = False							# После прожатия кнопки цикл run приостонавливается и спам прекращается(только в случае когда пользователь ввёл сам текст, из из text.txt кликер не прекратиться нужна для этого функция, но она не прописывается номарльно)
			if key.is_pressed ( start_key):																																																											
				run = True										# run == True и кликер снова работает
			elif key.is_pressed(stop_key):
				print ('Кликер выключен')
				trigger = False									# Триггер полностью отключает работу цикла и закрывает программу
				break

def funcspam(trigger,run,ping,file):
		while trigger:
			while run:
				if key.is_pressed ( start_key ):				# Кнопка для запуска кликера
					print ('Кликер запущен')
					while run:
						spam2(ping, file)
						if key.is_pressed ( pause_key ):		# Кнопка для остановки кликера
							print('Кликер остановлен')
							run = False							# После прожатия кнопки цикл run приостонавливается и спам прекращается(только в случае когда пользователь ввёл сам текст, из из text.txt кликер не прекратиться нужна для этого функция, но она не прописывается номарльно)
			if key.is_pressed ( start_key):																																																											
				run = True										# run == True и кликер снова работает
			elif key.is_pressed(stop_key):
				print ('Кликер выключен')
				trigger = False									# Триггер полностью отключает работу цикла и закрывает программу
				break

def funcClicker(trigger):
		while trigger:
			while run:
				if key.is_pressed ( start_key ):
					print ('Кликер запущен')
					while run:
						clicker(ping)
						if key.is_pressed ( pause_key ):
							print('Кликер остановлен')
							run = False
			if key.is_pressed ( start_key):
				run = True
			elif key.is_pressed(stop_key):
				print ('Кликер выключен')
				trigger = False
				break

trigger = True
run = True
sub_trigger = 1
trigger_for_action = True

while trigger_for_action:
	try:
		if sub_trigger == 1:
			action = int(input('Мышка или Клавиатура? | 1:2 | :  '))
			sub_trigger += 1
		if sub_trigger == 2:
			start_key = input ('Клавиша запуска: ')
			sub_trigger += 1
		if sub_trigger == 3:
			pause_key = input ('Клавиша паузы: ')
			if pause_key == start_key:
				print('Клавиши не могут повторяться, введите снова!')
				sub_trigger = 3
			else:
				sub_trigger += 1
		if sub_trigger == 4:
			stop_key = input ('Клавиша выключения программы: ')
			if stop_key == pause_key or stop_key == start_key:
				print('Клавиши не могут повторяться, введите снова!')
				sub_trigger = 4
			else:
				sub_trigger += 1
		if sub_trigger == 5:
			ping = float(input('Введи задержку нажатия: '))
			sub_trigger += 1
		trigger_for_action = False
	except ValueError:
		print('Ты ввёл не верные данные, попробуй ещё раз')


if action == 2:
	trigger445 = True
	words = str(input ('Введи текст для спама или используй текстовый файл, командой (My file): '))
	trigger_for_action2 = True
	while trigger_for_action2:
		try:
			inpunt_random445 = int(input('Так же вы можете сделать файл с рандомными символами, с помощью команды Yes|No(1|2): '))
			trigger_for_action2 = False
		except ValueError:
			print('Ты ввёл не верные данные')
	trigger_for_action3 = True
	if words == ('my file'):
		while trigger_for_action3:
			try:
				file = input('Напиши название и формат файла: ')
				text = open(file, encoding='UTF-8')
				trigger_for_action3 = False
			except ValueError:
				print('Ты ввёл не верный файл. \n Файл должен находиться в одной папке с программой!!!')
		

		if inpunt_random445 == 1:
			k = int(input('Количество символов: '))
			amount = int(input('Укажите количество кодов для генерации: '))
			random445(amount,file,k)
			print('Файл изменён!\nНажми кнопку', start_key, 'и кликер запуститься.')
		elif inpunt_random445 == 2:
			trigger_for_action = False
			print('Вы отказались от измены файла\nНажми кнопку', start_key, 'и кликер запуститься.')
					

		while trigger445:
			funcspam(trigger,run,ping,file)
			if key.is_pressed ( pause_key ):
				trigger445 = False								# Кнопка для остановки кликера
			print('Кликер остановлен')
		if key.is_pressed ( start_key):																																																											
			trigger445 = True
	else:
		funcspam2(trigger,run,ping,words)



elif action == 1:											# Всё тоже самое только кликер мышки
					funcspam()					

