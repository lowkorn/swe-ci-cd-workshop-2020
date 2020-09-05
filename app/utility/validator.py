def validate_name(name):
    is_contain_digit = any(c.isdigit() for c in name)
    if is_contain_digit is False:
        return True
    return False


def validate_id(id):
    if len(id) == 13:
        return True
    return False


def validate_phone_number(phone_number):
    if len(phone_number) == 10 and phone_number[0] == "0":
        return True
    return False
