"""Main funcftion for running the program."""
from get_log_errors import ErrorLogProcessing
from constants import ERROR_LOG_PATH

class MainClass: # pylint: disable=too-few-public-methods
    """Main class."""

    def __init__(self):
        """Initialize the class."""
        self.error_log_processing = ErrorLogProcessing()

    def run(self):
        """Run the program."""
        error_count, _ = self.error_log_processing.get_log_errors(ERROR_LOG_PATH)
        print(f"{error_count} Errors found!")

if __name__ == "__main__":
    main = MainClass()
    main.run()
