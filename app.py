#import necessary packages
from flask import Flask, request, jsonify
from datetime import datetime
import error
import database as db
import datetime
import json

app = Flask(__name__)
employees_list = []

 
@app.route('/')
def index():
    return "hello"
    
@app.route('/employee', methods=['GET'])
def get_employees():
    print("print something")
    employees = db.get_employee()
    print("print something")
    
    if employees:
        return jsonify(employees), 200
    else:
        return jsonify({"message": "no employee"}), 200


@app.route('/creatEmployee', methods=['POST'])
def create_employee():
    data = request.json
    
    name = data.get("name")
    gender = data.get("gender")
    age = data.get("age")
    email = data.get("email")
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    if not error.check_email_format(email):
        return {"error":"incorrect email format"}, 200
    
    if not error.check_for_age(age):
        return {"error":"incorrect age format"}, 200
    
    if not error.check_for_gender(gender):
        return {"error":"incorrect gender format"}, 200
    
    if not error.check_for_name(name):
        return {"error":"incorrect name format"}, 200
    
    employee = {"name":name, "gender": gender, "age": age, "email": email, "update_at": date}
    db.insert_employee(json.loads(employee))
    
    return {"message":"successful operation"}, 200
        

@app.route('/delEmployee', methods=['DELETE'])
def delete_employee():
    data = request.json
    email = data.get("email") #因為email是unique key
    
    if not error.check_email_format(email):
        return {"error":"incorrect internet format"}, 200
    
    db.delete_employee(email)
    
    return {"message":"sucessful operation"}, 200


if __name__ == '__main__':
    app.run(debug=True)
    