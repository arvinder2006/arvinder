import functools

def enforce_types(*types):
    """A decorator that validates the argument types of a function."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Check type matching for passed positional arguments
            for val, expected_type in zip(args, types):
                if not isinstance(val, expected_type):
                    raise TypeError(f"Argument {val} must be of type {expected_type.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


# Example Usage:
@enforce_types(int, int)
def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    try:
        print("Success Case:", add_numbers(10, 20))
        print("Failure Case:")
        add_numbers(10, "twenty")  # This will trigger the TypeError
    except TypeError as e:
        print(f"Caught expected error: {e}")
