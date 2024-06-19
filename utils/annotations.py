from functools import wraps

def TestCase(key):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func.test_case_key = key
            return func(*args, **kwargs)
        return wrapper
    return decorator
