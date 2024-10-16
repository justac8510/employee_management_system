import mysql.connector
from mysql.connector import errorcode

db_name = "employee"


def _create_database(cursor):
    try:
        cursor.execute("CREATE DATABASE IF NOT EXIST{} DEFAULT CHARACTER SET 'utf8'".format(db_name))
        cursor.close()
    except mysql.connector.Error:
        return {"error":"attempt to build the database"}, 500

def insert_employee(name, gender, age, email, date, cnx):
    cursor = cnx.cursor()
    
    try:
        cursor.execute("INSERT INTO employee VALUES (?, ?, ?, ?, ?)", (name, gender, age, email, date))
        cnx.commit()
        cursor.close()
    except:
        return {"error":"email already existed"}, 200
    
    
def delete_employee(email, cnx):
    cursor = cnx.cursor()
    cursor.execute("DELETE FROM employee WHERE email = ?", email)
    
    if cursor.rowcount <= 0:
        return {"error":"employee not existed"}, 200
    
    cnx.commit()
    cursor.close()


def get_employee(cnx):
    cursor = cnx.cursor()
    
    cursor.execute("SELECT * FROM employee")
    employees = cursor.fetchall()
    cursor.close()
    
    return employees
    
    
def start_database():
    try:
        cnx = mysql.connector.connect(user = "root", password = "0000")
        cursor = cnx.cursor()
        cursor.execute("USE {}".format(db_name))
        
        query = """
        CREATE TABLE IF NOT EXISTS employee (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        gender VARCHAR(10) NOT NULL,
        age INT NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE,
        updated_at VARCHAR(100) NOT NULL);
        """
        
        cursor.execute(query)
        cursor.close()
        return cnx
        
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_BAD_DB_ERROR:
            print("沒有資料庫，正在建資料庫")
            _create_database(cursor)
        else:
            print(f"unknown error {error.errno}")
