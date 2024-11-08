import re

def check_email_format(email):
    return re.match(r'^[\w\.-]+@[\w\.-]+\.(com)$', email)

def check_for_age(age):
    return (20 <= age and age <= 65)

def check_for_name(name):
    return type(name) == str

def check_for_date(date):
    return type(date) == str

def check_for_gender(gender):
    return gender.lower() == "male" or gender.lower() == "female" or gender.lower() == "f" or gender.lower() == "m"
