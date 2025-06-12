import inspect
from functools import wraps


def strict(func):
    sig = inspect.signature(func)
    annotations = func.__annotations__

    @wraps(func)
    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)
        for name, value in bound.arguments.items():
            if name in annotations:
                expected_type = annotations[name]
                if not isinstance(value, expected_type):
                    raise TypeError(
                        f"Argument '{name}' must be \n"
                        f"{expected_type.__name__}, got {type(value).__name__}"
                    )
        return func(*args, **kwargs)

    return wrapper
