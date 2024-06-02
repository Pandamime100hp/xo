import os


def clear_screen() -> None:
    """
    Clears the screen by executing the appropriate command based on the operating system.

    This function uses the `os.system()` function to execute the command `cls||clear` which clears the screen on Windows and Unix-based systems.

    Parameters:
    - None

    Returns:
    - None
    """
    os.system("cls||clear")