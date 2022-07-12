class NotAPinYinError(Exception):
    def __init__(self, string):
        message = f'"{string}" is not a valid pinyin.'
        super().__init__(message)


class NotAConsonantError(Exception):
    def __init__(self, string):
        message = f'"{string}" is not a valid consonant.'
        super().__init__(message)
