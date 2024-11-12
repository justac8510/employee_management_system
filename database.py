import mysql.connector
from mysql.connector import errorcode
import json
import time, datetime

db_name = "employee"

def update_database():
    try:
        cnx = mysql.connector.connect(user='root', password='0000')
        cursor = cnx.cursor()
        cursor.execute("USE {}".format(db_name))
        
        query = """
        CREATE TABLE IF NOT EXISTS employee (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        gender VARCHAR(10) NOT NULL,
        age INT NOT NULL,
        email NVARCHAR(100) NOT NULL UNIQUE,
        updated_at TIMESTAMP NOT NULL);
        """
        
        cursor.execute(query)
        cnx.commit()
        cursor.close()
        cnx.close()
        
    except mysql.connector.Error as error:
        print(f"unknown error {error.errno}")
        cursor.execute("CREATE DATABASE IF NOT EXISTS {};".format(db_name))
        return



def insert_employee(employee):
    cnx = mysql.connector.connect(user='root', password='0000', database=db_name)
    cursor = cnx.cursor()
    
    try:
        employee_info = json.loads(employee)
        updated_at = datetime.datetime.strptime(employee_info["updated_at"], "%d/%m/%Y")
        
        query = ("INSERT INTO employee (name, gender, age, email, updated_at)" "VALUES (%s, %s, %s, %s, %s)")
        employee_info = (employee_info["name"], employee_info["gender"], employee_info["age"], employee_info["email"], updated_at)
        cursor.execute(query, employee_info)        
        
        cnx.commit()
        cursor.close()
        cnx.close()
    except mysql.connector.Error as error:
        cnx.commit()
        cursor.close()
        cnx.close()
    
    
def delete_employee(email):
    cnx = mysql.connector.connect(user='root', password='0000', database=db_name)
    cursor = cnx.cursor()

    cursor.execute("DELETE FROM employee WHERE email = (%s)", email)
    
    if cursor.rowcount <= 0:
        cursor.close()
        return {"error":"employee not existed"}, 200
    
    cnx.commit()
    cursor.close()
    cnx.close()
    


def get_employee():
    cnx = mysql.connector.connect(user='root', password='0000', database=db_name)
    cursor = cnx.cursor()
    
    cursor.execute("SELECT * FROM employee")
    employees = cursor.fetchall()
    cnx.commit()
    cursor.close()
    cnx.close()
    
    return employees
    
    
if __name__ == "__main__":
    update_database()
