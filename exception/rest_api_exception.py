class RestApiException(Exception):
    """
    异常基类
    """
    STATUS_CODE = 400

    def __init__(self, code: int = STATUS_CODE, message: str = "error"):
        self.code = code
        self.message = message

    def get_status_code(self):
        return self.STATUS_CODE

    def with_status_code(self, status_code: int):
        self.STATUS_CODE = status_code
        return self

    def get_code(self):
        return self.code

    def set_code(self, code: int):
        self.code = code

    def get_message(self):
        return self.message

    def set_message(self, message: str):
        self.message = message

    def with_code(self, code: int):
        self.set_code(code)
        return self

    def with_message(self, message: str):
        self.set_message(message)
        return self
