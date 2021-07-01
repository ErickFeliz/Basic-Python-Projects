def get_month_program():
	while True:
	
		month = {	
		'1':'January',
		'2':'February',
		'3':'March',
		'4':'April',
		'5':'May',
		'6':'June',
		'7':'July',
		'8':'August',
		'9':'September',
		'10':'October',
		'11':'November',
		'12':'December'		}
			
		print('Enter a number from 1 to 12 to get a month with its related number.')
		
		key = input('Type a number:')
		
		if key in month:
			print('The month is', month[key])
		else:
			print('You entered a wrong value')
			
def prime_checker_program():
	while True:

		givennum = int(input("Enter a number: "))
	

		for i in range(2, givennum):
			if (givennum % i) == 0:
				print(givennum , "Is not a prime number")
				break
		else:
			print(givennum , "Is a prime number")
	
def gamertype_program():
	class gamer ():
		username = ''
		gamer_type = ''
		gaming_system = ''
		hour_play = ''
	
		def __init__(self):
			self.username = input("What is your username?\t")
			self.gamer_type = input("What type of gamer are you?\t")
			self.gaming_system = input("In what system do you play on?\t")
			self.hour_play = input("How many hour do you spend on games per day?\t")
			
	player = gamer()
	
	print("---------------------------""\nThe username is:" , player.username , "\nThe gamer type is:" , player.gamer_type , "\nThe system the play on is:" , player.gaming_system , "\nThey play" , player.hour_play , "per day")

def palcypher_program():
	def palindrome_checker(string):
	 
		# Start from leftmost and rightmost corners of str
		l = 0
		h = len(string) - 1
	 
		# Keep comparing characters while they are same
		while h > l:
			l+= 1 
			h-= 1
			if string[l-1] != string[h + 1]:
				return False
	 
		# If we reach here, then all characters were matching   
		return True

	#ERICKCYPHER converter function

	def ERICKCYPHER(plain_text):
		cypher_text = ''
		length = len(plain_text)
		
		for l in plain_text:
			cypher_char = chr(ord(l)+(length**2))
			
			cypher_text += cypher_char
		
		return cypher_text
		
	def unERICKCYPHER(cypher_text):
		plain_text = ''
		length = len(cypher_text)
		
		for l in cypher_text:
			plain_char = chr(ord(l)-(length**2))
			
			plain_text += plain_char
			
		return plain_text

	#entry point of the program
	while True:
		user_input = input('Please input a word:\t')
		if(palindrome_checker(user_input)): 
			print('Yes, it is palindrome')
		else:
			print('It is not palindrome')
		print(ERICKCYPHER(user_input))
		
		print(unERICKCYPHER(ERICKCYPHER(user_input)))
