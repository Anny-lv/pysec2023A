from src.main import ErrorLogProcessing




def test_get_log_errors():
    """Test get_log_errors."""
    error_log_processing = ErrorLogProcessing()
    error_count, _ = error_log_processing.get_log_errors("tests/test_data/syslog.txt")
    assert error_count == 3

