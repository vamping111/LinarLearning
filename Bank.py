PIN = input ("Здравствуйте! Введите ПИН-код вашей карты!\n")
Balance = 7000
if int(PIN) == 8504:
	print ("Вы можете воспользоваться услугами нашего банкомата!\n")
	while True:
		print (" 1. Просмотреть баланс\n", "2. Пополнить баланс\n", "3. Снять деньги\n")
		Menu = input ("Введите пункт меню >>> ")
		if int(Menu) == 1:
			print (Balance)		
		elif int(Menu) == 2:
			Plus = input ("Введите сумму пополнения >> ")
			Balance = Balance + int(Plus)
			print ("Ваш счет составляет - ",Balance)	
		elif int(Menu) == 3:
			Minus = input ("Введити сумму снятия >> ")
			Balance = Balance - int(Minus)
			if int(Minus) <= Balance:
				print ("На вашем счету осталось - ",Balance)
			elif int(Minus) > Balance:
				Balance = Balance + int(Minus)
				print ("На вашем счете недостаточно средств")
		else:
			print ("Введенн неверный пункт меню")
		continue
else:														 
	print ("Неверный ПИН-код!")
