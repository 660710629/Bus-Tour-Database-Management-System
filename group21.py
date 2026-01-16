import mysql.connector
from mysql.connector import Error

def connect_to_db():
    try:
        print("Attempting to connect...")
        connection = mysql.connector.connect(
            host="134.209.101.105", 
            user="student21",
            password="password21",
            database="db_group21"  
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

def execute_query(connection, query, values=None):
    cursor = connection.cursor()
    try:
        print(f"Executing query: {query} with values: {values}") 
        cursor.execute(query, values)
        connection.commit()
        print("Operation successful")
    except Error as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()

def Add_Customer(connection, User_id, Name_Surname, Congenital_Disease, Allergic, User_Number, Family_Number, Employee_id):
    query = """INSERT INTO customer
               (User_id, Name_Surname, Congenital_Disease, Allergic, User_Number, Family_Number, Employee_id)
               VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    values = (User_id, Name_Surname, Congenital_Disease, Allergic, User_Number, Family_Number, Employee_id)
    execute_query(connection, query, values)

def Add_Bus(connection, Bus_id, Brand, Employee_id):
    query = "INSERT INTO Bus (Bus_id, Brand, Employee_id) VALUES (%s, %s, %s)"
    values = (Bus_id, Brand, Employee_id)
    execute_query(connection, query, values)

def Add_Ticket(connection, OrderID, CarNumber, SeatNumber, Round, path):
    query = "INSERT INTO tickets (OrderID, CarNumber, SeatNumber, Round, path) VALUES (%s, %s, %s, %s, %s)"
    values = (OrderID, CarNumber, SeatNumber, Round, path)
    execute_query(connection, query, values)

def Delete_Ticket(connection, OrderID):
    query = "DELETE FROM tickets WHERE OrderID = %s"
    execute_query(connection, query, (OrderID,))

def Delete_Customer(connection, User_id):
    query = "DELETE FROM customer WHERE User_id = %s"
    execute_query(connection, query, (User_id,))

def Delete_Bus(connection, Bus_id):
    query = "DELETE FROM Bus WHERE Bus_id = %s"
    execute_query(connection, query, (Bus_id,))

def View_Customer(connection, Name_Surname):
    cursor = connection.cursor()
    query = "SELECT * FROM customer WHERE Name_Surname = %s"
    try:
        cursor.execute(query, (Name_Surname,))
        records = cursor.fetchall()
        if records:
            print(f"Customer information for {Name_Surname}:")
            for column in records:
                print(f"ID: {column[0]}, Name: {column[1]}, Disease: {column[2]}, Allergic: {column[3]}, User Number: {column[4]}, Family Number: {column[5]}")
        else:
            print(f"Customer not found: {Name_Surname}")
    except Error as e:
        print(f"An error occurred while retrieving data: {e}")
    finally:
        cursor.close()

def View_Ticket(connection, OrderID):
    cursor = connection.cursor()
    query = "SELECT * FROM tickets WHERE OrderID = %s"
    try:
        cursor.execute(query, (OrderID,))
        records = cursor.fetchall()
        if records:
            print(f"Ticket {OrderID}:")
            for column in records:
                print(f"ID: {column[0]}, Car Number: {column[1]}, Seat: {column[2]}, Round: {column[3]}, Path: {column[4]}")
        else:
            print(f"Ticket not found: {OrderID}")
    except Error as e:
        print(f"An error occurred while retrieving data: {e}")
    finally:
        cursor.close()

def main():
    connection = connect_to_db()
    if connection:
        try:
            while True:
                print("----- Bus Tour Menu -----")
                print("1. Add Ticket")
                print("2. Add Customer")
                print("3. Add Bus")
                print("4. Delete Ticket")
                print("5. Delete Customer")
                print("6. Delete Bus")
                print("7. View Customer")
                print("8. View Ticket")
                print("9. Exit")

                num = input("Enter your choice (1-9): ")
                print(f"User input: {num}")

                if num == "1":
                    OrderID = input("Enter Order ID: ")
                    CarNumber = input("Enter Car Number: ")
                    SeatNumber = input("Enter Seat Number: ")
                    Round = input("Enter Round: ")
                    path = input("Enter Path: ")
                    Add_Ticket(connection, OrderID, CarNumber, SeatNumber, Round, path)

                elif num == "2":
                    User_id = input("Enter User ID: ")
                    Name_Surname = input("Enter Name and Surname: ")
                    Congenital_Disease = input("Enter Congenital Disease: ")
                    Allergic = input("Enter Allergic: ")
                    User_Number = input("Enter User Number: ")
                    Family_Number = input("Enter Family Number: ")
                    Employee_id = input("Enter Employee ID: ")
                    Add_Customer(connection, User_id, Name_Surname, Congenital_Disease, Allergic, User_Number, Family_Number, Employee_id)

                elif num == "3":
                    Bus_id = input("Enter Bus ID: ")
                    Brand = input("Enter Brand: ")
                    Employee_id = input("Enter Employee ID: ")
                    Add_Bus(connection, Bus_id, Brand, Employee_id)

                elif num == "4":
                    OrderID = input("Enter Order ID to delete: ")
                    Delete_Ticket(connection, OrderID)

                elif num == "5":
                    User_id = input("Enter User ID to delete: ")
                    Delete_Customer(connection, User_id)

                elif num == "6":
                    Bus_id = input("Enter Bus ID to delete: ")
                    Delete_Bus(connection, Bus_id)

                elif num == "7":
                    Name_Surname = input("Enter Customer Name: ")
                    View_Customer(connection, Name_Surname)

                elif num == "8":
                    OrderID = input("Enter Order ID: ")
                    View_Ticket(connection, OrderID)

                elif num == "9":
                    print("Exiting program...")
                    break

                else:
                    print("Invalid choice, please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            connection.close()
            print("Connection closed.")
    else:
        print("Failed to connect to database.")

if __name__ == "__main__":
    main()
