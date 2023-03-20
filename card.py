#!/usr/bin/python3
import random, time, os

#sololearn bin = 5235915354xxxxxx
try:
	from colorama import Fore
	from credit_card_checker import CreditCardChecker as ccc

	f = Fore
	r = f.RED
	y = f.YELLOW
	g = f.GREEN
	b = f.BLUE

	def menu():

		print(f"""{b}
   ____________   ______                           __
  / ____/ ____/  / ____/__  ____  ___  _________ _/ /_____  _____
 / /   / /      / / __/ _ \/ __ \/ _ \/ ___/ __ `/ __/ __ \/ ___/
/ /___/ /___   / /_/ /  __/ / / /  __/ /  / /_/ / /_/ /_/ / /
\____/\____/   \____/\___/_/ /_/\___/_/   \__,_/\__/\____/_/
Created by: RoPaDoPe
|-------------------------------|
~~~~~[+]{b}Are YoU a Wizzard Hairy?{y} [+]~~~~~~

CHOOSE ONE OF THE FOLLOWING OPTIONS

!!!!. Zero Fucks GiVen .!!!!!

[1] Amazon Primec CC
[2] HBO MAX CC
[3] Netflix and Chill CC
[4] CC-checker(not ready yet)
[0] Fuck This im Leaving
[000] === I am not Responsible for your stupidity

THIS TOOL WAS MADE FOR EDUCATIONAL PURPOSES ONLY

|-------------------------------|
""")


	def generator(bin):

		numbers = '1234567890'
		yyyy = ["2022","2023","2024","2025","2026","2027","2028",]
		mm = ["01","02","03","04","05","06","07","08","09","10","11","12",]

		print("How many cc to generate")
		ui = int(input("Enter any Value: "))
		amount = 0
		while amount != ui:
			y_r = random.choices(yyyy)
			y_j = ''.join(y_r)
			m_r = random.choices(mm)
			m_j = ''.join(m_r)
			cvv_r = random.choices(list(numbers), k=3)
			cvv_j = ''.join(cvv_r)
			cc_r = random.choices(list(numbers), k=5)
			cc_j = bin+''.join(cc_r)
			check = ccc(cc_j).valid()
			if check == True:
				amount +=1
				print(f"{cc_j}|{m_j}|{y_j}|{cvv_j}")
				time.sleep(.1)



	def main():
		menu()
		while True:

			print(f'{b}┌──({y}i got you)-[~/LIVE]')
			ui = input(f"{r}└─>->>{g} ")
			if ui == '1':
				bin = '45101560210'
				generator(bin)

			elif ui == '2':
				bin = '52215801230'
				generator(bin)

			elif ui == '3':
				bin = '52215800230'
				generator(bin)

			elif ui == '4':
				for i in range(10):
					print(f"{y}Not Today Jack!")
					time.sleep(.1)

			elif ui == '000':
				os.system("Catch Yall Hoes Later")

			elif ui == '0':
				os.system("clear")
				break
			elif ui =='-h' or ui == 'help':
				menu()

			else:
				os.system(ui)


	main()


except ImportError as imerr:
	print("Some python modules are/is not installed!\n Enter root password to grant us permission to auto install this required modules!")
	os.system('sudo pip3 install colorama; sudo pip3 install credit_card_checker')
