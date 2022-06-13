
#Budget app for expenses. To later be connected to the To-do list.
#Possible code Login to access to-do and budget.
#Possible use code: Budget app
#import math1
import csv

print("Welcome!")
print("Ready to do?")
while True:
    enterexit = input("Answer with Y or N: ")
    if enterexit.upper() == "N":
        print("Exiting...")
        exit()
    else:
        enterexit.upper() == "Y"
        print("Let's get started.")
        print("What would you like to do today?")
        todo_budget = input("Enter 'N' for BUDGET or 'Y' for TODO: ")
        if todo_budget.upper() == "N": #This is chunky, I'd like to make it less chunky.
            print("Let's get budgeting!")
            checking = (int(input("Checking amount: ")))
            housing = (int(input("Housing: ")))
            saving = (int(input("Saving: ")))
            bills = (int(input("Bills: ")))
            transportation = (int(input("Transportation: ")))
            food = (int(input("Food: ")))
            misc = (int(input("Misc: ")))
            total_expenses = (housing + saving + bills + transportation + food + misc)
            print(str(total_expenses ) + " is your total expense for this month")
            months_leftover = (int(checking - total_expenses))
            print(str(months_leftover ) + " is your remainder this month.")
            exit()
            # I want to print results to a file here
        elif todo_budget.upper() == "Y": # I want to import a csv file here
            df = open ('todo.csv', 'rt')
            rows = csv.reader(df)
            for row in rows:
                print(row)
              #  exitinterview = input("Ready to go? 'Y' or 'N':  ")
              #  if exitinterview.upper() == "Y":
              #   print("goodbye!")
               #     exit()
               # elif exitinterview.upper() == "N":
               # enterexit = input("Answer with Y or N: ")
