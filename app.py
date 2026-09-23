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


# ─── CRUD Functions ──────────────────────────────────────────────

def add_record(records):
    """Add a new record by prompting the user for details."""
    print("\n--- Add Record ---")
    try:
        name = input("Enter name: ").strip()
        if not name:
            print("Name cannot be empty.")
            return

        age = int(input("Enter age: "))

        email = input("Enter email: ").strip()
        phone = input("Enter phone: ").strip()

        # Auto-generate ID
        new_id = max((r["id"] for r in records), default=0) + 1

        records.append({
            "id": new_id,
            "name": name,
            "age": age,
            "email": email,
            "phone": phone
        })
        save_records(records)
        print(f"Record added successfully. (ID: {new_id})")

    except ValueError:
        print("Invalid input. Age must be a number.")


def view_records(records):
    """Display all records."""
    print("\n--- All Records ---")
    if not records:
        print("No records found.")
        return

    for r in records:
        print(f"ID: {r['id']}  |  Name: {r['name']}  |  Age: {r['age']}  |  Email: {r['email']}  |  Phone: {r['phone']}")


def search_record(records):
    """Search records by name (case-insensitive partial match)."""
    print("\n--- Search Record ---")
    if not records:
        print("No records to search.")
        return

    term = input("Enter name to search: ").strip().lower()
    matches = [r for r in records if term in r["name"].lower()]

    if matches:
        print(f"Found {len(matches)} result(s):")
        for r in matches:
            print(f"ID: {r['id']}  |  Name: {r['name']}  |  Age: {r['age']}  |  Email: {r['email']}  |  Phone: {r['phone']}")
    else:
        print("No matching records found.")


def update_record(records):
    """Update a record by ID. Press Enter to keep current value."""
    print("\n--- Update Record ---")
    if not records:
        print("No records to update.")
        return

    try:
        record_id = int(input("Enter ID of record to update: "))
    except ValueError:
        print("Invalid ID.")
        return

    # Find the record
    target = None
    for r in records:
        if r["id"] == record_id:
            target = r
            break

    if target is None:
        print(f"No record found with ID {record_id}.")
        return

    print(f"Current: Name={target['name']}, Age={target['age']}, Email={target['email']}, Phone={target['phone']}")
    print("Press Enter to keep current value.\n")

    name = input(f"Name [{target['name']}]: ").strip()
    if name:
        target["name"] = name

    age_input = input(f"Age [{target['age']}]: ").strip()
    if age_input:
        try:
            target["age"] = int(age_input)
        except ValueError:
            print("Invalid age. Keeping current value.")

    email = input(f"Email [{target['email']}]: ").strip()
    if email:
        target["email"] = email

    phone = input(f"Phone [{target['phone']}]: ").strip()
    if phone:
        target["phone"] = phone

    save_records(records)
    print("Record updated successfully.")


def delete_record(records):
    """Delete a record by ID with confirmation."""
    print("\n--- Delete Record ---")
    if not records:
        print("No records to delete.")
        return

    try:
        record_id = int(input("Enter ID of record to delete: "))
    except ValueError:
        print("Invalid ID.")
        return

    # Find the record
    target = None
    for r in records:
        if r["id"] == record_id:
            target = r
            break

    if target is None:
        print(f"No record found with ID {record_id}.")
        return

    print(f"Record: Name={target['name']}, Age={target['age']}, Email={target['email']}, Phone={target['phone']}")
    confirm = input("Are you sure you want to delete? (y/n): ").strip().lower()

    if confirm == "y":
        records.remove(target)
        save_records(records)
        print("Record deleted successfully.")
    else:
        print("Deletion cancelled.")


# ─── Main Menu ───────────────────────────────────────────────────

def main():
    """Main menu loop."""
    records = load_records()

    while True:
        print("\n===== Record Management System =====")
        print("1. Add Record")
        print("2. View All Records")
        print("3. Search Record")
        print("4. Update Record")
        print("5. Delete Record")
        print("6. Exit")
        print("====================================")

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
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()
