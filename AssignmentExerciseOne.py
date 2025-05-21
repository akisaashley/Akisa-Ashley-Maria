# ATM Withdrawal Program

account_balance = 5000.0  # You can set this as your initial balance

withdraw_amount = float(input("Enter amount to withdraw: "))
5
if withdraw_amount <= 0:
    print("Withdrawal amount must be greater than 0.")
elif withdraw_amount > account_balance:
    print("Insufficient funds. Transaction denied.")
else:
    account_balance -= withdraw_amount
    print(f"Withdrawal successful! Your new balance is: ${account_balance:.2f}")
