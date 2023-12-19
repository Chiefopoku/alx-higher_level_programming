#!/usr/bin/python3
class CustomException(Exception):
    pass

def magic_calculation(a, b):
    result = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise CustomException('Too far')
            
            result += (a + b) ** i / i
        except CustomException as e:
            print(f"Caught an exception: {e}")
        else:
            result += b

    return result
