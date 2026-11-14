# main.py
# Main menu-driven program for the Cellphone Load Wallet

from load_wallet import LoadWallet


# Helper function to safely get a valid number from the user
def get_amount(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    # Get initial wallet information from the user
    owner = input("Enter owner name: ")
    mobile_number = input("Enter mobile number: ")

    while True:
        starting_balance = get_amount("Enter starting balance: P")
        if starting_balance < 0:
            print("Starting balance cannot be negative.")
        else:
            break

    # Create a LoadWallet object
    wallet = LoadWallet(owner, mobile_number, starting_balance)

    # Keep showing the menu until the user chooses Exit
    while True:
        print("\n----- MENU -----")
        print("1. Top Up Load")
        print("2. Send Load (same network)")
        print("3. Send Load (other network, with fee)")
        print("4. Show Balance")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            amount = get_amount("Enter top-up amount: P")
            wallet.top_up(amount)

        elif choice == "2":
            recipient = input("Enter recipient mobile number: ")
            amount = get_amount("Enter load amount to send: P")
            wallet.send_load(recipient, amount)

        elif choice == "3":
            recipient = input("Enter recipient mobile number: ")
            amount = get_amount("Enter load amount to send: P")
            wallet.send_with_fee(recipient, amount)

        elif choice == "4":
            wallet.show_balance()

        elif choice == "5":
            print("Thank you for using Cellphone Load Wallet. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1 to 5.")


# Start the program
if __name__ == "__main__":
    main()