def withdraw_money(account_balance, amount):
  """Withdraws money from a bank account.

  Args:
    account_balance: The current account balance.
    amount: The amount of money to withdraw.

  Returns:
    The updated account balance.
  """

  if amount > account_balance:
    print("No money")
    return account_balance
  else:
    print("Your money is processed and thanks for visiting the bank")
    return account_balance - amount

# Get the account balance
account_balance = 4000

# Ask the user for the amount to withdraw
amount = float(input("How much money do you want to withdraw? "))

# Withdraw the money and update the account balance
account_balance = withdraw_money(account_balance, amount)

# Print the updated account balance
print("Your remaining account balance is:", account_balance)
