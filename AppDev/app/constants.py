"""
This module defines constants used throughout the application
"""
DATA = {"records": [
    {'username': 'kumarmarshal', 'name': 'kumarm', 'dept': 'IT', 'dob': '2000-01-01', 'gender': 'M',
     'password': 'Kumar@0101', 'isadmin': False},
    {'username': 'naveenbireddy', 'name': 'naveenb', 'dept': 'Dev', 'dob': '2000-02-02', 'gender': 'M',
     'password': 'Naveen@0202', 'isadmin': False},
    {'username': 'adveshk22', 'name': 'adveshk', 'dept': 'Sales', 'dob': '2000-02-22', 'gender': 'M',
     'password': 'Advesh@0202', 'isadmin': True}
]}
VALID_GENDER = ["MALE", "FEMALE", "OTHERS", "M", "F"]
USERS = ["kumarm", "naveenb"]
ADMINS = ["adveshk"]
ALL_USERS = ["kumarm", "naveenb", "adveshk"]
