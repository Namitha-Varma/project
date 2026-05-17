username = input("username:")
password = input("password:")
attempts = input("attempts:")

try:
    if username == "":
        raise ValueError("username cannot be empty")
    
    if len(password) < 8:
        raise ValueError("weak password")
    
    attempts = int(attempts)
    if attempts < 0:
        raise ValueError("attempts cannot be negative")
    
except ValueError as e:
    print(e)

except Exception as e:
    print(e)
else:
    print("login data eccepted")
finally:
    print("validation completed")
    
