class BankAccount:
    """A simple class representing a bank account to demonstrate basic OOP."""
    
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        # Encapsulating the balance attribute
        self.__balance = balance 

    def deposit(self, amount: float) -> str:
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount:.2f}. New Balance: ${self.__balance:.2f}"
        return "Deposit amount must be positive."

    def withdraw(self, amount: float) -> str:
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount:.2f}. New Balance: ${self.__balance:.2f}"
        elif amount > self.__balance:
            return "Insufficient funds!"
        return "Withdrawal amount must be positive."

    def get_balance(self) -> float:
        return self.__balance


# Example Usage:
if __name__ == "__main__":
    account = BankAccount("Arvinder", 100.0)
    print(account.deposit(50))
    print(account.withdraw(30))
    print(f"Final Balance: ${account.get_balance():.2f}")
