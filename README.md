# 📚 Library Management System (Python + MySQL)

A terminal-based library management system to manage books, track issues and returns, and maintain records using a MySQL backend.

---

## 🛠️ Features

- 📘 View all available books
- ➕ Add new books to the system
- 📤 Issue books to users
- 🔁 Return books with date logging
- 🗃️ Track issued books and their return status

---

## 🗂️ Technologies Used

- Python 3.x
- MySQL
- `mysql-connector-python` library

---

## 🖼️ Screenshots

### 🔹 Book Issuing Flow
![Issuing Screenshot](images/terminal-screenshot.png)

### 🔹 Database Design
![ER Diagram](images/entity-relationship-diagram.png)

---

## ⚙️ Setup Instructions

### ✅ MySQL Setup

1. Import the schema:
```sql
-- In MySQL or phpMyAdmin
SOURCE database.sql;
