import re
def check_password_strength(password):
    """
    Checks the strength of a password.

    Returns:
        A string indicating the strength of the password.
    """
    lenght_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    # !!! The 'r' before the regular expression pattern is used to denote a raw string. !!!
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"\W", password) is None
    password_ok = not (lenght_error or digit_error or uppercase_error or lowercase_error or symbol_error)

    if password_ok:
        return "Strong password"
    else:
        return "Weak password"