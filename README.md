# Bank-Management-System

The provided code is a Python script for a banking system project utilizing MySQL for data storage and retrieval. The project encompasses various features essential for managing banking operations. Let's break down the features and functionalities present in the project:

**Username and Password Authentication:**

The script implements a function authenticate_user() to authenticate users based on their username and password. It allows a limited number of login attempts before exiting the program.

**Add Customer Details:**
The function AccInsert() allows the addition of customer details such as account number, name, age, occupation, address, mobile number, Aadhar number, deposited amount, and account type into the database.

**View Customer Details:**
The function AccView() facilitates the viewing of customer details based on various search criteria such as account number, name, mobile number, Aadhar number, or viewing all customers' details.

**Deposit Money:**
The function AccDeposit() enables users to deposit money into their accounts. It prompts the user to enter the account number, amount to be deposited, and the month of deposit.

**Withdraw Money:**
**The function AccWithdraw()** allows users to withdraw money from their accounts. It prompts the user to enter the account number, amount to be withdrawn, and the month of withdrawal.

**Close Account:**
The closeAcc() function facilitates closing a customer's account. It deletes the account details and associated transaction history from the database based on the provided account number.

**View All Customer Details:**
The function accView() retrieves and displays all details of a specific customer, including account information, transaction history (deposits and withdrawals), and total deposited amount.
Overall, this banking system project provides essential functionalities required for managing banking operations efficiently, including user authentication, customer data management, transaction handling (deposits and withdrawals), and account closure. Users can perform various actions like depositing money, withdrawing money, viewing customer details, and closing accounts through a command-line interface. The project leverages Python for scripting and MySQL for database management, ensuring data integrity and security.
