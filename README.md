# Python Expense Tracker

A terminal-based expense tracking application developed with Python
to help users record, organize, and monitor their expenses.

The project provides a practical introduction to managing financial
records using Python data structures, functions, user input,
conditional statements, and file handling.

## Features

- Add expenses with an amount, category, and description.
- View recorded expenses.
- Calculate total expenditure.
- Calculate expenditure by category.
- Delete selected expense records.
- Store expense data in a JSON file.
- Load previously saved expense data when supported by the
  application's startup workflow.

## Technologies Used

- Python 3
- JSON
- Python Standard Library

## Project Structure

Expense-Tracker/
|
|-- main.py
|-- expense.json
|-- README.md

Note: The filenames above reflect the structure discussed during
development. Update this section if your final repository uses
different filenames or additional modules.

## How It Works

The application allows users to record expenses by providing
the amount spent, the category of expenditure, and a description.

Recorded expenses can be displayed for review. The application
also supports calculating total spending and examining expenditure
by category.

Users can delete an expense record when necessary.

JSON file handling provides a way to store expense data so that
records can be retained between application sessions.

## Requirements

- Python 3 installed on your computer.
- A terminal or command-line interface.

No third-party packages are required for the core functionality
described in this project.

## Installation and Usage

### 1. Clone the Repository

git clone https://github.com/smackdex/Expense-Tracker.git

### 2. Navigate to the Project Directory

cd Expense-Tracker

### 3. Run the Application

python3 main.py

Follow the menu instructions displayed in the terminal to manage
your expense records.

## Data Storage

The application uses JSON file handling to store expense records.

JSON provides a simple way to represent structured data and makes
it possible for Python to save and retrieve expense information.

Keep the data file in the location expected by the application
so that saving and loading operations work correctly.

## Concepts Practised

This project provides practical experience with:

- Functions and program organization
- Dictionaries and lists
- Loops and conditional statements
- User input and validation
- Exception handling
- File handling
- JSON serialization and deserialization
- Expense calculations and category-based grouping



## Author

Abdulsamad Sanusi

