import os
import subprocess

def insecure_function(user_input):
    # SQL Injection vulnerability
    query = "SELECT * FROM users WHERE name = '" + user_input + "'"
    
    # Command injection vulnerability
    os.system("echo " + user_input)
    
    # Hardcoded credentials
    password = "super_secret_password123"
    
    # Insecure random
    import random
    token = random.randint(1, 100)
    
    return query, token

def process_data(data):
    # Using eval is insecure
    result = eval(data)
    return result