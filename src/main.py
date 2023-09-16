"""Main funcftion for running the program."""
from src.get_log_errors import ErrorLogProcessing
from src.constants import ERROR_LOG_PATH_LIST

class MainClass: # pylint: disable=too-few-public-methods
    """Main class."""

    def __init__(self):
        """Initialize the class."""
        self.error_log_processing = ErrorLogProcessing()

    def run(self):
        """Run the program."""
        for logfile in ERROR_LOG_PATH_LIST:
            error_count, _ = self.error_log_processing.get_log_errors(logfile)
            print(f"{error_count} Errors found!")

if __name__ == "__main__":
    main = MainClass()
    main.run()
