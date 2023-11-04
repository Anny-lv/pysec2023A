import os
import datetime
from src.constants import LOG_ROOT_PATH

class LogFileLister:
    def __init__(self):
        """Initialize the class."""
        self.directory = LOG_ROOT_PATH

    def collect_directory_contents(path):
        file_list = []
        try:
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                
                if os.path.isdir(item_path):
                    file_list.extend(collect_directory_contents(item_path))
                else:
                    file_info = {
                        "name": item,
                        "path": os.path.relpath(item_path, LOG_ROOT_PATH),
                    }
                    file_list.append(file_info)
        except Exception as e:
            print(e)
        return file_list

    def get_file_stats(self, filename):
        if os.path.exists(filename):
            file_size = os.path.getsize(filename)
            file_creation_time = datetime.datetime.fromtimestamp(os.path.getctime(filename))
            file_access_time = datetime.datetime.fromtimestamp(os.path.getatime(filename))
            file_modification_time = datetime.datetime.fromtimestamp(os.path.getmtime(filename))

            print(f"File: {filename}")
            print(f"Size: {file_size} bytes")
            print(f"Created: {file_creation_time}")
            print(f"Last Accessed: {file_access_time}")
            print(f"Last Modified: {file_modification_time}")
        else:
            print(f"File '{filename}' does not exist.")