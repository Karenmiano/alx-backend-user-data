#!/usr/bin/env python3
"""
Defines the function filter_datum.
"""
import re


def filter_datum(
        fields: str, redaction: str, message: str, separator: str) -> str:
    """
    Replaces the values of specified fields in a message
    with a redaction string.
    """
    for field in fields:
        message = re.sub(field + r'=[^{}]*'.format(separator),
                         field + "=" + redaction, message)
    return message
