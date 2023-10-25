#Bank assignment

print ("Welcome to First National Bank in Berlin")
print ("Do you want to withdraw any euros today?")
# amount of money in the bank Account
Amount = 4000

choice = input()
if choice == "no":
	print ("Goodbye and you wont be charged for using this ATM")


elif choice == "yes":
	user_answer = input("How much do you want to withdraw?")

	if int(user_answer) > Amount:
		print ("Insuffcient funds in your account")
	
	print ("Your withdsraw if being processed")
	

		
