#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except:
        pass
    finally:
        try:
            print("Inside result: {}".format(result))
        except:
            print("Inside result: {}".format(None))
            return None
    return result
