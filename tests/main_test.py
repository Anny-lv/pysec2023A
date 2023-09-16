# Import the MainClass and ErrorLogProcessing correctly
from src.main import MainClass
from src.get_log_errors import ErrorLogProcessing


def test_get_syslog_errors():
    """Test get_log_errors."""
    error_processor = ErrorLogProcessing()
    main_class = MainClass()
    main_class.run()
    
    test_dict = {
    "path": "tests/test_data/error_log.txt"
    }

    error_count, error_list = error_processor.get_log_errors(test_dict)

    assert error_count == 6
    assert len(error_list) == 6