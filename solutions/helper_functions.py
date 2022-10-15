def isEnum(data):
    """return True when the value in an array is a string """
    if isinstance(data, list):
        return all(isinstance(item, str) for item in data) and len(data) > 0
    return False


def isArray(data):
    """return True when the value in an array is another JSON object"""
    if isinstance(data, list):
        return all(isinstance(item, dict) for item in data) and len(data) > 0
    return False


def isString(data):
    """Return True if data is a string"""
    return isinstance(data, str)


def isInteger(data):
    """Return True if data is an integer"""
    return isinstance(data, int) and not isinstance(data, bool)


def checkType(data):
    if (isEnum(data)):
        return "ENUM"
    elif (isArray(data)):
        return "ARRAY"
    elif (isString(data)):
        return "STRING"
    elif (isInteger(data)):
        return "INTEGER"
    else:
        return "NOT A REQUESTED TYPE"
