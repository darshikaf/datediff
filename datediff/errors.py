class InvalidInput(Exception):
    """
    Invalid input to CLI. Date must be of format YYYY-MM-DD.
    """


class InvalidDate(Exception):
    """
    Input contains invalid date component.
    """


class InvalidMonth(Exception):
    """
    Input contains invalid month component.
    """


class InvalidYear(Exception):
    """
    Input contains invalid year component.
    """
