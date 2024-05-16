#!/usr/bin/env python3
"""
Defines the function filter_datum.
"""
import mysql.connector
import logging
import re
from typing import List
from os import environ

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Replaces the values of fields with a redaction string."""
    for field in fields:
        message = re.sub(r'{}=[^{}]*'.format(field, separator),
                         "{}={}".format(field, redaction), message)
    return message


def get_logger() -> logging.Logger:
    """
    Creates a logger Object.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    formatter = RedactingFormatter(list(PII_FIELDS))

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger


def get_db():
    """
    Sets up connection to mysql using mysql.connecter
    """
    connection = mysql.connector.connect(
        user=environ.get("PERSONAL_DATA_DB_USERNAME", "root"),
        password=environ.get("PERSONAL_DATA_DB_PASSWORD", ""),
        host=environ.get("PERSONAL_DATA_DB_HOST", "localhost"),
        database=environ.get("PERSONAL_DATA_DB_NAME")
    )

    return connection


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
        """Overrides logging.Formatter.format to redact the fields"""
        original_msg = super().format(record)
        return filter_datum(self.fields, self.REDACTION, original_msg,
                            self.SEPARATOR)
