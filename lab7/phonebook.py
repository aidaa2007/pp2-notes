import csv
from connect import connect

def insert_from_csv(conn, filename):
    cur = conn.cursor()
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cur.execute(
                "INSERT INTO contacts (first_name, last_name, phone) VALUES (%s, %s, %s)",
                (row[0], row[1], row[2])
            )
    conn.commit()
    cur.close()

def insert_console(conn):
    first_name = input("First name: ")
    last_name = input("Last name: ")
    phone = input("Phone: ")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO contacts (first_name, last_name, phone) VALUES (%s, %s, %s)",
        (first_name, last_name, phone)
    )
    conn.commit()
    cur.close()

def update_contact(conn):
    cur = conn.cursor()
    search_phone = input("Enter current phone of the contact to update: ")
    new_first_name = input("New first name: ")
    new_phone = input("New phone: ")
    cur.execute(
        "UPDATE contacts SET first_name = %s, phone = %s WHERE phone = %s",
        (new_first_name, new_phone, search_phone)
    )
    conn.commit()
    cur.close()

def query_contacts(conn):
    cur = conn.cursor()
    search_term = input("Enter name or phone prefix: ")
    cur.execute(
        "SELECT * FROM contacts WHERE first_name ILIKE %s OR phone LIKE %s",
        (f"%{search_term}%", f"{search_term}%")
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()

def delete_contact(conn):
    cur = conn.cursor()
    search_term = input("Enter first name or phone to delete: ")
    cur.execute(
        "DELETE FROM contacts WHERE first_name = %s OR phone = %s",
        (search_term, search_term)
    )
    conn.commit()
    cur.close()

def main():
    conn = connect()
    if not conn:
        print("Database connection failed")
        return

    while True:
        print("\n1. Insert from CSV")
        print("2. Insert from console")
        print("3. Update contact")
        print("4. Query contacts")
        print("5. Delete contact")
        print("6. Exit")
        choice = input("Choice: ")

        if choice == '1':
            filename = input("Enter csv filename (e.g., contacts.csv): ")
            insert_from_csv(conn, filename)
        elif choice == '2':
            insert_console(conn)
        elif choice == '3':
            update_contact(conn)
        elif choice == '4':
            query_contacts(conn)
        elif choice == '5':
            delete_contact(conn)
        elif choice == '6':
            break
        else:
            print("Invalid choice")

    conn.close()

if __name__ == '__main__':
    main()
