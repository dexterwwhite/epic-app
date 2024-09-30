from flask import current_app

# Test service layer function
def testFunction():
    response = {
        "User": "You",
        "Config Variable": current_app.config['CONFIG_VARIABLE'],
        "Sub-Map": {
            "Key1": "This",
            "Key2": "is",
            "Key3": "a",
            "Key4": "TEST"
        }
    }
    return response