#Budget app for expenses. To later be connected to the To-do list.
#Possible code Login to access to-do and budget.
#Possible use code: Budget app
#import math
#add dictionary,add test, logging module, budget log
import argparse
import csv #implements classes to read and write data from csv format.
#csv.reader iterates over lines in a given csvfile.
#csv.writer converts user data into delimited strings on the given file-like object.
#with open("'to--do.csv', 'w', newline = ''") as csvfile:
#fieldname = ['âœ“', 'Date', 'Task']
#???df = csv.writer hello world!
import unittest
import subprocess
import math
import pdb
import logging
import pickle
import datetime
logging.basicConfig(filename='todo.log', level = logging.DEBUG)
logging.basicConfig(filename='budget.log', level = logging.INFO)
print("Welcome!")

budget_dict = {"monthly": "The next 4 weeks", "Yearly" : "The next 365 days ",}
with open('budget_pick.pkl','wb') as pickle_file: # serialize an object without having to add extra code.
    pickle.dump(budget_dict, pickle_file) #converts obj to byte stream that can be loaded on a buffer or disk.
    #I'd like to print all user inpur to a text or csv file.

while True:
    print("Ready to do?")
    enterexit = input("Answer with Y or N: ")
    if enterexit.upper() == "N": #built in function to change any inpt to uppercase.
        print("Exiting...")
        exit()# exit the program completely

    elif enterexit.upper() == "Y":
        print("Let's get started.")
        print("What would you like to do today?")
        todo_budget = input("Enter 'N' for BUDGET, 'Y' for TODO, or 'x' to exit: ")

        if todo_budget.upper() == "N":  # This is chunky, I'd like to make it less chunky.
            print("Let's get budgeting!")
            print("Enter a numerical amount for each monthly budget category.")
            while True:
                try:
                    checking = (int(input("Checking amount: ")))#int allows for the input interger to be printed
                    housing = (int(input("Housing: ")))
                    savings = (int(input("Savings: ")))
                    bills = (int(input("Bills: ")))
                    transportation = (int(input("Transportation: ")))
                    food = (int(input("Food: ")))
                    misc = (int(input("Misc: ")))
                    total_expenses = (housing + savings + bills + transportation + food + misc)
                    logging.info(str(total_expenses) + " is your total expense for this month")
                    print(str(total_expenses) + " is your total expense for this month") #str turns the interger into a string.
                    months_leftover = (int(checking - total_expenses))
                    logging.info(str(months_leftover) + " is your remainder this month.")
                    print(str(months_leftover) + " is your remainder this month.")
                    with open('budget.csv', 'w', newline='') as k:
                        budgetwrite = csv.writer(k)
                        dm = datetime.date.today()
                        budgetwrite.writerow(('Date', 'Expense for this month', 'Remainder for this month', 'Checking', 'Housing', 'Saving', 'Bills', 'Transportation', 'Food', 'Misc'))
                        budgetwrite.writerow((dm, total_expenses, months_leftover, checking, housing , savings, bills, transportation, food, misc))
                        k.close()
                        break
                         #continues the loop at the start.
                except ValueError:
                    print("you did not enter a valid number.")

            # I want to print results to a file here


        elif todo_budget.upper() == "Y":  # I want to import a csv file here
            print("Welcome to your Todo list!")
            df = open('todo.csv', 'r')
            rows = csv.reader(df)
            with open('todo.csv', 'r') as csvfile:
                for row in rows:
                    print(row[1:4])
                    logging.debug(row)
                df.close()
        elif todo_budget.upper() == "X":
            print("Exit Interview")
            exitinterview = input("Ready to go? 'Y' or 'N':  ")
            # elif exitinterview.upper() == "N":
            # enterexit = input("Answer with Y or N: ")
            if exitinterview.upper() == "Y":
                print("goodbye!")
                exit()
            elif exitinterview.upper() == "N":
                continue
            else:
                print("Response not valid. Enter \'y\' or \'n\'.")
        else:
            print("Response not valid. Enter \'y\' , \'n\', or \'x\'.")
    else:
        print("Response not valid. Enter \'y\' or \'n\'.")
