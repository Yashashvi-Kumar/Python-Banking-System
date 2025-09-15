import mysql.connector
from datetime import date

# Establish a connection to the MySQL database
mydb = mysql.connector.connect(host="localhost", user="root", passwd="help", database="bank")
mycursor = mydb.cursor()

# Create tables if they don't exist
mycursor.execute("CREATE TABLE IF NOT EXISTS bank_master(acno CHAR(4) PRIMARY KEY, name VARCHAR(30), city CHAR(20), mobileno CHAR(10), balance DECIMAL(10,2))")
mycursor.execute("CREATE TABLE IF NOT EXISTS banktrans(acno CHAR(4), amount DECIMAL(10,2), dot DATE, ttype CHAR(1), FOREIGN KEY (acno) REFERENCES bank_master(acno))")
mydb.commit()

# Function to create a new bank account
def create_account():
    print("Welcome to Yuk Cooperative Bank!")
    print("All information prompted is mandatory to be filled")
    acno = input("Enter account number: ")
    name = input("Enter name (limit 35 characters): ")
    city = input("Enter city name: ")
    mn = input("Enter mobile no.: ")
    balance = 1000  # Set default balance to ₹1000
    mycursor.execute("INSERT INTO bank_master VALUES (%s, %s, %s, %s, %s)", (acno, name, city, mn, balance))
    mydb.commit()
    print("Account is successfully created!!!")

# Function to deposit money into an account
def deposit_money():
    acno = input("Enter account number: ")

    # Check if the account exists
    mycursor.execute("SELECT balance FROM bank_master WHERE acno = %s", (acno,))
    account_exists = mycursor.fetchone()

    if account_exists:
        dp = float(input("Enter amount to be deposited: "))
        dot = str(date.today())
        ttype = "d"

        # Update bank_master first
        mycursor.execute("UPDATE bank_master SET balance = balance + %s WHERE acno = %s", (dp, acno))
        mydb.commit()

        # Insert into banktrans
        mycursor.execute("INSERT INTO banktrans VALUES (%s, %s, %s, %s)", (acno, dp, dot, ttype))
        mydb.commit()

        print("Money has been deposited successfully!!!")
    else:
        print(f"Error: Account with account number {acno} not found!")

# Function to withdraw money from an account
def withdraw_money():
    acno = input("Enter account number: ")
    wd = eval(input("Enter amount to be withdrawn: "))
    
    mycursor.execute("SELECT balance FROM bank_master WHERE acno = %s", (acno,))
    record = mycursor.fetchone()

    if record:
        balance = record[0]
        if wd > balance:
            print("Error: Insufficient balance!")
        else:
            dot = str(date.today())
            ttype = "w"
            mycursor.execute("INSERT INTO banktrans VALUES (%s, %s, %s, %s)", (acno, wd, dot, ttype))
            mycursor.execute("UPDATE bank_master SET balance = balance - %s WHERE acno = %s", (wd, acno))
            mydb.commit()
            print("Money has been withdrawn successfully!!!")
    else:
        print(f"Account with account number {acno} not found!")

# Function to display account details and transaction history
def display_account():
    acno = input("Enter account number: ")
    mycursor.execute("SELECT * FROM bank_master WHERE acno = %s", (acno,))
    record = mycursor.fetchone()

    if record:
        print("\nAccount Details:")
        print(f"Account Number: {record[0]}")
        print(f"Name: {record[1]}")
        print(f"City: {record[2]}")
        print(f"Mobile Number: {record[3]}")
        print(f"Balance: ₹{record[4]:,.2f}")

        print("\nTransaction History:")
        mycursor.execute("SELECT * FROM banktrans WHERE acno = %s", (acno,))
        for transaction in mycursor:
            ttype = "Deposit" if transaction[3] == "d" else "Withdrawal"
            print(f"Date: {transaction[2]}, Amount: ₹{transaction[1]:,.2f}, Type: {ttype}")
    else:
        print(f"Account with account number {acno} not found!")

# Function to send money from one account to another
def send_money():
    sender_acno = input("Enter your account number: ")
    receiver_acno = input("Enter recipient's account number: ")
    amount = eval(input("Enter amount to be sent: "))

    # Check if sender's account exists
    mycursor.execute("SELECT balance FROM bank_master WHERE acno = %s", (sender_acno,))
    sender_record = mycursor.fetchone()

    if sender_record:
        sender_balance = sender_record[0]

        if amount > sender_balance:
            print("Error: Insufficient balance!")
        else:
            dot = str(date.today())
            ttype_sender = "w"
            ttype_receiver = "d"

            # Update sender's transaction
            mycursor.execute("INSERT INTO banktrans VALUES (%s, %s, %s, %s)", (sender_acno, amount, dot, ttype_sender))
            mycursor.execute("UPDATE bank_master SET balance = balance - %s WHERE acno = %s", (amount, sender_acno))

            # Update receiver's transaction
            mycursor.execute("INSERT INTO banktrans VALUES (%s, %s, %s, %s)", (receiver_acno, amount, dot, ttype_receiver))
            mycursor.execute("UPDATE bank_master SET balance = balance + %s WHERE acno = %s", (amount, receiver_acno))

            mydb.commit()
            print(f"₹{amount:,.2f} has been sent successfully!")
    else:
        print(f"Sender account with account number {sender_acno} not found!")

# Function to delete a bank account
def delete_account():
    acno = input("Enter account number to delete: ")
    confirmation = input("Are you sure you want to delete your account? (yes/no): ").lower()

    if confirmation == 'yes':
        # Delete from banktrans table
        mycursor.execute("DELETE FROM banktrans WHERE acno = %s", (acno,))
        
        # Delete from bank_master table
        mycursor.execute("DELETE FROM bank_master WHERE acno = %s", (acno,))
        mydb.commit()

        print("Account successfully deleted!")
    else:
        print("Account deletion canceled.")

# Main function to run the banking system
def main():
    print("Welcome to YUK Cooperative Bank!")
    while True:
        print("\n1=Create account")
        print("2=Deposit money")
        print("3=Withdraw money")
        print("4=Display account")
        print("5=Send money")
        print("6=Delete account")
        print("7=Exit")
        ch = input("Enter your choice: ")

        if ch == "1":
            create_account()
        elif ch == "2":
            deposit_money()
        elif ch == "3":
            withdraw_money()
        elif ch == '4':
            display_account()
        elif ch == '5':
            send_money()
        elif ch == '6':
            delete_account()
        elif ch == '7':
            print("\nThank you for using YUK Cooperative Bank!")
            break
        else:
            print("Invalid choice. Enter correct choice.")

if __name__ == "__main__":
    main()
