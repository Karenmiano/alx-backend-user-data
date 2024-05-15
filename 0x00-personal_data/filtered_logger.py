#!/usr/bin/env python3
"""
Defines the function filter_datum.
"""
import logging
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


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]) -> None:
        """
        Sets the format string of formatter.
        Sets the fields to be redacted.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Overrides logging.Formatter.format to redact the fields
        in logging.LogRecord.msg
        """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)
