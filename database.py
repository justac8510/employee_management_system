import mysql.connector
from mysql.connector import errorcode

db_name = "employee"


def _create_database(cursor):
    try:
        cursor.execute("CREATE DATABASE IF NOT EXIST{} DEFAULT CHARACTER SET 'utf8'".format(db_name))
        cursor.close()
    except mysql.connector.Error:
        return {"error":"嘗試建造資料庫，但是失敗"}, 500

def insert_employee(name, gender, age, email):
    cnx = mysql.connector.connect(user = "root", password = "0000", database = db_name)
    cursor = cnx.cursor()
    
    try:
        cursor.execute(
            "INSERT INTO employees (name, gender, age, email) VALUES (%s, %s, %s, %s)", (name, gender, age, email)
        )
    except:
        return {"error":"電子郵件已存在"}, 400
    
    cnx.commit()
    cursor.close()
    cnx.close()
    
def delete_employee(email):
    cnx = mysql.connector.connect(user = "root", password = "0000", database = db_name)
    cursor = cnx.cursor()
    cursor.execute("DELETE FROM employee WHERE email = %s", (email,))
    
    if cursor.rowcount <= 0:
        return {"error":"員工不存在"}, 400
    
    cnx.commit()
    cursor.close()
    cnx.close()

def get_employee():
    cnx = mysql.connector.connect(user = "root", password = "0000", database = db_name)
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
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);
        """
        
        cursor.execute(query)

        cursor.close()
        cnx.close()
        
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_BAD_DB_ERROR:
            #print("沒有資料庫，正在建資料庫")
            _create_database(cursor)
        else:
            print(f"未知錯誤 {error.errno}")
