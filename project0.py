#!/usr/bin/env bash
#Budget app for expenses. To later be connected to the To-do list.
#Possible code Login to access to-do and budget.
#Possible use code: Budget app
#import math
#add dictionary,add test, logging module, budget log kk

import csv #implements classes to read and write data from csv format.
#csv.reader iterates over lines in a given csvfile.
#csv.writer converts user data into delimited strings on the given file-like object.
#with open("'to--do.csv', 'w', newline = ''") as csvfile:
#fieldname = ['âœ“', 'Date', 'Task']
#???df = csv.writer
import unittest
import subprocess
import math
import pdb
import turtle
import logging
import pickle
logging.basicConfig(filename='todo.log', level = logging.DEBUG)
logging.basicConfig(filename='budget.log', level = logging.INFO)
print("Welcome!")

budget = {"monthly": "The next 4 weeks", "Yearly" : "The next 365 days ",}
while True:
    print("Ready to do?")
    enterexit = input("Answer with Y or N: ")
    if enterexit.upper() == "N":
        print("Exiting...")
        exit()
    else:
        enterexit.upper() == "Y"
        print("Let's get started.")
        print("What would you like to do today?")
        todo_budget = input("Enter 'N' for BUDGET or 'Y' for TODO: ")
        if todo_budget.upper() == "N":  # This is chunky, I'd like to make it less chunky.
            print("Let's get budgeting!")
            checking = (int(input("Checking amount: ")))
            housing = (int(input("Housing: ")))
            saving = (int(input("Saving: ")))
            bills = (int(input("Bills: ")))
            transportation = (int(input("Transportation: ")))
            food = (int(input("Food: ")))
            misc = (int(input("Misc: ")))
            total_expenses = (housing + saving + bills + transportation + food + misc)
            logging.info(str(total_expenses) + " is your total expense for this month")
            print(str(total_expenses) + " is your total expense for this month")
            months_leftover = (int(checking - total_expenses))
            logging.info(str(months_leftover) + " is your remainder this month.")
            print(str(months_leftover) + " is your remainder this month.")
            continue
            # I want to print results to a file here
        elif todo_budget.upper() == "Y":  # I want to import a csv file here
            df = open('todo.csv', 'rt')
            rows = csv.reader(df)
            for row in rows:
                print(row)
                logging.debug(row)
            break
print("Exit Interview")
exitinterview = input("Ready to go? 'Y' or 'N':  ")
        # elif exitinterview.upper() == "N":
        # enterexit = input("Answer with Y or N: ")
while exitinterview.upper() != "Y":
    print("goodbye!")
    exit()
    if exitinterview.upper() == "N":
        continue
