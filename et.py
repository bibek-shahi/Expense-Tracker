import os
import sys
import datetime
import json


#initializing data

is_valid = False
ids=0
date = str(datetime.date.today())
month=''
description=''
amount=0
value=''#for updating values

expenses=[]

highest_id=1

total_expenses=0

#Opening File and creating file


if 'expenses.json' in os.listdir():
    with open('expenses.json') as f:
        expenses = json.load(f)
else:
    with open('expenses.json', 'w') as f:
        empty_list= []
        json.dump(empty_list,f)


#Checking id
for expense in expenses:
    if expense['id']>=highest_id:
        highest_id = expense['id']+1


#User input Filtering


if  len(sys.argv) in range (2,7):
    if sys.argv[1] == "add":
        if len(sys.argv) == 6:
            if (sys.argv[2] == "--description") and (sys.argv[4] == "--amount"):
                if sys.argv[5].isdigit():

                    description = sys.argv[3]
                    amount = sys.argv[5]

                    is_valid = True


                else:
                    print("Amount entered is a not a number")
            else:
                print("Invalid command . Command must be --description or --amount")


        else:
            print(f"Invalid command the length is {len(sys.argv)} should be 6")
    elif sys.argv[1] == "update":
        if len(sys.argv) == 5:
            if sys.argv[2].isdigit():
                ids = int(sys.argv[2])
                if sys.argv[3] == "--description":
                    value = sys.argv[4]
                    is_valid = True

                elif sys.argv[3] == "--amount":
                    if sys.argv[4].isdigit():
                        value = int(sys.argv[4])
                        is_valid = True

                        # print(value)
                    else:
                        print("Amount entered is a not a number")
                else:
                    print("Invalid command . Command must be --description or --amount")
            else:
                print("ID entered is a not a number")


        else:
            print(f"Invalid command the length is {len(sys.argv)} should be 5")
    elif sys.argv[1] == "delete":
        if len(sys.argv) == 4:
            if sys.argv[2] == "--id":

                if sys.argv[3].isdigit():
                    ids=int(sys.argv[3])
                    is_valid = True
                else:
                    print("ID entered is a not a number")
            else:
                print("Invalid command . Command must be --id")
        else :
            print(f"Invalid command the length is {len(sys.argv)} should be 4")
    elif sys.argv[1] == "list":
        if len(sys.argv) == 2:
            is_valid = True

        else:
            print(f"Invalid command the length is {len(sys.argv)} should be 2")
    elif sys.argv[1] == "summary":
        if len(sys.argv) == 4:
            if sys.argv[2] == "--month":
                if sys.argv[3].isdigit():
                    month = sys.argv[3]
                    is_valid = True
                else:
                    print("Month entered is a not a number")
            else:
                print("Invalid command. Command only available for '--month'")
        elif len(sys.argv) == 2:
            is_valid = True

        else:
            print(f"Invalid command the length is {len(sys.argv)} should be 2 or 4")
    else:
        print("Invalid command")

else:
    print("Invalid length of arguments")




#Logic and updating


if (sys.argv[1] == "add") and is_valid:
    tran_dict=dict(id=highest_id,date=date,description=description,amount=amount)
    expenses.append(tran_dict)
    with open('expenses.json','w') as f:
        json.dump(expenses,f,indent=4 )
    print(f"Expense added with description:{description} and  amount: {amount}  successfully. ")
elif (sys.argv[1] == "update") and is_valid:
    if len(expenses) == 0:
        print("No item expenses list")
    else:
        if sys.argv[3] == "--description":
            for expense in expenses:
                if expense['id'] == ids:
                    expense['description'] = value
                    with open('expenses.json', 'w') as f:
                        json.dump(expenses, f, indent=4)
                    print(f"Expense id {ids} description updated successfully to {value} ")
        elif sys.argv[3] == "--amount":
            for expense in expenses:
                if expense['id'] == ids:
                    expense['amount'] = value
                    with open('expenses.json', 'w') as f:
                        json.dump(expenses, f, indent=4)
                    print(f"Expense id {ids} amount updated successfully to {value} ")

elif (sys.argv[1] == "delete")and is_valid:
    if len(expenses) == 0:
        print("No item expenses list")
    else:
        for expense in expenses:
            if expense['id'] == ids:
                expenses.remove(expense)
                with open('expenses.json', 'w') as f:
                    json.dump(expenses, f, indent=4)
                print('Expense deleted successfully')
elif (sys.argv[1] == "list") and is_valid:
    if len(expenses) == 0:
        print("No item expenses list")
    else:
        print(f'ID  Date       Description Amount')
        for expense in expenses:
            print(f'{expense["id"]}   {expense["date"]} {expense["description"]}          ${expense["amount"]} ')


elif (sys.argv[1] == "summary")and is_valid:
    if len(expenses) == 0:
        print("No item expenses list")
    else:
        if len(sys.argv) == 4:
            for expense in expenses:
                if (expense['date'][:4] == date[:4]) and (expense['date'][5:7] == month):
                    total_expenses = int(expense['amount'])+total_expenses
            print(f"Total for the month {month} is ${total_expenses}")
        else:
            for expense in expenses:
                total_expenses = int(expense['amount'])+total_expenses
            print(f"Total expences is ${total_expenses}")
