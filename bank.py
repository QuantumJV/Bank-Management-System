import os
import platform
import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Your_sql_password",
    database="bank"
)
mycursor = mydb.cursor()

def authenticate_user():
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        print("+=======================================================+\n")
        print("+ !!!!!!!!!!!!!!!! ENTER LOGIN DETAILS !!!!!!!!!!!!!!!!+\n")
        print("+=======================================================+\n")
        print(f">> Total attempts left: [ {max_attempts - attempts} / {max_attempts} ] <<\n")
        username = input(">>> ENTER YOUR USERNAME TO LOGIN => ")
        password = input(">>> ENTER YOUR PASSWORD TO LOGIN => ")

        sql = "SELECT * FROM users WHERE username = %s AND password = %s"
        mycursor.execute(sql, (username, password))
        result = mycursor.fetchone()

        if result:
            print(f"\n### Authentication successful. Welcome To Bank Management, {username}!! ###\n")
            return True
        else:
            print("\n$$$ Invalid username or password. Please try again. $$$\n")
            attempts += 1

    print("==> Maximum login attempts reached. Exiting program. <== \n")
    return False

def AccWithdraw():
    L = []
    AccountNo = int(input(">>> Enter the Account number => "))
    L.append(AccountNo)
    AmountWithdrawn = eval(input(">>> Enter the Amount to be withdrawn => "))
    L.append(AmountWithdrawn)
    month = input(">>> Enter month of Withdrawal =>")
    L.append(month)
    cust = (L)
    sql = "Insert into amount(AccountNo,AmountWithdrawn,Month) values(%s,%s,%s)"
    mycursor.execute(sql, cust)
    mydb.commit()
    
def AccInsert():
    print("=======================================================\n")
    print("+ !!!!!!!!!!!!!!!! ENTER YOUR DETAILS !!!!!!!!!!!!!!!! +\n")
    print("=======================================================\n")
    AccountNo = int(input("ENTER THE ACCOUNT NUMBER !! "))
    name = input("ENTER THE CUSTOMER NAME !! ")
    age = int(input("ENTER THE AGE OF CUSTOMER !! "))
    occupation = input("ENTER THE CUSTOMER OCCUPATION !! ")
    Address = input("ENTER THE ADDRESS OF THE CUSTOMER !! ")
    MobileNo = int(input("ENTER THE MOBILE NUMBER !! "))
    AadharNumber = int(input("ENTER THE AADHAR NUMBER !! "))
    Amount = float(input("ENTER THE MONEY DEPOSITED !! "))
    AccountType = input("ENTER THE ACCOUNT TYPE (Saving/RD/PPF/Current) !! ")
    sql = '''Insert into ACCOUNT(AccountNo,Name,Age,occupation,Address,MobileNo,AadharNumber,Amount,AccountType) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}')'''.format(AccountNo,name,age,occupation,Address,MobileNo,AadharNumber,Amount,AccountType)
    mycursor.execute(sql)
    mydb.commit()

def AccView():
    print("=======================================================\n")
    print("+ !!!!!!!!!!!!!!!! ENTER YOUR DETAILS !!!!!!!!!!!!!!!! +\n")
    print("=======================================================\n")
    print("++++ SELECT THE SEARCH CRITERIA !! ++++ \n")
    print("1. Account No")
    print("2. Name")
    print("3. Mobile No")
    print("4. Aadhar Number")
    print("5. View All")
    ch = int(input("\n>>> ENTER THE CHOICE => "))
    if ch == 1:
        s = int(input("ENTER ACCOUNT NUMBER !!"))
        rl = (s,)
        sql = "SELECT * FROM account WHERE AccountNo=%s"
        mycursor.execute(sql, rl)
        res = mycursor.fetchall()
        print("The Customer details are as follows : ")
        k = pd.DataFrame(res, columns=['AccountNo','Name','Age','occupation','Address','MobileNo','AadharNumber','Amount','AccountType'])
        print(k)
    elif ch == 2:
        s = input("ENTER NAME !!")
        rl = (s,)
        sql = "select * from account where Name=%s"
        mycursor.execute(sql, rl)
        res = mycursor.fetchall()
        print("The Customer details are as follows : ")
        k = pd.DataFrame(res, columns=['AccountNo','Name','Age','occupation','Address','MobileNo','AadharNumber','Amount','AccountType'])
        print(k)
    elif ch == 3:
        s = int(input("ENTER MOBILE NUMBER !!"))
        rl = (s,)
        sql = "select * from account where MobileNo=%s"
        mycursor.execute(sql, rl)
        res = mycursor.fetchall()
        print("The Customer details are as follows : ")
        k = pd.DataFrame(res, columns=['AccountNo','Name','Age','occupation','Address','MobileNo','AadharNumber','Amount','AccountType'])
        print(k)
    elif ch == 4:
        s = input("ENTER AADHAR !! ")
        rl = (s,)
        sql = "select * from account where AadharNumber=%s"
        mycursor.execute(sql, rl)
        res = mycursor.fetchall()
        print("The Customer details are as follows : ")
        k = pd.DataFrame(res, columns=['AccountNo','Name','Age','occupation','Address','MobileNo','AadharNumber','Amount','AccountType'])
        print(k)
    elif ch == 5:
        sql = "select * from account"
        mycursor.execute(sql)
        res = mycursor.fetchall()
        print("\n +++++++++++++++++++++++++++++++ THE CUSTOMER DETAILS ARE AS FOLLOWS !! ++++++++++++++++++++++++++++ \n")
        k = pd.DataFrame(res, columns=['AccountNo','Name','Age','occupation','Address','MobileNo','AadharNumber','Amount','AccountType'])
        print(k)
        print("\n ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ ")

def AccDeposit():
    L = []
    AccountNo = int(input("Enter the Account number : "))
    L.append(AccountNo)
    AmountDeposite = eval(input("Enter the Amount to be deposited : "))
    L.append(AmountDeposite)
    month = input("Enter month of Salary : ")
    L.append(month)
    cust = (L)
    sql = "Insert into amount(AccountNo,AmountDeposite,Month) values(%s,%s,%s)"
    mycursor.execute(sql, cust)
    mydb.commit()

def accView():
    print("=======================================================\n")
    print("+ !!!!!!!!!!!!!!!! ENTER YOUR DETAILS !!!!!!!!!!!!!!!! +\n")
    print("=======================================================\n")
    print("++++++++++ PLEASE ENTER THE DETAILS TO VIEW THE MONEY DETAILS !! ++++++++++")
    AccountNo = int(input("\n>>> ENTER THE ACCOUNT NUMBER OF THE CUSTOMER WHOSE AMOUNT IS TO BE VIEWED => "))
    sql = ''' SELECT 
            Account.AccountNo, 
            Account.Name, 
            Account.Age,
            Account.occupation,
            Account.Address,    
            Account.MobileNo,
            Account.AadharNumber,
            Account.Amount,
            Account.AccountType,
            SUM(amount.AmountDeposite) AS TotalDeposited,
            amount.month,
            amount.AmountWithdrawn
        FROM 
            Account 
            INNER JOIN amount ON Account.AccountNo = amount.AccountNo 
        WHERE 
            Account.AccountNo = %s
        GROUP BY 
            Account.AccountNo, 
            Account.Name, 
            Account.Age,
            Account.occupation,
            Account.Address,
            Account.MobileNo,
            Account.AadharNumber,
            Account.Amount,
            Account.AccountType,
            amount.month,
            amount.AmountWithdrawn
    '''
    rl = (AccountNo,)
    mycursor.execute(sql, rl)
    res = mycursor.fetchall()
    print("The Customer details are as follows : ")
    k = pd.DataFrame(res, columns=['AccountNo','Name','Age','occupation','Address','MobileNo','AadharNumber','Amount','AccountType','TotalDeposited','month','AmountWithdrawn'])
    print(k)


def closeAcc():
    AccountNo = int(input(">>>ENTER THE ACCOUNT NUMBER OF THE CUSTOMER TO BE CLOSED => "))
    
    # Check if the account exists
    check_sql = "SELECT * FROM account WHERE AccountNo = %s"
    mycursor.execute(check_sql, (AccountNo,))
    res = mycursor.fetchall()

    if not res:
        print("=>ACCOUNT NOT FOUND.<=")
        return

    print("The Following Account details will be closed;")
    k = pd.DataFrame(res, columns=['AccountNo', 'Name', 'Age', 'Occupation', 'Address', 'MobileNo', 'AadharNumber', 'Amount', 'AccountType'])
    print(k)
    delete_amount_sql = "DELETE FROM amount WHERE AccountNo = %s"
    mycursor.execute(delete_amount_sql, (AccountNo,))
    
    delete_account_sql = "DELETE FROM account WHERE AccountNo = %s"
    mycursor.execute(delete_account_sql, (AccountNo,))
    mydb.commit()
    
def displayMenu():
    print("\nEnter 1: To Add Customer")
    print("Enter 2: To View Customer")
    print("Enter 3: To Deposit Money")
    print("Enter 4: To Withdraw Money")
    print("Enter 5: To Close Account")
    print("Enter 6: To View All Customer Details")

def runAgain():
    runAgn = input("\n>>> Do You Want To Run The Program Again Yes[Y]/no[n] => ")
    return runAgn.lower() == 'y'

if authenticate_user():
    while True:
        def displayMenu():
            print("=======================================================\n")
            print("+ !!!!!!!!!!!!!!!! WELCOME TO BANK  !!!!!!!!!!!!!!!!! +\n")
            print("=======================================================\n")
            print("\nEnter 1: To Add Customer")
            print("Enter 2: To View Customer")
            print("Enter 3: To Deposit Money")
            print("Enter 4: To Withdraw Money")
            print("Enter 5: To Close Account")
            print("Enter 6: To View All Customer Details")

        displayMenu()

        try:
            userInput = int(input("\n>>> Please Select An Above Option => "))
        except ValueError:
            exit("\n>>> Hey! That's Not A Number !!")

        print("\n")

        if userInput == 1:
            AccInsert()
        elif userInput == 2:
            AccView()
        elif userInput == 3:
            AccDeposit()
        elif userInput == 4:
            AccWithdraw()
        elif userInput == 5:
            closeAcc()
        elif userInput == 6:
            accView()
        else:
            print(">>>Enter correct choice. . . ")

        if not runAgain(): 
            break
