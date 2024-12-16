import sys
from src.logger import logging

def error_message_details(error, error_detail:sys):
    """
    """
    _,_,exc_tb = error_detail.exc_info()  # get exception info (e.g. line, module etc) from sys
    file_name = exc_tb.tb_frame.f_code.co_filename # https://docs.python.org/3/reference/datamodel.html#codeobject.co_filename
    line_number = exc_tb.tb_lineno
    error_message = str(error)
    custom_error_message = f'Error occurred in script {file_name}\nLine number: {line_number}\nError message: {error_message}\n'

    return custom_error_message


class CustomException(Exception):
    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_details)

    # whenever we raise/print exception, we show our custom error_message
    def __str__(self):
        return self.error_message


if __name__ == '__main__':

    try:
        a = 1/0
    except Exception as e:
        logging.info("Oh no! Divide by zero")
        raise CustomException(e, sys)