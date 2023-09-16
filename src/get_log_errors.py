"""Class for error log processing."""
from typing import List, Tuple


class ErrorLogProcessing:
    """Class for error log processing."""
    def __init__(self):
        self.error_count: int = 0
    
    def get_log_errors(self, path: str) -> tuple[int, List[str]]:
        error_list: List[str] = []
        try:
            # Open the log file for reading
            with open(path, 'r') as log_file:
                # Read each line in the log file
                for line in log_file:
                    # Check if the line contains the word "Error"
                    if "error" in line.lower():
                        self.error_count += 1
                        error_list.append(line)

        except FileNotFoundError:
            print(f"Log file not found at {path}")
            return 0, []
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0, []

            # Print the total number of errors found
        return self.error_count, error_list
        

