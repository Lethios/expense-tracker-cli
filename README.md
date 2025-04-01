# Expense Tracker CLI

A simple command-line tool to manage your expenses by adding, deleting, listing, and summarizing them.


## Features
- Add expenses with a description and amount.
- Delete expenses using their unique ID.
- List all expenses in a tabular format.
- View a summary of total expenses or filter by month.
- Data is stored in a JSON file for persistence.


## Installation
Clone the repository and navigate to the folder:
```bash
git clone https://github.com/Lethios/expense-tracker-cli.git
cd expense-tracker
```


## Usage
Run the script using:
```bash
python expense-tracker.py <command> [options]
```


### Commands
Add an expense:
```bash
python expense-tracker.py add --desc "Lunch" --amt 15
```
Delete an expense:
```bash
python expense-tracker.py delete --id 3
```
List all expenses:
```bash
python expense-tracker.py list
```
View expense summary:
```bash
python expense-tracker.py summary  # Total expenses
python expense-tracker.py summary --month 3  # March expenses
```
### Example Output
```bash
# ID    Date            Description     Amount  
# 1     19-02-2025      Lunch           $15  
# 2     30-03-2025      Groceries       $40

# Total expenses: $55

# Total expenses for March: $40
```


## Author
**Lethios**
- Github: [@Lethios](https://github.com/Lethios)
- Twitter: [@LethiosDev](https://x.com/LethiosDev)


## License
Copyright © 2025 [Lethios](https://github.com/Lethios).  
This project is licensed under the [MIT License](LICENSE).
