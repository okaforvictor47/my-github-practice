

def reverse_text(text):
    """
    Reverses the given string.

    Args:
        text (str): The text to reverse.

    Returns:
        str: The reversed text.
    """
    return text[::-1]


def calculate(a, b, operation):
    """
    Performs basic arithmetic operations.

    Args:
        a (float): The first number.
        b (float): The second number.
        operation (str): The operation to perform: 'add', 'subtract', 'multiply', or 'divide'.

    Returns:
        float: The result of the arithmetic operation.

    Raises:
        ValueError: If an invalid operation is provided or division by zero is attempted.
    """
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    else:
        raise ValueError("Invalid operation. Choose from: 'add', 'subtract', 'multiply', 'divide'.")
