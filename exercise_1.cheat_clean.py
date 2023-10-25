def withdraw_money(account_balance, amount):
  """Withdraws money from a bank account.

  Args:
    account_balance: The current account balance.
    amount: The amount of money to withdraw.

  Returns:
    The updated account balance.
  """

  if amount > account_balance:
    raise ValueError("Insufficient balance")

  account_balance -= amount
  return account_balance


# Get the account balance
account_balance = 4000

# Ask the user for the amount to withdraw
amount = float(input("How much money do you want to withdraw? "))

try:
  # Withdraw the money and update the account balance
  account_balance = withdraw_money(account_balance, amount)
except ValueError as e:
  # Handle insufficient balance error
  print(e)
else:
  # Print the updated account balance
  print("Your remaining account balance is:", account_balance)