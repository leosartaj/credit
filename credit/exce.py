#!/usr/bin/python2

"""
Exceptions
"""

class CreditSheetExists(Exception):
    """
    Raised when credit sheet already exists
    """
    pass


class CreditSheetError(Exception):
    """
    Raised when credit sheet there is an error related to credit sheet
    """
    pass
