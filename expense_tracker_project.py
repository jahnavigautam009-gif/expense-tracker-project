expenses = []

try:
    with open("expenses.txt","r") as f:
        for line in f:
            expenses.append(line.strip())

except FileNotFoundError:
    pass

def show_menu():
    print("\n---Expense Tracker---")
    print("1.Add Expense")
    print("2.View Expenses")
    print("3.Total Expenses")
    print("4.Exit")

while True:
    show_menu()
    choice= input("enter your choice:")

    if choice == "1":
        amount=input("enter your amount:")
        category=input("enter category:")
        expenses.append(amount + " " + category)
        print("Expenses Added!")

    elif choice == "2":
        print("\n---Expenses---")
        if len(expenses)==0:
            print("no expenses added yet")
        else :
            for e in expenses:
                print(e)

    elif choice == "3":
        print("\n---Total Expenses---")
        total=0
        for e in expenses:
            amount= e.split()[0]
            total += float(amount)
        print("Total Expenses:",total)

    elif choice == "4":
        with open("expenses.txt","w") as f:
            for e in expenses:
                f.write(e+"\n")
        print("Exiting...Goodbye!")
        break

    else:
        print("Invalid Choice!")


    
    



