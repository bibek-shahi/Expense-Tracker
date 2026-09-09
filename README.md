# Expense Tracker

A simple command-line expense tracker built with Python.

This project allows users to add, update, delete, list, and summarize expenses. Expense data is stored locally in a JSON file. From https://roadmap.sh/projects/expense-tracker

## Features

* Add a new expense
* Update an existing expense
* Delete an expense
* View all expenses
* View total expenses
* View expenses for a specific month
* Store expenses in a JSON file
* Basic input validation

## Technologies Used

* Python
* JSON
* `sys.argv`
* `datetime`
* `os`

## How to Run

Make sure Python is installed on your computer.

Clone the repository:

```bash
git clone <your-repository-url>
```

Go into the project folder:

```bash
cd expense-tracker
```

Run the program using:

```bash
py et.py <command>
```

## Commands

### Add an Expense

```bash
py et.py add --description "Lunch" --amount 20
```

Example output:

```text
Expense added with description: Lunch and amount: 20 successfully.
```

### List All Expenses

```bash
py et.py list
```

Example output:

```text
ID  Date        Description  Amount
1   2026-09-10  Lunch        $20
2   2026-09-10  Dinner       $30
```

### Update an Expense Description

```bash
py et.py update 1 --description "Work Lunch"
```

### Update an Expense Amount

```bash
py et.py update 1 --amount 25
```

### Delete an Expense

```bash
py et.py delete --id 1
```

### View Total Expenses

```bash
py et.py summary
```

Example output:

```text
Total expenses is $50
```

### View Expenses for a Specific Month

```bash
py et.py summary --month 9
```

Example output:

```text
Total for the month 9 is $50
```

## Data Storage

Expenses are stored inside:

```text
expenses.json
```

Each expense contains:

```json
{
    "id": 1,
    "date": "2026-09-10",
    "description": "Lunch",
    "amount": 20
}
```

If the JSON file does not exist, the program creates it automatically.

## What I Learned

While building this project, I practiced:

* Working with command-line arguments
* Reading and writing JSON files
* Using Python dictionaries and lists
* Looping through stored data
* Validating user input
* Generating unique expense IDs
* Working with dates
* Updating and deleting stored data
* Building program logic using conditions

## Future Improvements

Some features I would like to add in the future:

* Support decimal expense amounts
* Add expense categories
* Filter expenses by category
* Add monthly budgets
* Show warnings when a budget is exceeded
* Export expenses to CSV
* Refactor the application into functions
* Use `argparse` instead of manually handling `sys.argv`

## Project Inspiration

This project was built as part of the Expense Tracker project from roadmap.sh.

## Author

Built as a Python learning project.
