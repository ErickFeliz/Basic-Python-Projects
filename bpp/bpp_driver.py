import bpp_functions

print("Choose a program that you want to run entering the following number associated with the program" , "\n1.Get Month" , "\n2.Prime checker" , "\n3.Gamer Type" , "\n4.Palindrome checker and Cyphering")

user_input = input("Enter:\t")

if user_input == "1":
	bpp_functions.get_month_program()

if user_input == "2":
	bpp_functions.prime_checker_program()
	
if user_input == "3":
	bpp_functions.gamertype_program()

if user_input == "4":
	bpp_functions.palcypher_program()

else:
	print("This number is not associated with any program")
	exit()

	
