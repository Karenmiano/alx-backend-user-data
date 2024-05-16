#!/usr/bin/env python3
"""
Defines the function filter_datum.
"""
from mysql.connector import connection
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


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Sets up connection to mysql using mysql.connecter
    """
    cnxn = connection.MySQLConnection(
        user=environ.get("PERSONAL_DATA_DB_USERNAME", "root"),
        password=environ.get("PERSONAL_DATA_DB_PASSWORD", ""),
        host=environ.get("PERSONAL_DATA_DB_HOST", "localhost"),
        database=environ.get("PERSONAL_DATA_DB_NAME", ""),
        port=3306,
    )

    return cnxn


def main() -> None:
    """
    Gets users from database and logs their entries in filtered form.
    """
    db = get_db()
    cursor = db.cursor()
    users_query = "SELECT * FROM users"
    cursor.execute(users_query)

    logger = get_logger()

    for (name, email, phone,
         ssn, password, ip, last_login, user_agent) in cursor:
        message = (f"name={name}; email={email}; phone={phone}; ssn={ssn}; "
                   f"password={password}; ip={ip}; last_login={last_login}; "
                   f"user_agent={user_agent};")
        logger.info(message)


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


if __name__ == '__main__':
    main()
