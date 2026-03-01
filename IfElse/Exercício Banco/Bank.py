from BankAccount import BankAccount

class Bank:
    """Simple bank manager that holds a list of accounts."""

    def __init__(self, name="Banco Master"):
        self.name = name
        # store instances of bankaccount
        self.accounts: list[BankAccount] = []

    def add_account(self, owner: str, number: str, balance: float = 0.0):
        """Create a new account and append to the list."""
        acct = BankAccount(owner, number, balance)
        self.accounts.append(acct)
        return acct

    def list_accounts(self):
        """Return a list of tuples representing each account."""
        return [(a.owner, a.number, a.balance) for a in self.accounts]

    def find_account(self, number: str):
        """Lookup an account by its number or return None."""
        for a in self.accounts:
            if a.number == number:
                return a
        return None

    def transfer(self, from_number: str, to_number: str, amount: float):
        """Transfer money from one account to another."""
        from_account = self.find_account(from_number)
        to_account = self.find_account(to_number)
        
        if from_account is None:
            print(f"Error: Account {from_number} not found.")
            return False
        if to_account is None:
            print(f"Error: Account {to_number} not found.")
            return False
        if amount <= 0:
            print("Error: Transfer amount must be positive.")
            return False
        if from_account.balance < amount:
            print(f"Error: Insufficient funds. Balance: {from_account.balance}")
            return False
        
        from_account.withdraw(amount)
        to_account.deposit(amount)
        print(f"Transferred {amount} from {from_account.owner} ({from_number}) to {to_account.owner} ({to_number})")
        return True


if __name__ == "__main__":
    # simple interactive demo
    b = Bank()
    b.add_account("Alice", "001", 100.0)
    b.add_account("Bob", "002", 250.0)
    print("Initial Accounts:")
    for o, n, bal in b.list_accounts():
        print(f"{o} ({n}): {bal}")
    
    print("\n--- Transferring 50 from Alice to Bob ---")
    b.transfer("001", "002", 50)
    
    print("\nUpdated Accounts:")
    for o, n, bal in b.list_accounts():
        print(f"{o} ({n}): {bal}")