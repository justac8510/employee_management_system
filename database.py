import mysql.connector
from mysql.connector import errorcode

db_name = "employee"

def _update_database():
    try:
        cnx = mysql.connector.connect(database=db_name)
        cursor = cnx.cursor()
        cursor.execute("USE {}".format(db_name))
        
        query = """
        CREATE TABLE IF NOT EXISTS employee (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        gender VARCHAR(10) NOT NULL,
        age INT NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE,
        updated_at TIMESTAMP NOT NULL;
        """
        
        cursor.execute(query)
        cursor.close()
        return cnx
        
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_BAD_DB_ERROR:
            print("no database, creating one...")
            _create_database(cursor)
        else:
            print(f"unknown error {error.errno}")


def _create_database(cursor):
    try:
        cursor.execute("CREATE DATABASE IF NOT EXIST{} DEFAULT CHARACTER SET 'utf8'".format(db_name))
        cursor.close()
    except mysql.connector.Error:
        return {"error":"attempt to build the database"}, 500


def insert_employee(employee):
    cnx = mysql.connector.connect(database=db_name)
    cursor = cnx.cursor()
    
    try:
        cursor.execute("INSERT INTO employee VALUES (?, ?, ?, ?, ?)", (employee["name"], employee["gender"], employee["age"], employee["email"], employee["update_at"]))
        cnx.commit()
        cursor.close()
    except:
        cursor.close()
        return {"error":"email already existed"}, 200
    
    
def delete_employee(email):
    cnx = mysql.connector.connect(database=db_name)
    cursor = cnx.cursor()

    cursor.execute("DELETE FROM employee WHERE email = ?", email)
    
    if cursor.rowcount <= 0:
        cursor.close()
        return {"error":"employee not existed"}, 200
    
    cnx.commit()
    cursor.close()


def get_employee():
    cnx = mysql.connector.connect(user = "root", password = "0000")
    cursor = cnx.cursor()
    
    cursor.execute("SELECT * FROM employee")
    employees = cursor.fetchall()
    cursor.close()
    
    return employees
    
    
if __name__ == "__main__":
    _update_database
