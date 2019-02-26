def is_year(text):
    if int(text) < 1900 or int(text) > 2100:
        return True
    else:
        return False