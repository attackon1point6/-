from exception.rest_api_exception import RestApiException


class NotFoundException(RestApiException):
    STATUS_CODE = 404