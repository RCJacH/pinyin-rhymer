class NotAPinYinError(Exception):
    def __init__(self, string):
        message = f'{string} cannot be parsed as a PinYin'
        super().__init__(message)
