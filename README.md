# Personal Expense Tracker

## Overview
The **Personal Expense Tracker** is a Python program that helps users track their daily spending. You can add expenses, organize them by category (like Food, Transport, etc.), and view summaries by day or category. The program saves all expenses to a file, so you can access them later.

## Features
- **Add Daily Expenses**: Record your expenses with date, category, description, and amount.
- **Organize by Category**: Categorize your expenses (e.g., Food, Transport, Entertainment).
- **View Summaries**: View total expenses by a specific date or category.
- **Save Data**: All expense data is stored in a text file, so you can see your records after closing the program.
- **Error Handling**: The program will ask you to correct mistakes like wrong date formats or non-numeric amounts.

## How to Use in PyCharm
1. **Clone or download** the project files onto your computer.
2. **Open PyCharm** and create a new project or open the existing project.
3. **Add the project files** (like `expense_tracker.py` and `expenses.txt`) to your PyCharm project folder.
4. **Run the program**:
   - Right-click `expense_tracker.py`.
   - Click **Run 'expense_tracker'**.
5. In the **Run console**, you'll see a menu with options:
   - **1. Add a New Expense**: Add daily expenses.
   - **2. View Summary by Date**: View expenses for a specific day.
   - **3. View Summary by Category**: View expenses for a specific category.
   - **4. Exit**: Save your expenses and exit the program.

## Example Interaction
Here’s how the program looks when you add an expense:

```plaintext
-----------------------------------------------
|         Welcome to the Expense Tracker       |
-----------------------------------------------
1. Add a New Expense
2. View Summary by Date
3. View Summary by Category
4. Exit
-----------------------------------------------
Select an option: 1

-----------------------------------------------
|           Add a New Expense                 |
-----------------------------------------------
Enter Date (DD/MM/YYYY): 01/10/2024
Enter Category (Food/Transport/Entertainment): Food
Enter Description: Lunch with friends
Enter Amount: 12.50
-----------------------------------------------
Expense added successfully!
```

## Data Storage
- Your expenses are stored in a file called `expenses.txt` in the project folder. It will look like this:
  ```
  01/10/2024,Food,Lunch with friends,12.50
  ```

## Project Files
- **expense_tracker.py**: The main Python script that runs the program.
- **expenses.txt**: A text file where all the expenses are saved.

## Future Improvements
- Add monthly and yearly summaries.
- Create a graphical user interface (GUI) for better usability.
- Add tools to analyze spending habits and generate reports.

## Requirements
- Python 3.x (PyCharm comes with all necessary configurations for running Python code).

## How to Run the Project in PyCharm
1. Open the project in PyCharm.
2. Make sure the correct Python interpreter is set up in PyCharm.
3. Right-click `expense_tracker.py` and select **Run 'expense_tracker'**.
