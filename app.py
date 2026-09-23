import json

DATA_FILE = "records.json"


# ─── File I/O ─────────────────────────────────────────────────────

def load_records():
    """Load records from JSON file. Returns empty list if file doesn't exist."""
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_records(records):
    """Save records list to JSON file."""
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(records, f, indent=4)
    except Exception as e:
        print(f"Error saving records: {e}")


# ─── Helper Functions ─────────────────────────────────────────────

def get_roll_no(record):
    """Retrieve Roll Number from record (supports 'roll_no' and 'id')."""
    return record.get("roll_no", record.get("id"))


def format_student(r):
    """Format student details as a single string."""
    roll = get_roll_no(r)
    return f"Roll No: {roll:<5} | Name: {r['name']:<16} | Age: {r['age']:<3} | Email: {r['email']:<26} | Phone: {r['phone']}"


# ─── CRUD Functions ──────────────────────────────────────────────

def add_record(records):
    """Add a new student record with input validation and duplicate check."""
    print("\n--- Add Student Record ---")
    roll_no_input = input("Enter Roll Number: ").strip()
    if not roll_no_input:
        print("Error: Roll Number cannot be empty.")
        return

    try:
        roll_no = int(roll_no_input)
    except ValueError:
        print("Error: Invalid input! Roll Number must be an integer.")
        return

    # Check for duplicate Roll Number
    if any(get_roll_no(r) == roll_no for r in records):
        print(f"Error: A student with Roll Number {roll_no} already exists.")
        return

    name = input("Enter Name: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return

    age_input = input("Enter Age: ").strip()
    if not age_input:
        print("Error: Age cannot be empty.")
        return

    try:
        age = int(age_input)
    except ValueError:
        print("Error: Invalid input! Age must be a number.")
        return

    email = input("Enter Email: ").strip()
    phone = input("Enter Phone: ").strip()

    records.append({
        "roll_no": roll_no,
        "id": roll_no,
        "name": name,
        "age": age,
        "email": email,
        "phone": phone
    })
    save_records(records)
    print(f"\nStudent record added successfully! (Roll No: {roll_no})")


def view_records(records):
    """Display all student records."""
    print("\n--- All Student Records ---")
    if not records:
        print("No student records found.")
        return

    print("-" * 80)
    for r in records:
        print(format_student(r))
    print("-" * 80)
    print(f"Total Students: {len(records)}")


def search_record(records):
    """Search records by Roll Number or Name (case-insensitive partial match)."""
    print("\n--- Search Student Record ---")
    if not records:
        print("No student records to search.")
        return

    term = input("Enter Name or Roll Number to search: ").strip()
    if not term:
        print("Search term cannot be empty.")
        return

    term_lower = term.lower()
    matches = [
        r for r in records
        if term_lower in r["name"].lower() or str(get_roll_no(r)) == term
    ]

    if matches:
        print(f"\nFound {len(matches)} matching result(s):")
        print("-" * 80)
        for r in matches:
            print(format_student(r))
        print("-" * 80)
    else:
        print(f"No student record found matching '{term}'.")


def update_record(records):
    """Update a student record by Roll Number. Press Enter to keep current value."""
    print("\n--- Update Student Record ---")
    if not records:
        print("No student records to update.")
        return

    try:
        roll_no = int(input("Enter Roll Number of student to update: "))
    except ValueError:
        print("Invalid input: Roll Number must be an integer.")
        return

    target = None
    for r in records:
        if get_roll_no(r) == roll_no:
            target = r
            break

    if target is None:
        print(f"No student found with Roll Number {roll_no}.")
        return

    print(f"\nCurrent Details: {format_student(target)}")
    print("Press Enter to keep current value.\n")

    name = input(f"Name [{target['name']}]: ").strip()
    if name:
        target["name"] = name

    age_input = input(f"Age [{target['age']}]: ").strip()
    if age_input:
        try:
            target["age"] = int(age_input)
        except ValueError:
            print("Invalid age entered. Keeping current value.")

    email = input(f"Email [{target['email']}]: ").strip()
    if email:
        target["email"] = email

    phone = input(f"Phone [{target['phone']}]: ").strip()
    if phone:
        target["phone"] = phone

    save_records(records)
    print("\nStudent record updated successfully!")


def delete_record(records):
    """Delete a student record by Roll Number with user confirmation."""
    print("\n--- Delete Student Record ---")
    if not records:
        print("No student records to delete.")
        return

    try:
        roll_no = int(input("Enter Roll Number of student to delete: "))
    except ValueError:
        print("Invalid input: Roll Number must be an integer.")
        return

    target = None
    for r in records:
        if get_roll_no(r) == roll_no:
            target = r
            break

    if target is None:
        print(f"No student found with Roll Number {roll_no}.")
        return

    print(f"\nTarget Record: {format_student(target)}")
    confirm = input("Are you sure you want to delete this record? (y/n): ").strip().lower()

    if confirm == "y":
        records.remove(target)
        save_records(records)
        print("\nStudent record deleted successfully!")
    else:
        print("Deletion cancelled.")


# ─── Main Menu ───────────────────────────────────────────────────

def main():
    """Main menu loop for Student Management System."""
    records = load_records()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student Record")
        print("2. View All Student Records")
        print("3. Search Student Record")
        print("4. Update Student Record")
        print("5. Delete Student Record")
        print("6. Exit")
        print("=====================================")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_record(records)
        elif choice == "2":
            view_records(records)
        elif choice == "3":
            search_record(records)
        elif choice == "4":
            update_record(records)
        elif choice == "5":
            delete_record(records)
        elif choice == "6":
            print("\nThank you for using Student Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
