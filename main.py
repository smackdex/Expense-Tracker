print('--------------Expense Tracker--------------')

import json

def load_expenses():
    try:
        with open('expenses.json', 'r') as file:
            return json.load(file)
    except:
        return []
    
expenses = load_expenses()

def save_expenses(expenses):
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    try:
         user_amount = int(input('Enter amount: '))
         user_category = input('Enter category:\n')
         user_description = input('Enter description:\n')
         
         user_expense = {
               'amount':user_amount,
               'category':user_category,
               'description':user_description
             }
         
         expenses.append(user_expense)
         print('Expense has been added successfully')
         save_expenses(expenses)
    except ValueError:
    
        print('you are not writting the correct input')

    
def view_expenses(expenses):
        if len(expenses) == 0:
            print('empty file')
        else:
            for check in expenses:
                print(check)
        
def total_spending(expenses):
        if len(expenses) == 0:
            return ('empty file')
        total = 0
        for each_amount  in expenses:
            total += each_amount['amount']
        return total

def spending_by_category(expenses):
    if len(expenses) == 0:
        return ('This is an empty list')
    else:
        category = input('what category of your choice:\n').lower()
        category_amount = 0
        for each_set in expenses:
            if each_set['category'] == category:
                category_amount += each_set['amount']
        return category_amount


def delete_expense(expenses):

    if len(expenses) == 0:
        return 'sorry, nothing to delete. The file is actually empty'

    delete = input('what category of expense do you want to delete?\n').lower()

    deleted = False

    for each_expense in expenses.copy():

        if each_expense['category'] == delete:

            expenses.remove(each_expense)
            deleted = True

    if deleted:
        save_expenses(expenses)
        return 'expenses have been successfully deleted'
    else:
        return 'your chosen category is not found'

while True:
    try:
        check = int(input('what do you want to do?\n 1. add expense\n 2. view expenses\n 3. delete expense\n 4. spending by category\n 5. total spending\n 6. Exit\n your answer: '))
        if check == 1:
                add_expense(expenses)
        
        elif check == 2:
                view_expenses(expenses)
        elif check == 3:
                update = delete_expense(expenses)
                print(update)
        
        elif check == 4:
                result = spending_by_category(expenses)
                print(result)
        
        elif check == 5:
                print(total_spending(expenses))
        
        elif check == 6: 
                print('EXIT')
                break
        else:
                print('Chosen number is not in the option')
                
    except ValueError:
          print('sorry you can only use any of those numbers available in the option')
          

         






    


    



   






























