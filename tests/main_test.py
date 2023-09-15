
import  pytest
from src.get_log_errors import ErrorLogProcessing



def test_get_log_errors():
    """Test get_log_errors."""
    error_count, _ = ErrorLogProcessing.get_log_errors(ErrorLogProcessing,"tests/test_data/syslog.txt")
    assert error_count == 3

