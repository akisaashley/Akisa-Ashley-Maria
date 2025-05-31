class Transaction:
    def deposit(self, amount, currency="USD"):
        return f"Deposited {amount} in {currency}"

t = Transaction()
print(t.deposit(100))             
print(t.deposit(200, "EUR"))     
