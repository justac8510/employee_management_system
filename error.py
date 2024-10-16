
def check_email_format(email):
    if type(email) != str:
        return False
    
    if "@" in email:
        return ".com" in email[email.index("@"):]
    return False

def check_for_age(age):
    if type(age) == int:
        return 20 <= age and age <= 65
    else:
        return False
    
def check_for_name(name):
    return type(name) == str

def check_for_date(date):
    return type(date) == str

def check_for_gender(gender):
    return gender.lower() == "male" or gender.lower() == "female" or gender.lower() == "f" or gender.lower() == "m"
