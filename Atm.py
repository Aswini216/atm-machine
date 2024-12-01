class ATM:
    def __init__(self, initial_balance=0, pin="1234"):
        self.balance = initial_balance
        self.pin = pin
        self.transaction_history = []
        self.pin_attempts = 3  # Limit the number of incorrect PIN attempts

    def check_pin(self):
        for attempt in range(self.pin_attempts):
            entered_pin = input("Enter your PIN: ")
            if entered_pin == self.pin:
                return True
            else:
                remaining_attempts = self.pin_attempts - (attempt + 1)
                print(f"Invalid PIN. {remaining_attempts} attempt(s) remaining.")
        print("Too many incorrect attempts. Exiting.")
        return False

    def change_pin(self):
        if self.check_pin():
            new_pin = input("Enter your new PIN: ")
            confirm_pin = input("Confirm your new PIN: ")
            if new_pin == self.pin:
                print("New PIN cannot be the same as the old PIN.")
            elif new_pin == confirm_pin:
                self.pin = new_pin
                print("PIN successfully changed!")
            else:
                print("PINs do not match. Try again.")

    def check_balance(self):
        if self.check_pin():
            print(f"Your account balance is: ${self.balance:.2f}")
            self.transaction_history.append("Balance inquiry")

    def deposit_cash(self):
        if self.check_pin():
            try:
                amount = float(input("Enter the amount to deposit: "))
                if amount > 0:
                    self.balance += amount
                    print(f"${amount:.2f} has been deposited. New balance: ${self.balance:.2f}")
                    self.transaction_history.append(f"Deposited: ${amount:.2f}")
                else:
                    print("Enter a valid amount.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    def withdraw_cash(self):
        if self.check_pin():
            try:
                amount = float(input("Enter the amount to withdraw: "))
                if 0 < amount <= self.balance:
                    self.balance -= amount
                    print(f"${amount:.2f} has been withdrawn. New balance: ${self.balance:.2f}")
                    self.transaction_history.append(f"Withdrew: ${amount:.2f}")
                else:
                    print("Insufficient balance or invalid amount.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    def view_transaction_history(self):
        if self.check_pin():
            if self.transaction_history:
                print("Transaction History:")
                for i, transaction in enumerate(self.transaction_history, start=1):
                    print(f"{i}. {transaction}")
            else:
                print("No transactions to display.")

    def run(self):
        while True:
            print("\nATM Menu:")
            print("1. Balance Inquiry")
            print("2. Deposit Cash")
            print("3. Withdraw Cash")
            print("4. Change PIN")
            print("5. View Transaction History")
            print("6. Exit")
            try:
                choice = int(input("Select an option: "))
                if choice == 1:
                    self.check_balance()
                elif choice == 2:
                    self.deposit_cash()
                elif choice == 3:
                    self.withdraw_cash()
                elif choice == 4:
                    self.change_pin()
                elif choice == 5:
                    self.view_transaction_history()
                elif choice == 6:
                    confirm_exit = input("Are you sure you want to exit? (yes/no): ").strip().lower()
                    if confirm_exit == "yes":
                        print("Thank you for using the ATM. Goodbye!")
                        break
                else:
                    print("Invalid option. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

# Create an ATM instance and start the simulation
if __name__ == "__main__":
    atm = ATM(initial_balance=1000)  # Initial balance set to $1000
    atm.run()
