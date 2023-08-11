print("Email validator")
print('----------------')

import re
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        print(f"{email} is a valid email address.")
    else:
         print(f"{email} is NOT a valid email address.")

email=input()
is_valid_email(email)
