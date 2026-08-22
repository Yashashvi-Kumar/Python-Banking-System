# 🏦 Python Banking System

A simple **command-line banking management system** developed using **Python and MySQL** as a Class 12 Computer Science project.

The project simulates basic banking operations such as creating accounts, depositing and withdrawing money, transferring money between accounts, viewing account details and transaction history, and deleting accounts.

---

## 📌 Project Overview

The **YUK Cooperative Bank** system is a menu-driven application that connects Python to a MySQL database.

It maintains customer account information and transaction records in two database tables:

* `bank_master` — stores customer account details and current balance.
* `banktrans` — stores deposit, withdrawal, and money-transfer transactions.

The project demonstrates how Python can be integrated with MySQL to create a simple database-driven application.

---

## ✨ Features

The banking system provides the following operations:

### 1. 🆕 Create Account

* Creates a new bank account.
* Stores the customer's:

  * Account number
  * Name
  * City
  * Mobile number
* New accounts are created with an initial balance of **₹1000**.

### 2. 💰 Deposit Money

* Allows money to be deposited into an existing account.
* Updates the account balance.
* Records the transaction with the current date.

### 3. 💸 Withdraw Money

* Allows money to be withdrawn from an account.
* Checks whether sufficient balance is available.
* Prevents withdrawal when the balance is insufficient.
* Records the withdrawal in the transaction table.

### 4. 📄 Display Account

Displays:

* Account number
* Account holder's name
* City
* Mobile number
* Current balance
* Complete transaction history

### 5. 🔄 Send Money

Allows money to be transferred from one account to another.

The system:

* Checks the sender's account.
* Checks the sender's available balance.
* Deducts the amount from the sender.
* Adds the amount to the recipient.
* Records both transactions.

### 6. 🗑️ Delete Account

* Asks the user for confirmation.
* Deletes the account's transaction records.
* Deletes the account from the main account table.

### 7. 🚪 Exit

Closes the banking application.

---

## 🗄️ Database Structure

The project uses a MySQL database named:

```text
bank
```

### `bank_master`

Stores the main account information.

| Column     | Data Type       | Description                  |
| ---------- | --------------- | ---------------------------- |
| `acno`     | `CHAR(4)`       | Account number / Primary Key |
| `name`     | `VARCHAR(30)`   | Account holder's name        |
| `city`     | `CHAR(20)`      | Customer's city              |
| `mobileno` | `CHAR(10)`      | Customer's mobile number     |
| `balance`  | `DECIMAL(10,2)` | Current account balance      |

### `banktrans`

Stores transaction information.

| Column   | Data Type       | Description                                        |
| -------- | --------------- | -------------------------------------------------- |
| `acno`   | `CHAR(4)`       | Account number / Foreign Key                       |
| `amount` | `DECIMAL(10,2)` | Transaction amount                                 |
| `dot`    | `DATE`          | Date of transaction                                |
| `ttype`  | `CHAR(1)`       | Transaction type (`d` = deposit, `w` = withdrawal) |

---

## 🔗 Database Relationship

The `acno` column in `banktrans` references the `acno` column in `bank_master`.

```text
bank_master
    |
    | acno
    ↓
banktrans
```

This relationship ensures that transactions are associated with a valid bank account.

---

## 🛠️ Technologies Used

* **Python 3**
* **MySQL**
* **MySQL Connector/Python**
* **SQL**
* Python `datetime` module

---

## 📦 Requirements

Before running the project, make sure you have:

1. Python 3 installed
2. MySQL Server installed and running
3. MySQL Connector for Python installed

Install the connector using:

```bash
pip install mysql-connector-python
```

---

## ⚙️ Database Setup

Create the MySQL database before running the Python program:

```sql
CREATE DATABASE bank;
```

Then make sure the MySQL username and password in the Python program match your MySQL installation.

For example:

```python
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="help",
    database="bank"
)
```

> **Note:** Replace `passwd="help"` with your actual MySQL password.

The program automatically creates the required tables if they do not already exist.

---

## ▶️ How to Run

### Step 1 — Clone the repository

```bash
git clone https://github.com/your-username/Python-Banking-System.git
```

### Step 2 — Open the project folder

```bash
cd Python-Banking-System
```

### Step 3 — Install the MySQL connector

```bash
pip install mysql-connector-python
```

### Step 4 — Create the database

Open MySQL and run:

```sql
CREATE DATABASE bank;
```

### Step 5 — Configure the database connection

Update the following section in the Python file:

```python
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="your_password",
    database="bank"
)
```

### Step 6 — Run the program

```bash
python bank.py
```

---

## 🖥️ Main Menu

When the program starts, the following menu is displayed:

```text
Welcome to YUK Cooperative Bank!

1=Create account
2=Deposit money
3=Withdraw money
4=Display account
5=Send money
6=Delete account
7=Exit

Enter your choice:
```

The user can select an operation by entering the corresponding number.

---

## 🧠 Python Concepts Demonstrated

This project demonstrates several important Class 12 programming concepts:

* Functions
* Conditional statements
* Loops
* User input
* Exception-prone input handling
* MySQL database connectivity
* SQL queries
* Primary keys
* Foreign keys
* CRUD operations
* Database transactions
* String formatting
* Date handling
* Variables and data types
* Menu-driven programming

---

## 🔐 Basic Banking Operations

### Deposit

```text
Previous Balance
       +
 Deposit Amount
       ↓
 New Balance
```

### Withdrawal

```text
Current Balance
       -
Withdrawal Amount
       ↓
 Remaining Balance
```

### Money Transfer

```text
Sender Account              Receiver Account
      │                            │
      ↓                            ↓
   - Amount                     + Amount
      │                            │
      └──────── Transaction ────────┘
```

---

## 📁 Project Structure

A simple project structure can be:

```text
Python-Banking-System/
│
├── bank.py
├── README.md
└── LICENSE
```

---

## 🎯 Project Objectives

The main objectives of this project are:

1. To understand Python-MySQL connectivity.
2. To learn how databases can be used in real-world applications.
3. To implement basic banking operations using Python.
4. To understand SQL queries and database relationships.
5. To practice functions and menu-driven programming.
6. To maintain transaction records using a relational database.

---

## ⚠️ Important Note

This project is intended **for educational purposes only** and is not suitable for handling real banking operations or sensitive financial information.

For a production banking system, additional security measures would be required, including authentication, authorization, encrypted communication, secure password storage, transaction locking, input validation, logging, and proper error handling.

---

## 🚀 Possible Future Improvements

The project can be extended by adding:

* 🔑 Customer login and authentication
* 🔐 Password/PIN protection
* 📱 OTP verification
* 📊 Monthly account statements
* 🧾 Receipt generation
* 🔎 Search functionality
* 🏦 Multiple account types
* 👤 Admin panel
* 📈 Transaction reports
* 💳 Debit/credit card simulation
* 🛡️ Better input validation and error handling
* 🔒 Secure database transactions
* 🖥️ Graphical User Interface (GUI) using Tkinter

---

## 👨‍🎓 Project Information

**Project Name:** Python Banking System
**Bank Name:** YUK Cooperative Bank
**Language:** Python
**Database:** MySQL
**Project Type:** Class 12 Computer Science Project
**Application Type:** Command-Line / Console Application

---

## 📜 License

This project was created for educational purposes as part of a Class 12 Computer Science project.

You are welcome to study, modify, and improve the code for learning purposes.

---

## ⭐ Acknowledgement

This project helped demonstrate how **Python programming and MySQL databases can work together to build a practical real-world application**.

Thank you for checking out the **Python Banking System**! 🏦🐍
