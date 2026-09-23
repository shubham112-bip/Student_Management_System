# Student Management System

A console-based Record Management Application built with Python that allows users to manage student records through a menu-driven interface. This project demonstrates core Python concepts including data types, conditional statements, loops, functions, exception handling, and file I/O.

## Project Description

This application provides a fully functional command-line interface for managing student records. Users can perform all CRUD (Create, Read, Update, Delete) operations on records that are persistently stored in a JSON file. The application is designed with a clean, modular architecture using well-defined functions for each operation.

## Features

- **Add Record** — Add a new student record with auto-generated ID, name, age, email, and phone number
- **View All Records** — Display all stored records in a formatted table
- **Search Record** — Search records by name using case-insensitive partial matching
- **Update Record** — Update any field of an existing record by ID (press Enter to keep current value)
- **Delete Record** — Delete a record by ID with confirmation prompt
- **Persistent Storage** — All records are saved to a JSON file, so data is retained between sessions
- **Input Validation** — Robust exception handling for invalid inputs (non-numeric age, empty names, invalid IDs)
- **Menu-Driven Interface** — Simple and intuitive numbered menu for navigation

## Technologies & Concepts Used

| Technology / Concept         | Usage in Project                                                |
|-----------------------------|-----------------------------------------------------------------|
| **Python 3**                | Core programming language                                       |
| **JSON module**             | File I/O for reading/writing records to `records.json`          |
| **Data Types & Variables**  | Strings, integers, lists, dictionaries used for record storage  |
| **Conditional Statements**  | Menu selection logic, input validation, confirmation prompts    |
| **Loops**                   | `while True` for main menu loop, `for` loops for record search  |
| **Functions**               | Modular design — each operation is a separate function          |
| **Exception Handling**      | `try/except` blocks for `ValueError`, `FileNotFoundError`, etc. |
| **File I/O**                | Persistent storage using JSON file read/write operations        |

## How to Run the Application

### Prerequisites
- Python 3.6 or higher installed on your system

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/shubham112-bip/Student_Management_System.git
   cd Student_Management_System
   ```

2. **Run the application:**
   ```bash
   python3 app.py
   ```
   Or on Windows:
   ```bash
   python app.py
   ```

3. **Follow the on-screen menu** to add, view, search, update, or delete records.

## Sample Input/Output

### Main Menu
```
===== Record Management System =====
1. Add Record
2. View All Records
3. Search Record
4. Update Record
5. Delete Record
6. Exit
====================================
Enter your choice (1-6):
```

### Adding a Record
```
--- Add Record ---
Enter name: Shubham
Enter age: 22
Enter email: shubhammshah20@gmail.com
Enter phone: 7208410291
Record added successfully. (ID: 1)
```

### Viewing All Records
```
--- All Records ---
ID: 1  |  Name: Shubham  |  Age: 22  |  Email: shubhammshah20@gmail.com  |  Phone: 7208410291
```

### Searching a Record
```
--- Search Record ---
Enter name to search: shubham
Found 1 result(s):
ID: 1  |  Name: Shubham  |  Age: 22  |  Email: shubhammshah20@gmail.com  |  Phone: 7208410291
```

### Updating a Record
```
--- Update Record ---
Enter ID of record to update: 1
Current: Name=Shubham, Age=22, Email=shubhammshah20@gmail.com, Phone=7208410291
Press Enter to keep current value.

Name [Shubham]:
Age [22]: 23
Email [shubhammshah20@gmail.com]:
Phone [7208410291]:
Record updated successfully.
```

### Deleting a Record
```
--- Delete Record ---
Enter ID of record to delete: 1
Record: Name=Shubham, Age=22, Email=shubhammshah20@gmail.com, Phone=7208410291
Are you sure you want to delete? (y/n): y
Record deleted successfully.
```

## Project Structure

```
Student_Management_System/
├── app.py              # Main application source code
├── records.json        # Data file storing student records (auto-created)
└── README.md           # Project documentation
```

## Data File

The application uses **`records.json`** to store all records. This file is automatically created when the first record is added. Records are stored as a JSON array of objects:

```json
[
    {
        "id": 1,
        "name": "Shubham",
        "age": 22,
        "email": "shubhammshah20@gmail.com",
        "phone": "7208410291"
    }
]
```

## GitHub Repository

- **Repository:** [Student_Management_System](https://github.com/shubham112-bip/Student_Management_System)
- **Author:** Shubham Shah
- **Language:** Python 3

## License

This project is submitted as an academic assignment.
