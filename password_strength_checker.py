import re
import getpass

def password_strength_check(password):
    """
    Checks the strength of a password.

    Returns:
        A string indicating the strength of the password.
    """

    lenght_error = len(password) < 8

    """!!! The 'r' before the regular expression pattern is used to denote a raw string. !!!"""
    """!!! The re.search function searches for this pattern in the password string. !!!"""

    digit_error = re.search(r"\d", password) is None # \d pattern matches any digit character
    uppercase_error = re.search(r"[A-Z]", password) is None # [A-Z] pattern matches any uppercase letter
    lowercase_error = re.search(r"[a-z]", password) is None # [a-z] pattern matches any lowercase letter
    symbol_error = re.search(r"\W", password) is None # \W pattern matches any non-word character (symbol)
    password_ok = not (lenght_error or digit_error or uppercase_error or lowercase_error or symbol_error)

    if password_ok:
        return "Strong password"
    else:
        return "Weak password"
    
if __name__ == "__main__":
    password = getpass.getpass(prompt="Enter your password: ")
    result = password_strength_check(password)
    print(result)
"""
This allows you to run the check_password_strength() function directly 
from the command line by executing the password_strength_checker.py file.
"""