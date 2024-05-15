#!/usr/bin/env python3
"""
Defines the function filter_datum.
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Replaces the values of specified fields in a message
    with a redaction string.
    """
    for field in fields:
        message = re.sub(r'{}=[^{}]*'.format(field, separator),
                         "{}={}".format(field, redaction), message)
    return message
