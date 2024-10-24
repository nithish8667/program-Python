def is_strong_password(password):  
    if len(password) < 8:  
        return False  
    has_upper = has_lower = has_digit = has_special = False  
    special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>?/"  
    for char in password:  
        if char.isupper():  
            has_upper = True  
        elif char.islower():  
            has_lower = True  
        elif char.isdigit():  
            has_digit = True  
        elif char in special_characters:  
            has_special = True  
    return all([has_upper, has_lower, has_digit, has_special])   
password =input()
print(is_strong_password(password))
