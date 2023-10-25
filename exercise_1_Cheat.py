account_balance = 4000

def withdraw_money(amount):
  if amount > account_balance:
    print("No money")
  else:
    account_balance -= amount
    print("Your money is processed Thanks")

# Ask the man how much money he wants to withdraw
amount = int(input("How much money do you want to withdraw? "))

# Withdraw the money
withdraw_money(amount)

# Print the updated account balance
print("Your remaining account balance is:", account_balance)
