"""
This module defines constants used throughout the application
"""
DATA = {"records": [
    {'username': 'kumarm', 'name': 'kumarm', 'dept': 'IT', 'dob': '2000-01-01', 'gender': 'M', 'isadmin': False},
    {'username': 'naveenb', 'name': 'naveenb', 'dept': 'Dev', 'dob': '2000-02-02', 'gender': 'M','isadmin': False},
    {'username': 'adveshk', 'name': 'adveshk', 'dept': 'Sales', 'dob': '2000-02-22', 'gender': 'M',  'isadmin': True}
]}
VALID_GENDER = ["MALE", "FEMALE", "OTHERS", "M", "F"]
USERS = ["kumarm", "naveenb"]
ADMINS = ["adveshk"]
ALL_USERS = ["kumarm", "naveenb", "adveshk"]
PASSWORDS = {
    "adveshk": "Advesh@0202",
    "naveenb": "Naveen@0202",
    "kumarm": "Kumar@0101"
}
# email configurations
SMTP_PORT = 587  # For starttls
SMTP_SERVER = "smtp.gmail.com"
SENDER_EMAIL = "adveshk22@gmail.com"
RECEIVER_EMAIL = ["adveshk22@gmail.com", "adveshhh.k@gmail.com"]
PASSWORD = "uuphxybkxlowcpgp"

DELETE_MESSAGE = """
Hlo Team
Admin has deleted the Record in DATA,performed DELETE Method
Thank you 
"""
UPDATE_MESSAGE = """
Hlo team
Admin has updated the records in DATA,it'means Performed PUT Method
Thank You
"""
GET_ALL_MESSAGE = """
Some one is checking all users information from the table
"""
PARTIAL_UPDATE = """
Hlo Team
Admin has partially updated the records in DATA, It's means performed PATCH Method
Thank you
"""

CREATE_USER = """
Hlo team
Admin has triggered the create_user function to crate user(or)admin
Check logs for better understand
"""
UNAUTHENTICATED_MESSAGE = f"""
Hlo team
ALERT:-Unauthenticated user, trying to access the application
check logs
"""
UPDATE_USER_RECORD = """
Hlo team
User has updated his profile
Thank you
"""

UNAUTHENTICATED_MESSAGE = "UnAuthorised user {} trying to access the application"

UNAUTHENTICATED_MESSAGE_BODY= """
Hlo team\n
UnAuthorised user {} trying to access the application"
Thank you, 

"""
ERROR_GROUP_EMAIL =' [adveshk22@gmail.com]'