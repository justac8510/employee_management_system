#import necessary packages
from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime
import error
import database as db

app = Flask(__name__)


db_name = "employee"

 
@app.route('/create_employee', methods=['POST'])
def create_employee():
    data = request.json
    
    name = data.get('name')
    gender = data.get('gender')
    age = data.get('age')
    email = data.get('email')
    
    if error.check_email_format(email):
        return {"error":"電子郵件格式不正確"}, 400
    
    if error.check_for_age(age):
        return {"error":"年齡格式不正確"}, 400
    
    if error.check_for_gender(gender):
        return {"error":"性別格式不正確"}, 400
    
    if error.check_for_name(name):
        return {"error":"名字格式不正確"}, 400
    
    db.insert_employee(name, gender, age, email)
        

@app.route('/delete_employee', methods=['DELETE'])
def delete_employee():
    data = request.json
    email = data.get('email') #因為email是unique key
    
    if error.check_email_format(email):
        return {"error":"電子郵件格式不正確"}, 400
    
    db.delete_employee(email)


@app.route('/employees', methods=['GET'])
def get_employees():
    employees = db.get_employee()
    
    if employees:
        return jsonify(employees), 200
    else:
        return jsonify({"message": "目前沒有員工"}), 200

if __name__ == '__main__':
    app.run(debug=True)
    