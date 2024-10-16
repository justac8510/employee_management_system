#import necessary packages
from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime
import error
import database as db

app = Flask(__name__)
db_name = "employee"
cnx = db.start_database()

 
@app.route('/')
def index():
    return "<p></p>"

@app.route('/create_employee', methods=['POST'])
def create_employee():
    data = request.json
    
    name = data.get('name')
    gender = data.get('gender')
    age = data.get('age')
    email = data.get('email')
    date = data.get('date')
    
    if not error.check_email_format(email):
        return {"error":"incorrect email format"}, 200
    
    if not error.check_for_age(age):
        return {"error":"incorrect age format"}, 200
    
    if not error.check_for_gender(gender):
        return {"error":"incorrect gender format"}, 200
    
    if not error.check_for_name(name):
        return {"error":"incorrect name format"}, 200
    
    if not error.check_for_date(date):
        return {"error":"incorrect date format"}, 200
        
    
    print("request sent")
    db.insert_employee(name, gender, age, email, date, cnx)
    
    return {"message":"successful operation"}, 200
        

@app.route('/delete_employee', methods=['DELETE'])
def delete_employee():
    data = request.json
    email = data.get('email') #因為email是unique key
    
    if not error.check_email_format(email):
        return {"error":"incorrect internet format"}, 200
    
    db.delete_employee(email, cnx)
    
    return {"message":"sucessful operation"}, 200


@app.route('/employees', methods=['GET'])
def get_employees():
    employees = db.get_employee(cnx)
    
    if employees:
        return jsonify(employees), 200
    else:
        return jsonify({"message": "no employee"}), 200

if __name__ == '__main__':
    app.run(debug=True)
    