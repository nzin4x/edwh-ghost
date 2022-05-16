import pprint


class BaseGhostException(Exception):
    # Base, inherit this cls

    def __init__(
        self, status_code, error_type=None, error_message="", *a, exception=None
    ):
        super().__init__(
            str(status_code), error_type, error_message, *a
        )  # -> self.args

        self.status_code = str(status_code)
        self.error_type = error_type
        self.error_message = error_message
        self.exception = exception

    def __str__(self):
        return " - ".join(self.args) + "\n" + pprint.pformat(self.exception)


class GhostResponseException(BaseGhostException):
    # -> from JSON['errors']
    pass


class GhostUnknownException(BaseGhostException):
    # -> if JSON but no errors key
    pass


class GhostJSONException(BaseGhostException):
    # -> if JSON could not be parsed
    pass


class GhostResourceNotFoundException(BaseGhostException):
    # -> call correct but just no data
    pass
