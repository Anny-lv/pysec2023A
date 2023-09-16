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
        errors_found = False
        for logfile in ERROR_LOG_PATH_LIST: # Use of list and dictionary
            error_count, error_set = self.error_log_processing.get_log_errors(logfile)
        if error_set is not None: # Use of Boolean
            errors_found = True
        if errors_found:
            for error in error_set:
                print(error)
            print(f"Total {error_count} Errors found!")
        else:
            print("No errors found!")
        

if __name__ == "__main__":
    main = MainClass()
    main.run()
