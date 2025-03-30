"""
Expense Tracker CLI

This script provides a command-line interface (CLI) to manage personal expenses.  
Users can add, delete, list, and summarize expenses stored in a JSON file.

Usage:
  python expense-tracker.py <command> [options]

Commands:
  add      --desc <description> --amt <amount>   Add a new expense.
  delete   --id <expense_id>                     Remove an expense by ID.
  list                                          Show all recorded expenses.
  summary  [--month <month_number>]              Show total or monthly expenses.

Data is stored in a JSON file ('data.json') for persistence.

Author: Lethios
"""

import argparse
import sys
import os
from datetime import datetime
import json

DATA_FILE = "data.json"

HELP_MESSAGE = """
Welcome to the Expense Tracker CLI!

Usage:
  python expense-tracker.py <command>

Commands:
  add  --desc (description) --amt (amount)  Add a new expense (description and amount required)
  delete --id (expense_id)                  Delete an expense by its unique ID
  list                                      List all recorded expenses
  summary [--month <month_number>]          Summary of total or monthly expenses

"""

if "--help" == sys.argv[1] or "help" == sys.argv[1]:
    print(HELP_MESSAGE)
    sys.exit(0)

parser = argparse.ArgumentParser(description="Expense Tracker CLI")
subparser = parser.add_subparsers(dest="command")

add_parser = subparser.add_parser("add")
add_parser.add_argument("--description", "--desc", type=str)
add_parser.add_argument("--amount", "--amt", type=int)

delete_parser = subparser.add_parser("delete")
delete_parser.add_argument("--id", type=int)

list_parser = subparser.add_parser("list")

summary_parser = subparser.add_parser("summary")
valid_int = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
summary_parser.add_argument("--month", type=int, choices=valid_int)

args = parser.parse_args()

def load_expenses():
    """
    Load expenses from the data file.
    """

    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = file.read()
        return json.loads(data) if data else []

def save_expenses(expense_data):
    """
    Saves expenses to the data file in JSON format.
    """

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(expense_data, file, indent=4)

expense_list = load_expenses()

if args.command == "add":
    if (args.description or args.desc) is None or (args.amount or args.amt) is None:
        print("Please provide a description and an amount for the expense.")
        sys.exit(1)

    if expense_list:
        NEW_ID = expense_list[-1]['id'] + 1
    else:
        NEW_ID = 1

    date_now = datetime.now().strftime("%d-%m-%Y")
    expense_list.append({"id": NEW_ID,
                         "date": date_now,
                         "description": (args.description or args.desc),
                         "amount": (args.amount or args.amt)})

    save_expenses(expense_list)
    print(f"Expense added successfully. (ID: {NEW_ID})")
    sys.exit(0)

elif args.command == "delete":
    if args.id is None:
        print("Please provide an ID of the expense.")
        sys.exit(1)

    for expense in expense_list:
        if expense['id'] == args.id:
            expense_list.remove(expense)
            break

    save_expenses(expense_list)
    print(f"Expense {args.id} deleted successfully.")
    sys.exit(0)

elif args.command == "list":
    if len(expense_list) == 0:
        print("No expenses found.")
        sys.exit(1)

    print()
    print(f"{"ID":<5} {"Date":<15} {"Description":<15} {"Amount":<10}")
    for expense in expense_list:
        print(f"{expense['id']:<5} {expense['date']:<15} {expense['description']:<15} {expense['amount']:<10}")

    print()
    sys.exit(0)

elif args.command == "summary":
    if args.month is None:
        TOTAL_EXPENSES = 0
        for expense in expense_list:
            TOTAL_EXPENSES += expense['amount']

        print(f"Total expenses: ${TOTAL_EXPENSES}")
        sys.exit(0)

    else:
        MONTHLY_EXPENSES = 0
        month = {1: "January",
                 2: "February",
                 3: "March",
                 4: "April",
                 5: "May",
                 6: "June",
                 7: "July",
                 8: "August",
                 9: "September",
                 10: "October",
                 11: "November",
                 12: "December"}

        for expense in expense_list:
            if int(expense['date'][3:5:]) == args.month:
                MONTHLY_EXPENSES += expense['amount']

        print(f"Total expenses for {month[args.month]}: ${MONTHLY_EXPENSES}")
        sys.exit(0)

else:
    print("Invalid argument.")
    sys.exit(1)

