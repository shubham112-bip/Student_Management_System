# Student Management System

A console-based Student Record Management Application built with Python that allows users to manage student records through an intuitive menu-driven interface. This project demonstrates core Python concepts including data types and variables, conditional statements and loops, functions, exception handling, and file I/O.

## Project Description

This application provides a fully functional command-line interface for managing student records. Users can perform complete CRUD (Create, Read, Update, Delete) operations on records that are persistently stored in a JSON file (`records.json`). The application is designed with a clean, modular architecture using functions for each operation and handles user errors gracefully.

## Features

- **Add Student Record** — Add a new student record with Roll Number, Name, Age, Email, and Phone Number (with duplicate Roll Number check)
- **View All Student Records** — Display all stored student records in a neatly formatted tabular view
- **Search Student Record** — Search records by Student Name (case-insensitive partial match) or Roll Number
- **Update Student Record** — Update any field of an existing student by Roll Number (press Enter to retain current values)
- **Delete Student Record** — Delete a student record by Roll Number with confirmation prompt
- **Persistent Storage** — All records are saved to `records.json`, ensuring data is preserved between application restarts
- **Input Validation & Exception Handling** — Handles invalid data types (e.g., entering non-numeric characters for Roll Number or Age) and runtime/file errors
- **Menu-Driven Interface** — Clear, numbered interactive menu for easy navigation

## Technologies & Concepts Used

| Technology / Concept         | Usage in Project                                                             |
|-----------------------------|------------------------------------------------------------------------------|
| **Python 3**                | Core programming language                                                    |
| **JSON Module**             | File I/O for reading and writing student records in `records.json`           |
| **Data Types & Variables**  | Integers (Roll Number, Age), Strings (Name, Email, Phone), Lists & Dicts     |
| **Conditional Statements**  | Menu routing, input validation checks, duplicate checks, confirmation prompts|
| **Loops**                   | `while True` for continuous menu loop, `for` loops for search & display      |
| **Functions**               | Modular design (`load_records`, `save_records`, `add_record`, `view_records`, `search_record`, `update_record`, `delete_record`) |
| **Exception Handling**      | `try/except` catching `ValueError`, `FileNotFoundError`, `json.JSONDecodeError` |
| **File I/O**                | Persistent storage across sessions with JSON read/write operations           |

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

---

## Required Screenshots & Sample Walkthrough

### Screenshot 1: Application Main Menu
```
===== Student Management System =====
1. Add Student Record
2. View All Student Records
3. Search Student Record
4. Update Student Record
5. Delete Student Record
6. Exit
=====================================
Enter your choice (1-6):
```

---

### Screenshot 2: Adding a New Student Record Successfully
```
Enter your choice (1-6): 1

--- Add Student Record ---
Enter Roll Number: 106
Enter Name: Tanya Singh
Enter Age: 21
Enter Email: tanya.singh@example.com
Enter Phone: 9811223344

Student record added successfully! (Roll No: 106)
```

---

### Screenshot 3: Viewing All Student Records (Minimum 5 Records)
```
Enter your choice (1-6): 2

--- All Student Records ---
--------------------------------------------------------------------------------
Roll No: 101   | Name: Shubham Shah     | Age: 22  | Email: shubhammshah20@gmail.com   | Phone: 7208410291
Roll No: 102   | Name: Priya Sharma     | Age: 21  | Email: priya.sharma@example.com   | Phone: 9820123456
Roll No: 103   | Name: Aarav Patel      | Age: 22  | Email: aarav.patel@example.com    | Phone: 9876543210
Roll No: 104   | Name: Ananya Verma     | Age: 20  | Email: ananya.verma@example.com   | Phone: 9123456780
Roll No: 105   | Name: Rohan Kulkarni   | Age: 23  | Email: rohan.k@example.com        | Phone: 9988776655
--------------------------------------------------------------------------------
Total Students: 5
```

---

### Screenshot 4: Updating or Deleting a Student Record

#### Updating a Student Record:
```
Enter your choice (1-6): 4

--- Update Student Record ---
Enter Roll Number of student to update: 105

Current Details: Roll No: 105   | Name: Rohan Kulkarni   | Age: 23  | Email: rohan.k@example.com        | Phone: 9988776655
Press Enter to keep current value.

Name [Rohan Kulkarni]: 
Age [23]: 24
Email [rohan.k@example.com]: 
Phone [9988776655]: 

Student record updated successfully!
```

#### Deleting a Student Record:
```
Enter your choice (1-6): 5

--- Delete Student Record ---
Enter Roll Number of student to delete: 105

Target Record: Roll No: 105   | Name: Rohan Kulkarni   | Age: 23  | Email: rohan.k@example.com        | Phone: 9988776655
Are you sure you want to delete this record? (y/n): y

Student record deleted successfully!
```

---

### Screenshot 5: Error Handling (Entering Invalid Data Type for a Roll Number)
```
Enter your choice (1-6): 1

--- Add Student Record ---
Enter Roll Number: abc
Error: Invalid input! Roll Number must be an integer.
```
*Or during Update/Delete operations:*
```
Enter your choice (1-6): 4

--- Update Student Record ---
Enter Roll Number of student to update: xyz
Invalid input: Roll Number must be an integer.
```

---

## Project Structure

```
Student_Management_System/
├── app.py              # Main application source code
├── records.json        # Data file storing student records (JSON format)
└── README.md           # Assignment documentation & walkthrough
```

## Data File (`records.json`)

The application uses **`records.json`** to store all student records persistently. The initial file includes 5 sample student records:

```json
[
    {
        "roll_no": 101,
        "id": 101,
        "name": "Shubham Shah",
        "age": 22,
        "email": "shubhammshah20@gmail.com",
        "phone": "7208410291"
    },
    {
        "roll_no": 102,
        "id": 102,
        "name": "Priya Sharma",
        "age": 21,
        "email": "priya.sharma@example.com",
        "phone": "9820123456"
    },
    {
        "roll_no": 103,
        "id": 103,
        "name": "Aarav Patel",
        "age": 22,
        "email": "aarav.patel@example.com",
        "phone": "9876543210"
    },
    {
        "roll_no": 104,
        "id": 104,
        "name": "Ananya Verma",
        "age": 20,
        "email": "ananya.verma@example.com",
        "phone": "9123456780"
    },
    {
        "roll_no": 105,
        "id": 105,
        "name": "Rohan Kulkarni",
        "age": 23,
        "email": "rohan.k@example.com",
        "phone": "9988776655"
    }
]
```

## GitHub Repository

- **Repository:** [https://github.com/shubham112-bip/Student_Management_System](https://github.com/shubham112-bip/Student_Management_System)
- **Author:** Shubham Shah
- **Language:** Python 3

## License

This project is submitted as an academic assignment.
