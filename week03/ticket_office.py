tickets_sold = 0
total_revenue = 0
free_tickets = 0

while True:
    name = input("Customer name (or q to quit): ")

    if name.lower() == "q":
        break

    age = int(input("Age: "))

    if age < 0 or age > 120:
        print("Invalid age.")
        continue

    day = input("Day (weekday/weekend): ").lower()

    if day != "weekday" and day != "weekend":
        print("Invalid day.")
        continue

    student = input("Student (yes/no): ").lower()

    if student != "yes" and student != "no":
        print("Please answer yes or no.")
        continue

    if day == "weekday":
        base_price = 200
    else:
        base_price = 250

    if age < 6:
        price = 0
        category = "Free"
        free_tickets += 1
    elif age >= 65:
        price = base_price * 0.50
        category = "Senior"
    elif age >= 6 and age <= 12:
        price = base_price * 0.60
        category = "Child"
    elif student == "yes" and age <= 25:
        price = base_price * 0.70
        category = "Student"
    else:
        price = base_price
        category = "Standard"

    print(f"{name}: {price:.2f} TRY ({category})")

    tickets_sold += 1
    total_revenue += price

if tickets_sold == 0:
    print("No tickets sold.")
else:
    average_price = total_revenue / tickets_sold

    print(f"Tickets sold: {tickets_sold}")
    print(f"Total revenue: {total_revenue:.2f} TRY")
    print(f"Average price: {average_price:.2f} TRY")
    print(f"Free tickets: {free_tickets}")
