def is_valid_password(password):
    if len(password) < 8:
        return False
    
    has_number = any(char.isdigit() for char in password)

    has_uppercase = any(char.isupper() for char in password)

    return has_number and has_uppercase


password = input("Enter your password: ")

if is_valid_password(password):
    print("✅ Password is valid.")

else:
    print("Invalid Password")