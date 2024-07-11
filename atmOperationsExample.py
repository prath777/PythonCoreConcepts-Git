def deposit(balance, amount):
    if amount > 0:
        balance += amount
        print(f"{amount} deposited successfully.")
    else:
        print("Invalid deposit amount.")
    return balance

def withdraw(balance, amount):
    if 0 < amount <= balance:
        balance -= amount
        print(f"${amount} withdrawn successfully.")
    else:
        print("Invalid withdrawal amount or insufficient funds.")
    return balance

def check_balance(balance):
    print(f"Current balance: ${balance}")

def main():
    balance = 0
    while True:
        print("\nATM Menu")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            balance = deposit(balance, amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            balance = withdraw(balance, amount)
        elif choice == "3":
            check_balance(balance)
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
