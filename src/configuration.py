import i18n

class Configuration:
    """Configuration class for the game."""

    LOCALE_FILE_PATH: str = "../locale"

    def __init__(self, locale: str = "en") -> None:
        """Initialise the Configuration class."""
        self.locale: str = locale

    def i18n(self) -> i18n:
        """Initialise the i18n library."""
        i18n.load_path.append(self.LOCALE_FILE_PATH)
        return i18n