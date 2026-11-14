class LoadWallet:
    # Constructor to initialize wallet attributes
    def __init__(self, owner, mobile_number, starting_balance):
        self.owner = owner
        self.mobile_number = mobile_number
        self._balance = starting_balance  # Protected attribute for encapsulation

    # Method to add load to the wallet
    def top_up(self, amount):
        if amount <= 0:
            print("Invalid amount. Top-up must be greater than P0.00.")
        else:
            self._balance = self._balance + amount
            print(f"New balance: P{self._balance:.2f}")

    # Method to send load to another number on the same network (no fee)
    def send_load(self, recipient, amount):
        if amount <= 0:
            print("Invalid amount. Load amount must be greater than P0.00.")
        elif amount > self._balance:
            print("Insufficient balance.")
        else:
            self._balance = self._balance - amount
            print(f"Successfully sent P{amount:.2f} load to {recipient}.")
            print(f"New balance: P{self._balance:.2f}")

    # Method to send load to a different network with a service fee
    def send_with_fee(self, recipient, amount, fee=2.0):
        total_deduction = amount + fee
        if amount <= 0:
            print("Invalid amount. Load amount must be greater than P0.00.")
        elif total_deduction > self._balance:
            print(f"Insufficient balance (includes P{fee:.2f} service fee).")
        else:
            self._balance = self._balance - total_deduction
            print(f"Successfully sent P{amount:.2f} load to {recipient} (Fee: P{fee:.2f}).")
            print(f"New balance: P{self._balance:.2f}")

    # Method to display wallet details and current balance
    def show_balance(self):
        print(f"Owner         : {self.owner}")
        print(f"Mobile Number : {self.mobile_number}")
        print(f"Balance       : P{self._balance:.2f}")