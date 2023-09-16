# Import the MainClass and ErrorLogProcessing correctly
from src.main import MainClass
from src.get_log_errors import ErrorLogProcessing
from src.constants import ERROR_LOG_PATH_LIST

def test_get_syslog_errors():
    """Test get_log_errors from syslog file."""
    error_processor = ErrorLogProcessing()
    main_class = MainClass()
    main_class.run()
    
    test_dict = ERROR_LOG_PATH_LIST[0]

    error_count, error_list = error_processor.get_log_errors(test_dict)

    assert error_count == 6
    assert len(error_list) == 6

def test_get_weblog_errors():
    """Test get_log_errors from web log file."""
    error_processor = ErrorLogProcessing()
    main_class = MainClass()
    main_class.run()
    
    test_dict = ERROR_LOG_PATH_LIST[1]

    error_count, error_list = error_processor.get_log_errors(test_dict)

    assert error_count == 4
    assert len(error_list) == 4