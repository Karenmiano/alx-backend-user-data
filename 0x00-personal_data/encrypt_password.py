#!/usr/bin/env python3
"""
Defines the function hash_password
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Returns hashed password of password.
    """
    encode_pswd = password.encode('utf-8')

    return bcrypt.hashpw(encode_pswd, bcrypt.gensalt())
