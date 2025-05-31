import mysql.connector
from datetime import date

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Replace with your MySQL password
    database="library_db"
)
cursor = conn.cursor()

def show_menu():
    print("\n=== Library Management System ===")
    print("1. View All Books")
    print("2. Add New Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. View Issued Books")
    print("6. Exit")

def view_books():
    cursor.execute("SELECT * FROM books")
    for row in cursor.fetchall():
        print(f"ID: {row[0]} | Title: {row[1]} | Author: {row[2]} | Status: {row[3]}")

def add_book():
    title = input("Book Title: ")
    author = input("Author Name: ")
    cursor.execute("INSERT INTO books (title, author) VALUES (%s, %s)", (title, author))
    conn.commit()
    print("✅ Book added.")

def issue_book():
    book_id = int(input("Enter Book ID to issue: "))
    issued_to = input("Enter recipient name: ")
    today = date.today()

    cursor.execute("SELECT status FROM books WHERE book_id = %s", (book_id,))
    result = cursor.fetchone()
    if result and result[0] == 'available':
        cursor.execute("INSERT INTO issued_books (book_id, issued_to, issue_date) VALUES (%s, %s, %s)", 
                       (book_id, issued_to, today))
        cursor.execute("UPDATE books SET status = 'issued' WHERE book_id = %s", (book_id,))
        conn.commit()
        print("📚 Book issued.")
    else:
        print("⚠️ Book not available or invalid.")

def return_book():
    book_id = int(input("Enter Book ID to return: "))
    today = date.today()
    cursor.execute("SELECT * FROM issued_books WHERE book_id = %s AND return_date IS NULL", (book_id,))
    result = cursor.fetchone()

    if result:
        cursor.execute("UPDATE issued_books SET return_date = %s WHERE book_id = %s AND return_date IS NULL", 
                       (today, book_id))
        cursor.execute("UPDATE books SET status = 'available' WHERE book_id = %s", (book_id,))
        conn.commit()
        print("🔁 Book returned.")
    else:
        print("⚠️ This book was not issued or has already been returned.")

def view_issued_books():
    cursor.execute("""
        SELECT i.issue_id, b.title, i.issued_to, i.issue_date, i.return_date
        FROM issued_books i
        JOIN books b ON i.book_id = b.book_id
    """)
    for row in cursor.fetchall():
        print(f"Issue ID: {row[0]} | Title: {row[1]} | To: {row[2]} | Issued: {row[3]} | Returned: {row[4]}")

# Main loop
while True:
    show_menu()
    choice = input("Select an option (1–6): ")

    if choice == '1':
        view_books()
    elif choice == '2':
        add_book()
    elif choice == '3':
        issue_book()
    elif choice == '4':
        return_book()
    elif choice == '5':
        view_issued_books()
    elif choice == '6':
        print("👋 Exiting. Goodbye!")
        break
    else:
        print("❌ Invalid choice. Try again.")

cursor.close()
conn.close()
