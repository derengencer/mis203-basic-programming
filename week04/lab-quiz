
balance = float(input("Enter starting balance: "))

while balance < 0:
    print("Starting balance cannot be negative.")
    balance = float(input("Enter starting balance: "))

deposit = float(input("Enter monthly deposit: "))

while deposit <= 0:
    print("Monthly deposit must be positive.")
    deposit = float(input("Enter monthly deposit: "))

rate = float(input("Enter monthly interest rate (%): "))

while rate < 0:
    print("Interest rate cannot be negative.")
    rate = float(input("Enter monthly interest rate (%): "))

goal = float(input("Enter savings goal: "))

while goal <= 0:
    print("Savings goal must be positive.")
    goal = float(input("Enter savings goal: "))

month = 0
total_interest = 0

if balance >= goal:
    print("Savings goal already reached!")
else:
    print("\nMonth | Interest Earned | New Balance")
    print("--------------------------------------")

    while month < 60:
        month += 1

        interest = balance * rate / 100
        balance += interest
        total_interest += interest
        balance += deposit

        print(f"{month:5} | {interest:15.2f} | {balance:11.2f}")

        if balance >= goal:
            break

    if balance >= goal:
        print(f"\nSavings goal reached in {month} months!")
    else:
        print("\nSavings goal not reached within 60 months.")

print(f"Final balance: {balance:.2f}")
print(f"Total interest earned: {total_interest:.2f}")
