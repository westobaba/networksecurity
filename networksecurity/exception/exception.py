import sys
# Correctly import the logger instance from the logger module
from networksecurity.logging.logger import logger

class NetworkSecurity(Exception):
    """Base class for all network security exceptions."""

    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)
        _, _, exc_tb = error_details.exc_info()
        self.line_number = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        original_message = super().__str__()
        return f"{original_message} in file {self.file_name} at line {self.line_number}"

