class Controller:
    def __init__(self) -> None:
        """Handles the user input and the logic of the input."""
        pass

    def get_input(self) -> str:
        """Get user input during a decision.
        
        Returns:
            str: User input.
        """
        user_input: str = input("?>: ")
        return user_input
