# Functions.py file module

def add_expense(incomes: list, expenses: list) -> tuple:
    """
    Adds one or more expenses to the expenses list.
    Receives:
        incomes: list of income dictionaries (not modified)
        expenses: list of expense dictionaries (will be updated)
    Returns:
        A tuple: (incomes, updated expenses)
    """
    while True:
        description = input("Enter expense description (or 'q' to quit): ")
        if description.lower() == "q":
            break
        try:
            amount = float(input("Enter expense amount: "))
            expenses.append({
                "amount": amount,
                "description": description
            })
        except ValueError:
            print("Invalid amount. Please enter a number.")
    return incomes, expenses






#def add_expense(incomes: list, expenses: list) -> tuple:
    #return incomes, expenses





#def show_balance(incomes: list, expenses: list) -> tuple:
    #return incomes, expenses






#def show_transaction_history(incomes: list, expenses: list) -> tuple:
    #return incomes, expenses




