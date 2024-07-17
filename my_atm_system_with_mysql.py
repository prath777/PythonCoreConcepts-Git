import mysql.connector
from mysql.connector import Error
from datetime import datetime




def create_connection():
    """Establishing Connection with mysql  """
    return mysql.connector.connect( 
        host="localhost",
        user="root",
        password="root",
        database="atm_db"
    )
connection =create_connection()
# if connection.is_connected():
#      print("Connection created successfully")



def create_user(username,password):
    """ For Registering a new user """
    connection=create_connection()
    cursor=connection.cursor()
    # username=input("Enter Username")
    # password=input("Enter your password")

    query="INSERT INTO USERS (username,password) VALUES (%s,%s)"
    
    try:
        cursor.execute(query,(username,password))

        connection.commit()
        print("user created successfully")
    except:
        print("Username already exists")
        print("Please try with Different username")

        print("User not created")
        connection.rollback()

    # print(cursor.rowcount,"record inserted!")  
    connection.close()  




def user_exist(username,password):
         """ It check the user exist in the database or not"""
        
         connection=create_connection()
         cursor=connection.cursor()
         try:

                query="SELECT User_id FROM USERS WHERE username= %s and password= %s "
                cursor.execute(query,(username,password))
                result=cursor.fetchone()
               
                if result==None:
                    print("User doesn't exist")
                    raise Exception ("Invalid username or password")
                else:
                    print("User exist")
                    user_id=result[0]
                    query1="SELECT account_id from accounts where user_id= %s"
                    cursor.execute(query1,(user_id,))
                    result1=cursor.fetchone()
                    print("Your account_id is \n",result1)
                    return True
                
         except Error as e:
             print(f"Error: {e}")
             return False
             connection.rollback()
connection.close()


def record_transaction(user_id, transaction_type, amount):
    """ It records the transactions which user perform which transaction and what is the amount """
    try:
        connection = create_connection()
        cursor = connection.cursor()
        query = "SELECT account_id FROM accounts WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        account_id = cursor.fetchone()[0]
        query = "INSERT INTO transactions (account_id, transaction_type, amount) VALUES (%s, %s, %s)"
        cursor.execute(query, (account_id, transaction_type, amount))
        connection.commit()
        cursor.close()
        connection.close()
    except Error as e:
        print(f"Error: {e}")

def show_transaction_record(account_id):
    """ It shows the transactions records perform by the user"""
    connection = create_connection()
    cursor = connection.cursor()

    try:
        query = "SELECT * FROM TRANSACTIONS WHERE account_id = %s"
        cursor.execute(query, (account_id,))

        result = cursor.fetchall()
        
        l = []
        for i in result:
            # Convert transaction_date to a string if it is a datetime object
            if isinstance(i[4], datetime):
                transaction_date_str = i[4].strftime("%Y-%m-%d %H:%M:%S")
            else:
                transaction_date_str = str(i[4])
            
            dic = {
                "transaction_id": i[0],
                "account_id": i[1],
                "transaction_type": i[2],
                "amount": i[3],
                "transaction_date": transaction_date_str
            }
            l.append(dic)
            print("\n")
            print("\n")
            print(l)

    except Error as e:
        print(f"Error: {e}")
    finally:
        connection.close()

#Get balance


def get_balance(user_id):
    ''' It is used to fetch the current balance from the database'''
    try:
        connection = create_connection()
        cursor = connection.cursor()
        query = "SELECT balance FROM accounts WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        print(result)
        cursor.close()
        connection.close()
        if result and result[0] is not None:
            return result[0]
        else:
            return 0
    except Error as e:
        print(f"Error: {e}")
        return 0




def update_balance(user_id, amount):
    """It is used to update the balance in the database """
    try:
        connection = create_connection()
        cursor = connection.cursor()
        query = "UPDATE accounts SET balance = %s WHERE user_id = %s"
        cursor.execute(query, (amount, user_id))
        connection.commit()
        cursor.close()
        connection.close()
        print(f"Updated balance for user_id {user_id} to {amount}")
    except Error as e:
        print(f"Error: {e}")



def deposit(user_id, amount):
    """This function is used for deposit the amount in the Account"""
    if amount > 0:
        balance = get_balance(user_id)
        new_balance = balance + amount
        update_balance(user_id, new_balance)
        record_transaction(user_id, 'deposit', amount)
        print(f"${amount} deposited successfully.")
    else:
        print("Invalid deposit amount.")
    return get_balance(user_id)


def withdraw(user_id, amount):
    """This function is used for withdrawing the amount from the database"""
    if amount > 0:
        balance = get_balance(user_id)
        new_balance = balance - amount
        update_balance(user_id, new_balance)
        record_transaction(user_id, 'withdraw', amount)
        print(f"${amount} deposited successfully.")
    else:
        print("Invalid withdraw amount.")
    return get_balance(user_id)


#User Page

while (True):
    print("/n Welcome in to atm")
    print("1.For login")
    print("2.For Register")
    print("3.For Quit")

    choice= int(input("Enter your choice"))

    if choice==1:
       username=input("Enter your username: ")
       password=input("Enter the password: ")
       print("Checking username is exist or not")
       user_exist(username,password)
  
    
       print("Welcome  User")
       while True:
        print("\nATM Menu")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction statements")
        print("5. Quit")
        choice = input("Choose an option: ")

        try:
            if choice == "1":
                amount = (input("Enter amount to deposit: "))
                amount = float(amount)
                user_id=int(input("Enter the user_id: "))
                deposit(user_id, amount)
            elif choice == "2":
                amount =(input("Enter amount to withdraw: "))
                amount = float(amount)
                user_id=int(input("Enter the user id: "))
                withdraw(user_id, amount)
            elif choice == "3":
                 user_id=int(input("Enter the user_id: "))
                 get_balance(user_id)
            elif choice =="4":
                 account_id=input("Enter your account_id: ")
                 show_transaction_record(account_id)

            elif choice == "5":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e: 
            print(amount,type(amount)) 
            if (amount==" "):
                print("Blank spaces are not allowed")
            elif(type(amount)==str):
                print("String are not allowed")
            else:
                print(e)

    elif choice==2:
        print("Welcome in to the Register Page")
        username=input('Enter the username: ')
        password=input("Enter the password: ")
        create_user(username,password)
       

    elif choice==3:
        print("Thank you for using the atm goodbye!")
        break

    else:
        print("Invalid choice")