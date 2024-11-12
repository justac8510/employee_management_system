#import necessary packages
from flask import Flask, request, jsonify
import datetime
import error
import database as db
import datetime
import json

app = Flask(__name__)
employees_list = []

@app.route("/")
def index():
    return "<p></p>"
    
@app.route("/employee", methods=['GET'])
def get_employees():
    employees = db.get_employee()
    
    if employees:
        return jsonify(employees), 200
    else:
        return jsonify({"message": "no employee"}), 200


'''
When creating the api post call, make sure to match the parameter

- name: String type
- gender: male, m, female, f, not case sensitive
- age: integer value
- email: The identifier must begin with an alphabet and can include a combination of alphabets, 
numbers, and hyphens. It should be followed by a symbol, after which there must be a sequence 
of alphabets and numbers, ending with '.com'.

'''
@app.route("/", methods=['POST'])
@app.route("/createEmployee", methods=['POST'])
def create_employee():
    data = request.json
    
    name = data["name"]
    gender = data["gender"]
    age = data["age"]
    email = data["email"]
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    
    if not error.check_email_format(email):
        return {"error":"incorrect email format"}, 200
    
    if not error.check_for_age(age):
        return {"error":"incorrect age format"}, 200
    
    if not error.check_for_gender(gender):
        return {"error":"incorrect gender format"}, 200
    
    if not error.check_for_name(name):
        return {"error":"incorrect name format"}, 200
    
    employee = {"name":name, "gender": gender, "age": age, "email": email, "update_at": date}
    employees_list.append(employee)
    db.insert_employee(json.dumps(employee))
    
    return {"message":"successful operation"}, 200
        

@app.route("/delEmployee", methods=['DELETE'])
def delete_employee():
    data = request.json
    email = data["email"] #因為email是unique key
    
    if not error.check_email_format(email):
        return {"error":"incorrect internet format"}, 200
    
    db.delete_employee(email)
    
    return {"message":"sucessful operation"}, 200


if __name__ == '__main__':
    app.run(debug=True ,port=5000,use_reloader=True)
    